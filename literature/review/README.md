# Literature Review Agent (OpenAlex + Semantic Scholar + Unpaywall)

Configurable agent that generates a **“latest literature”** markdown report tailored to your research background.

## Data sources

| Service | Role | Install / auth |
|---------|------|----------------|
| **OpenAlex** | Primary search: venue, DOI, abstract, citations, OA flag | No key; set `apis.contact_email` |
| **Semantic Scholar** | Search + abstracts + citation counts + OA PDF hints | Optional free API key (recommended) |
| **Unpaywall** | Resolves **open-access PDF/HTML** from DOI | No key; requires `apis.contact_email` |
| **Crossref** | Optional metadata fallback | Uses `contact_email` as `mailto` |

There is **no pip package** for these — they are REST APIs called via `requests` (already in `requirements.txt`).

## Quickstart

```bash
cd "literature/review"
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 1) Set your email in config.yaml → apis.contact_email (required for Unpaywall)

# 2) Optional: Semantic Scholar API key (higher rate limits)
export SEMANTIC_SCHOLAR_API_KEY="your-key-here"
# Or set apis.semantic_scholar_api_key in config.yaml

python lit_review.py --config config.yaml
```

Report path is printed under `reports/`.

## API setup

### Unpaywall
- Docs: https://unpaywall.org/products/api
- **Requires** a valid email in `apis.contact_email`
- Used after filtering to attach `Open access (PDF)` links to each DOI

### OpenAlex
- Docs: https://docs.openalex.org/
- **Polite pool**: pass `mailto=` (wired to `contact_email`)
- Enabled via `search.backends: [openalex, ...]`

### Semantic Scholar
- Docs: https://api.semanticscholar.org/api-docs/
- **Without key**: low rate limits (fine for small runs)
- **With key**: request at https://www.semanticscholar.org/product/api#api-key-form
- Set `SEMANTIC_SCHOLAR_API_KEY` or `apis.semantic_scholar_api_key`
- Sort options: `publicationDate`, `citationCount`, `relevance`

## Customize

Edit `config.yaml`:
- `search.query_templates` — topic queries
- `search.backends` — `openalex`, `semantic_scholar`, `crossref`
- `apis.contact_email` — **required** for Unpaywall
- `apis.semantic_scholar_api_key` — optional
- `quality.*` — venue blocklist / prefer list
- `web_explainers.*` — Wikipedia + LibreTexts

## Notes

- Does **not** scrape Google Scholar (no official API).
- Does **not** download paywalled full text; OA links only where Unpaywall/S2 find them.
- Merge logic dedupes by DOI and combines metadata from multiple backends.
