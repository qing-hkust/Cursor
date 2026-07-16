# Agent workspace organization

Academic work categories for this Cursor agents repo — not software-engineering labels.

## Do these categories make sense?

Yes. They match how research/teaching work actually splits:

| Category | What lives here |
| --- | --- |
| `simulation/` | Run scripts, configs, parameter sweeps, post-process hooks |
| `data-analysis/` | Notebooks/scripts, figures, small derived tables |
| `literature/` | Notes, bib snippets, paper digests, reading lists |
| `writing/` | Paper/proposal/thesis drafts and outlines |
| `course-prep/` | Lectures, problem sets, grading rubrics, slides outlines |
| `chore/` | Env maintenance, regenerating assets, repo hygiene |
| `shared/` | Cross-cutting code (e.g. matplotlib style) |

Keep **one primary category per agent run**. “Other chore” is fine as a catch-all; don’t invent more buckets until one of these is chronically overloaded.

## Local vs cloud — which goes where?

Cursor **cloud agents clone this GitHub repo**, work on a branch, and open a PR. They do **not** see arbitrary files on your laptop unless those files are committed (or fetched via configured storage/MCP).

| Category | Prefer | Why | Cloud works well when… |
| --- | --- | --- | --- |
| **Literature** | **Cloud** | Async, web/MCP search, markdown notes as PRs | You want digests while AFK; outputs are text in `literature/` |
| **Course prep** | **Cloud** | Bounded artifacts (outline, pset draft) | Prompt is specific; materials land in `course-prep/` |
| **Chore** | **Cloud** | Repeatable, low judgment | Regen plots, bump deps, tidy READMEs via automation |
| **Data analysis** | **Mixed** | Exploration needs you; batch jobs don’t | Scripts + small data are in-repo; agent runs analysis and updates figures |
| **Writing** | **Local** (cloud for drafts) | Prose needs tight steering | Cloud: “draft §2 from `literature/` notes”; you edit locally after |
| **Simulation** | **Local / HPC** | Heavy compute ≠ Cursor’s default VM | Cloud: write/fix drivers & configs; run big jobs on your cluster, commit results summaries only |

### Rule of thumb

- **Cloud** = bounded task, repo already has inputs, success is a diff/PR you can review later.
- **Local** = interactive judgment, huge data, GUI tools, or HPC that the Cursor VM cannot reach.

### How a cloud run works for these categories

1. Put inputs in the matching folder (and push to GitHub).
2. Start a cloud agent on this repo with a plain-language goal, e.g. *“In `literature/`, draft a one-page digest of papers on X; cite links.”*
3. Agent branches → edits only that area → opens a PR.
4. You merge or refine locally.

Optional later: **Automations** (cron / Slack) for chore + weekly literature digests.

## Moving files: local folders vs “cloud”

| Goal | What to do |
| --- | --- |
| Organize on disk for you **and** agents | Move into the category folders in **this repo** (done below). Cloud agents see the same tree after push. |
| Make something available to cloud agents | **Commit + push** it (or store externally and document the fetch path). There is no separate “Cursor cloud drive.” |
| Keep large/private data off GitHub | Leave outside the repo (or gitignore); point agents at paths/secrets/MCP. Don’t commit raw sim dumps or proprietary datasets. |
| Split by machine | Laptop = interactive `writing/` + exploratory analysis; GitHub = source of truth cloud agents clone; HPC = simulation binaries/outputs, with only scripts/summaries in git. |

### This PR’s file moves

| From (repo root) | To |
| --- | --- |
| `scientific_plot.py` | `shared/scientific_plot.py` |
| `example_scientific_plot.py` | `data-analysis/example_scientific_plot.py` |
| `example_scientific_plot.png` | `data-analysis/example_scientific_plot.png` |

Empty category folders include a short README so the next agent knows what belongs there.

## What not to do

- Don’t use engineering prefixes like `[impl]` — category **folders** are the organizer; agent titles can be normal English.
- Don’t install HPC/GPU stacks into `.cursor/environment.json` just for chore/literature runs — keep the cloud env lean; add heavier envs only if you dedicate a repo/environment to simulation.
- Don’t put all six categories’ secrets into one mega-prompt — scope the agent to one folder.
