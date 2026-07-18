from __future__ import annotations

import datetime as dt
import os
import re
import textwrap
import time
from dataclasses import dataclass, replace
from typing import Any, Iterable

import requests
import yaml
from dateutil.relativedelta import relativedelta


DEFAULT_CONTACT_EMAIL = "you@example.com"


@dataclass(frozen=True)
class Work:
    title: str
    doi: str | None
    url: str | None
    journal: str | None
    publisher: str | None
    year: int | None
    authors: str | None
    abstract: str | None
    source: str
    citation_count: int | None = None
    oa_url: str | None = None
    oa_pdf_url: str | None = None
    oa_status: str | None = None


def _norm(s: str | None) -> str:
    return (s or "").strip().lower()


def _looks_blocked(*, text: str, blocked_keywords: list[str]) -> bool:
    t = _norm(text)
    return any(k.lower() in t for k in blocked_keywords)


def _prefer_score(*, journal: str | None, preferred_keywords: list[str]) -> int:
    j = _norm(journal)
    score = 0
    for kw in preferred_keywords:
        if kw.lower() in j:
            score += 5
    return score


def load_config(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _api_settings(cfg: dict[str, Any]) -> dict[str, Any]:
    apis = cfg.get("apis", {}) or {}
    email = (apis.get("contact_email") or DEFAULT_CONTACT_EMAIL).strip()
    s2_key = (apis.get("semantic_scholar_api_key") or os.environ.get("SEMANTIC_SCHOLAR_API_KEY") or "").strip()
    return {
        "contact_email": email,
        "semantic_scholar_api_key": s2_key or None,
        "user_agent": f"lit-review-agent/0.3 (mailto:{email})",
        "unpaywall_enabled": bool((apis.get("unpaywall") or {}).get("enabled", True)),
        "semantic_scholar_enabled": bool((apis.get("semantic_scholar") or {}).get("enabled", True)),
        "semantic_scholar_sort": (apis.get("semantic_scholar") or {}).get("sort", "publicationDate"),
    }


def _validate_api_config(apis: dict[str, Any]) -> None:
    email = apis["contact_email"]
    if email in (DEFAULT_CONTACT_EMAIL, "you@example.com", "test@example.com"):
        import sys

        print(
            "Warning: set apis.contact_email in config.yaml to your real email "
            "(required by Unpaywall; placeholder addresses return 422).",
            file=sys.stderr,
        )
    if apis["semantic_scholar_enabled"] and not apis["semantic_scholar_api_key"]:
        import sys

        print(
            "Warning: Semantic Scholar runs without an API key (strict rate limits). "
            "Set SEMANTIC_SCHOLAR_API_KEY or apis.semantic_scholar_api_key.",
            file=sys.stderr,
        )


def _request_json(
    url: str,
    *,
    params: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    timeout: int = 45,
    retries: int = 2,
) -> dict[str, Any]:
    last_exc: Exception | None = None
    for attempt in range(retries + 1):
        r = requests.get(url, params=params, headers=headers, timeout=timeout)
        if r.status_code == 429 and attempt < retries:
            time.sleep(2 ** attempt)
            continue
        try:
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as exc:
            last_exc = exc
            if exc.response is not None and exc.response.status_code == 429 and attempt < retries:
                time.sleep(2 ** attempt)
                continue
            raise
    if last_exc:
        raise last_exc
    raise RuntimeError("request failed without exception")


def _extract_year_crossref(it: dict[str, Any]) -> int | None:
    for k in ("published-online", "published-print", "issued"):
        d = it.get(k, {})
        parts = (d.get("date-parts") or [[None]])[0]
        if parts and parts[0]:
            try:
                return int(parts[0])
            except Exception:
                return None
    return None


def _format_authors_crossref(authors: list[dict[str, Any]]) -> str | None:
    names: list[str] = []
    for a in authors[:8]:
        given = (a.get("given") or "").strip()
        family = (a.get("family") or "").strip()
        if given or family:
            names.append(" ".join([p for p in (given, family) if p]))
    if not names:
        return None
    if len(authors) > 8:
        names.append("et al.")
    return ", ".join(names)


def _strip_jats(s: str | None) -> str | None:
    if not s:
        return None
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s or None


def _reconstruct_openalex_abstract(inv: dict[str, list[int]] | None) -> str | None:
    if not inv:
        return None
    max_pos = max((pos for poss in inv.values() for pos in poss), default=-1)
    if max_pos < 0:
        return None
    words = [""] * (max_pos + 1)
    for word, positions in inv.items():
        for pos in positions:
            words[pos] = word
    text = " ".join(words).strip()
    return text or None


def _format_authors_openalex(authorships: list[dict[str, Any]]) -> str | None:
    names: list[str] = []
    for a in authorships[:8]:
        author = a.get("author") or {}
        name = (author.get("display_name") or "").strip()
        if name:
            names.append(name)
    if not names:
        return None
    if len(authorships) > 8:
        names.append("et al.")
    return ", ".join(names)


def _format_authors_semantic_scholar(authors: list[dict[str, Any]]) -> str | None:
    names: list[str] = []
    for a in authors[:8]:
        name = (a.get("name") or "").strip()
        if name:
            names.append(name)
    if not names:
        return None
    if len(authors) > 8:
        names.append("et al.")
    return ", ".join(names)


def _merge_work(existing: Work, incoming: Work) -> Work:
    """Combine duplicate hits from different metadata backends."""
    abstract = existing.abstract or incoming.abstract
    if existing.abstract and incoming.abstract and len(incoming.abstract) > len(existing.abstract):
        abstract = incoming.abstract

    citations = existing.citation_count
    if incoming.citation_count is not None:
        citations = max(citations or 0, incoming.citation_count)

    source = existing.source
    if incoming.source != existing.source:
        source = f"{existing.source}+{incoming.source}"

    return replace(
        existing,
        title=existing.title or incoming.title,
        doi=existing.doi or incoming.doi,
        url=existing.url or incoming.url,
        journal=existing.journal or incoming.journal,
        publisher=existing.publisher or incoming.publisher,
        year=existing.year or incoming.year,
        authors=existing.authors or incoming.authors,
        abstract=abstract,
        source=source,
        citation_count=citations,
        oa_url=existing.oa_url or incoming.oa_url,
        oa_pdf_url=existing.oa_pdf_url or incoming.oa_pdf_url,
        oa_status=existing.oa_status or incoming.oa_status,
    )


def openalex_search(query: str, *, per_page: int, from_date: dt.date, contact_email: str) -> list[Work]:
    params = {
        "search": query,
        "filter": f"from_publication_date:{from_date.isoformat()},type:article",
        "per_page": str(per_page),
        "sort": "publication_date:desc",
        "mailto": contact_email,
    }
    data = _request_json(
        "https://api.openalex.org/works",
        params=params,
        headers={"User-Agent": f"lit-review-agent/0.3 (mailto:{contact_email})"},
    )
    items = data.get("results", []) or []
    out: list[Work] = []
    for it in items:
        loc = it.get("primary_location") or {}
        src = loc.get("source") or {}
        journal = src.get("display_name")
        publisher = src.get("host_organization_name") or (it.get("host_venue") or {}).get("display_name")
        doi_raw = it.get("doi")
        doi = doi_raw.replace("https://doi.org/", "") if doi_raw else None
        url = loc.get("landing_page_url") or doi_raw or it.get("id")
        oa = it.get("open_access") or {}
        oa_url = oa.get("oa_url")
        out.append(
            Work(
                title=(it.get("display_name") or it.get("title") or "").strip(),
                doi=doi,
                url=url,
                journal=journal,
                publisher=publisher,
                year=it.get("publication_year"),
                authors=_format_authors_openalex(it.get("authorships") or []),
                abstract=_reconstruct_openalex_abstract(it.get("abstract_inverted_index")),
                source="openalex",
                citation_count=it.get("cited_by_count"),
                oa_url=oa_url,
                oa_status=oa.get("oa_status"),
            )
        )
    return out


def semantic_scholar_search(
    query: str,
    *,
    limit: int,
    from_year: int,
    api_key: str | None,
    contact_email: str,
    sort: str = "publicationDate",
) -> list[Work]:
    fields = ",".join(
        [
            "title",
            "year",
            "authors",
            "venue",
            "externalIds",
            "abstract",
            "citationCount",
            "url",
            "openAccessPdf",
            "isOpenAccess",
            "publicationDate",
        ]
    )
    headers = {"User-Agent": f"lit-review-agent/0.3 (mailto:{contact_email})"}
    if api_key:
        headers["x-api-key"] = api_key

    params: dict[str, Any] = {
        "query": query,
        "limit": str(limit),
        "fields": fields,
        "year": f"{from_year}-",
        "sort": sort,
    }
    try:
        data = _request_json(
            "https://api.semanticscholar.org/graph/v1/paper/search",
            params=params,
            headers=headers,
            timeout=60,
            retries=3,
        )
    except requests.HTTPError as exc:
        if exc.response is not None and exc.response.status_code == 429:
            return []
        raise
    items = data.get("data", []) or []
    out: list[Work] = []
    for it in items:
        ext = it.get("externalIds") or {}
        doi = ext.get("DOI")
        oa_pdf = (it.get("openAccessPdf") or {}).get("url")
        out.append(
            Work(
                title=(it.get("title") or "").strip(),
                doi=doi,
                url=it.get("url") or (f"https://doi.org/{doi}" if doi else None),
                journal=it.get("venue"),
                publisher=None,
                year=it.get("year"),
                authors=_format_authors_semantic_scholar(it.get("authors") or []),
                abstract=(it.get("abstract") or "").strip() or None,
                source="semantic_scholar",
                citation_count=it.get("citationCount"),
                oa_pdf_url=oa_pdf,
                oa_status="open" if it.get("isOpenAccess") else None,
            )
        )
    return out


def crossref_search(query: str, *, rows: int, from_date: dt.date, contact_email: str) -> list[Work]:
    params = {
        "query.bibliographic": query,
        "filter": f"from-pub-date:{from_date.isoformat()},type:journal-article",
        "rows": str(rows),
        "select": ",".join(
            [
                "title",
                "DOI",
                "URL",
                "container-title",
                "publisher",
                "published-print",
                "published-online",
                "author",
                "abstract",
            ]
        ),
        "mailto": contact_email,
        "sort": "published",
        "order": "desc",
    }
    data = _request_json(
        "https://api.crossref.org/works",
        params=params,
        headers={"User-Agent": f"lit-review-agent/0.3 (mailto:{contact_email})"},
        timeout=30,
    )
    items = data.get("message", {}).get("items", []) or []
    out: list[Work] = []
    for it in items:
        title = (it.get("title") or [""])[0] or ""
        doi = it.get("DOI")
        url = it.get("URL")
        journal = (it.get("container-title") or [""])[0] or None
        publisher = it.get("publisher")
        out.append(
            Work(
                title=title.strip(),
                doi=doi,
                url=url,
                journal=journal,
                publisher=publisher,
                year=_extract_year_crossref(it),
                authors=_format_authors_crossref(it.get("author") or []),
                abstract=_strip_jats(it.get("abstract")),
                source="crossref",
            )
        )
    return out


def unpaywall_lookup(doi: str, *, contact_email: str) -> dict[str, str | None]:
    """Resolve OA links via Unpaywall (https://unpaywall.org/products/api)."""
    try:
        data = _request_json(
            f"https://api.unpaywall.org/v2/{doi}",
            params={"email": contact_email},
            headers={"User-Agent": f"lit-review-agent/0.3 (mailto:{contact_email})"},
            timeout=20,
        )
    except requests.HTTPError as exc:
        code = exc.response.status_code if exc.response is not None else None
        if code in (404, 422):
            return {"oa_url": None, "oa_pdf_url": None, "oa_status": None}
        raise

    best = data.get("best_oa_location") or {}
    return {
        "oa_url": best.get("url_for_landing_page") or best.get("url") or data.get("oa_url"),
        "oa_pdf_url": best.get("url_for_pdf") or best.get("url"),
        "oa_status": data.get("oa_status"),
    }


def enrich_with_unpaywall(works: list[Work], *, contact_email: str, enabled: bool) -> list[Work]:
    if not enabled:
        return works

    enriched: list[Work] = []
    for i, w in enumerate(works):
        if not w.doi or (w.oa_pdf_url and w.oa_url):
            enriched.append(w)
            continue
        oa = unpaywall_lookup(w.doi, contact_email=contact_email)
        enriched.append(
            replace(
                w,
                oa_url=w.oa_url or oa["oa_url"],
                oa_pdf_url=w.oa_pdf_url or oa["oa_pdf_url"],
                oa_status=w.oa_status or oa["oa_status"],
            )
        )
        if i and i % 10 == 0:
            time.sleep(0.2)
    return enriched


def dedupe_works(works: Iterable[Work]) -> list[Work]:
    by_key: dict[str, Work] = {}
    for w in works:
        key = _norm(w.doi) or _norm(w.url) or _norm(w.title)
        if not key:
            continue
        if key in by_key:
            by_key[key] = _merge_work(by_key[key], w)
        else:
            by_key[key] = w
    return list(by_key.values())


def _year_in_window(year: int | None, *, from_year: int, to_year: int) -> bool:
    if year is None:
        return False
    return from_year <= year <= to_year


def filter_and_rank(works: list[Work], cfg: dict[str, Any], *, from_year: int) -> list[Work]:
    q = cfg["quality"]
    blocked = q.get("blocked_domain_keywords", []) or []
    preferred = q.get("preferred_journal_keywords", []) or []
    allowed_venue_any = q.get("allowed_venue_keywords_any", []) or []
    topic_any = q.get("topic_keywords_any", []) or []
    min_pref = int(q.get("min_prefer_score", 0) or 0)
    enforce = bool(q.get("enforce_blocklist", True))
    to_year = dt.date.today().year

    kept: list[Work] = []
    for w in works:
        if not _year_in_window(w.year, from_year=from_year, to_year=to_year):
            continue

        blob = " ".join([w.url or "", w.publisher or "", w.journal or "", w.title])
        if enforce and _looks_blocked(text=blob, blocked_keywords=blocked):
            continue

        topic_blob = " ".join([w.title, w.abstract or "", w.journal or "", w.publisher or ""])
        if topic_any and not any(k.lower() in _norm(topic_blob) for k in topic_any):
            continue

        if allowed_venue_any:
            venue_blob = " ".join([w.journal or "", w.publisher or ""])
            if not any(k.lower() in _norm(venue_blob) for k in allowed_venue_any):
                continue

        if min_pref > 0 and _prefer_score(journal=w.journal, preferred_keywords=preferred) < min_pref:
            continue

        kept.append(w)

    def sort_key(w: Work) -> tuple[int, int, int, int]:
        pref = _prefer_score(journal=w.journal, preferred_keywords=preferred)
        year = w.year or 0
        cites = w.citation_count or 0
        has_doi = 1 if w.doi else 0
        return (pref, year, cites, has_doi)

    return sorted(kept, key=sort_key, reverse=True)


def wiki_summary(title: str, *, user_agent: str) -> tuple[str | None, str | None]:
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{requests.utils.quote(title)}"
    r = requests.get(url, headers={"User-Agent": user_agent}, timeout=30)
    if r.status_code != 200:
        return None, None
    data = r.json()
    extract = (data.get("extract") or "").strip() or None
    page = (data.get("content_urls", {}) or {}).get("desktop", {}).get("page")
    return extract, page


def libretext_blurb(url: str, *, user_agent: str) -> tuple[str | None, str | None]:
    r = requests.get(url, headers={"User-Agent": user_agent}, timeout=30)
    if r.status_code not in (200,):
        return None, None
    html = r.text
    for pattern in (
        r'<meta\s+property="og:description"\s+content="([^"]+)"',
        r'<meta\s+name="description"\s+content="([^"]+)"',
    ):
        m = re.search(pattern, html, flags=re.I)
        if m:
            text = re.sub(r"\s+", " ", m.group(1)).strip()
            if text:
                return text, url
    return None, url


def _theme_bullets(works: list[Work], cfg: dict[str, Any]) -> list[str]:
    themes = [
        ("Zn anodes & reversibility", ["zinc anode", "mossy", "dead zinc", "hydrogen evolution", "zn ", " zn"]),
        ("Nanoporous metals & hyperuniformity", ["hyperuniform", "nanoporous", "dealloying", "saxs", "spectral density"]),
        ("Membranes & ion selectivity", ["membrane", "ion select"]),
        ("Seawater electrolysis", ["seawater", "chlorine"]),
    ]
    bullets: list[str] = []
    for label, keys in themes:
        matched = []
        for w in works[:25]:
            blob = _norm(" ".join([w.title, w.abstract or "", w.journal or ""]))
            if any(k.lower() in blob for k in keys):
                matched.append(w)
        if not matched:
            continue
        years = [w.year for w in matched if w.year]
        yr_span = f"{min(years)}–{max(years)}" if years else "recent"
        venues = sorted({w.journal for w in matched[:4] if w.journal})
        venue_note = ", ".join(venues[:3])
        bullets.append(
            f"**{label}** ({yr_span}, n={len(matched)} in top results): "
            f"active venues include {venue_note or 'see list below'}; "
            f"representative: *{matched[0].title}* ({matched[0].journal or 'n.d.'}, {matched[0].year or 'n.d.'})."
        )
    if not bullets and works:
        bullets.append(
            f"**Cross-cutting** ({works[0].year or 'n.d.'}–{works[-1].year or 'n.d.'}): "
            f"{len(works)} curated papers from preferred journals; see abstracts below."
        )
    return bullets


def _backend_label(backends: list[str]) -> str:
    labels = {
        "openalex": "OpenAlex",
        "semantic_scholar": "Semantic Scholar",
        "crossref": "Crossref",
    }
    return ", ".join(labels.get(b, b) for b in backends)


def generate_report(*, cfg: dict[str, Any], works: list[Work]) -> str:
    today = dt.date.today()
    bg = (cfg.get("project", {}) or {}).get("user_background_hint", "").strip()
    lookback = int((cfg.get("search", {}) or {}).get("lookback_years", 3))
    backends = (cfg.get("search", {}) or {}).get("backends", ["openalex", "semantic_scholar"])
    apis = _api_settings(cfg)
    ua = apis["user_agent"]

    lines: list[str] = []
    lines.append(f"# Literature review ({today.isoformat()})")
    lines.append("")
    if bg:
        lines.append("## Interpreted research background (used for search)")
        lines.append("")
        lines.append(textwrap.dedent(bg).strip())
        lines.append("")

    lines.append("## Executive summary (latest, reputable venues)")
    lines.append("")
    lines.append(
        f"_Curated from **{_backend_label(backends)}** over the last **{lookback} years**. "
        "Open-access links enriched via **Unpaywall** when DOIs are available. "
        "MDPI and similar publishers are blocked; results are ranked toward Nature-family, Joule, EES, ACS Energy Letters, JES, etc._"
    )
    lines.append("")
    if not works:
        lines.append("_No works matched current filters. Try lowering `quality.min_prefer_score` or widening `search.query_templates`._")
        lines.append("")
    else:
        for b in _theme_bullets(works, cfg):
            lines.append(f"- {b}")
        lines.append("")

    lines.append("## What’s new (curated papers)")
    lines.append("")
    if not works:
        lines.append("")
    else:
        for i, w in enumerate(works, 1):
            meta = " — ".join([p for p in [w.journal, str(w.year) if w.year else None] if p])
            ref = w.doi and f"https://doi.org/{w.doi}" or w.url or ""
            lines.append(f"### {i}. {w.title}")
            if meta:
                lines.append(f"- **Venue**: {meta}")
            if w.authors:
                lines.append(f"- **Authors**: {w.authors}")
            if w.citation_count is not None:
                lines.append(f"- **Citations**: {w.citation_count}")
            if ref:
                lines.append(f"- **DOI**: {ref}")
            if w.oa_pdf_url:
                lines.append(f"- **Open access (PDF)**: {w.oa_pdf_url}")
            elif w.oa_url:
                lines.append(f"- **Open access**: {w.oa_url}")
            if w.oa_status:
                lines.append(f"- **OA status**: {w.oa_status}")
            if w.abstract:
                snippet = w.abstract if len(w.abstract) <= 900 else w.abstract[:900].rstrip() + "…"
                lines.append(f"- **Abstract**: {snippet}")
            lines.append(f"- **Metadata source**: {w.source}")
            lines.append("")

    lines.append("## Credible web explainers (Wikipedia + LibreTexts)")
    lines.append("")
    web = cfg.get("web_explainers", {}) or {}
    for t in web.get("topics", []) or []:
        summ, page = wiki_summary(t, user_agent=ua)
        if summ and page:
            lines.append(f"### {t} (Wikipedia)")
            lines.append(summ)
            lines.append(f"- **Reference**: {page}")
            lines.append("")

    for t, url in (web.get("libretexts_urls", {}) or {}).items():
        summ, page = libretext_blurb(url, user_agent=ua)
        if not page:
            lines.append(f"### {t} (LibreTexts)")
            lines.append(f"- **Reference**: {url}")
            lines.append("")
            continue
        lines.append(f"### {t} (LibreTexts)")
        if summ:
            lines.append(summ)
        lines.append(f"- **Reference**: {page}")
        lines.append("")

    if cfg.get("output", {}).get("include_bib", True) and works:
        lines.append("## References (papers)")
        lines.append("")
        for w in works:
            ref = w.doi and f"https://doi.org/{w.doi}" or w.url or ""
            venue = w.journal or w.publisher or "Unknown venue"
            year = w.year or "n.d."
            authors = w.authors or "Unknown authors"
            lines.append(f"- {authors} ({year}). *{w.title}*. {venue}. {ref}".rstrip())
            if w.oa_pdf_url:
                lines.append(f"  - OA PDF: {w.oa_pdf_url}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def collect_works(cfg: dict[str, Any], *, from_date: dt.date) -> list[Work]:
    s = cfg["search"]
    apis = _api_settings(cfg)
    rows = int(s.get("max_results_per_query", 25))
    queries = s.get("query_templates", []) or []
    backends = s.get("backends", ["openalex", "semantic_scholar", "crossref"])
    from_year = from_date.year

    all_works: list[Work] = []
    if "openalex" in backends:
        for q in queries:
            all_works.extend(
                openalex_search(q, per_page=rows, from_date=from_date, contact_email=apis["contact_email"])
            )
    if "semantic_scholar" in backends and apis["semantic_scholar_enabled"]:
        for q in queries:
            all_works.extend(
                semantic_scholar_search(
                    q,
                    limit=rows,
                    from_year=from_year,
                    api_key=apis["semantic_scholar_api_key"],
                    contact_email=apis["contact_email"],
                    sort=apis["semantic_scholar_sort"],
                )
            )
            time.sleep(1.0)
    if "crossref" in backends:
        for q in queries:
            all_works.extend(
                crossref_search(q, rows=rows, from_date=from_date, contact_email=apis["contact_email"])
            )
    return dedupe_works(all_works)


def run(config_path: str) -> str:
    cfg = load_config(config_path)
    apis = _api_settings(cfg)
    _validate_api_config(apis)
    s = cfg["search"]
    lookback_years = int(s.get("lookback_years", 3))
    max_total = int(s.get("max_total_results", 60))

    from_date = dt.date.today() - relativedelta(years=lookback_years)
    from_year = from_date.year
    works = collect_works(cfg, from_date=from_date)
    ranked = filter_and_rank(works, cfg, from_year=from_year)[:max_total]
    ranked = enrich_with_unpaywall(ranked, contact_email=apis["contact_email"], enabled=apis["unpaywall_enabled"])
    return generate_report(cfg=cfg, works=ranked)


def save_report(md: str, *, cfg: dict[str, Any], config_path: str) -> str:
    out_cfg = cfg.get("output", {}) or {}
    report_dir = out_cfg.get("report_dir", "reports")
    template = out_cfg.get("markdown_filename_template", "literature_review_{date}.md")
    today = dt.date.today().isoformat()

    import os

    os.makedirs(report_dir, exist_ok=True)
    path = os.path.join(report_dir, template.format(date=today))
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
        f.write("\n")
        f.write("<!-- provenance -->\n")
        f.write(f"<!-- config: {config_path} -->\n")
    return path


def main() -> None:
    import argparse

    p = argparse.ArgumentParser(
        description="Literature review agent (OpenAlex, Semantic Scholar, Unpaywall, Crossref)."
    )
    p.add_argument("--config", default="config.yaml", help="Path to config.yaml")
    p.add_argument("--out", default=None, help="Write report markdown to this path (optional)")
    args = p.parse_args()

    cfg = load_config(args.config)
    md = run(args.config)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(md)
        print(args.out)
    else:
        path = save_report(md, cfg=cfg, config_path=args.config)
        print(path)


if __name__ == "__main__":
    main()
