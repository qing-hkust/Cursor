# AGENTS.md

Academic agent workspace. Taxonomy and cloud/local guidance: [docs/agent-organization.md](docs/agent-organization.md).

## Categories (folders)

| Folder | Use for |
| --- | --- |
| `simulation/` | Sim drivers, configs, sweep scripts |
| `data-analysis/` | Analysis scripts, figures, small tables |
| `literature/` | Paper notes, digests, reading lists |
| `writing/` | Manuscripts, proposals, outlines |
| `course-prep/` | Lectures, psets, rubrics |
| `chore/` | Repo/env maintenance tasks |
| `shared/` | Cross-cutting helpers (plot style, etc.) |

Prefer **one folder per agent run**. Cloud agents only see what is in this git repo.

## Environment

- **Runtime**: Python 3.12 on Ubuntu (Cursor Cloud)
- **Dependencies**: `matplotlib` (`requirements.txt`)
- **Install**: `.cursor/environment.json` — keep lean

## Verify

```bash
python3 data-analysis/example_scientific_plot.py
```

Writes `data-analysis/example_scientific_plot.png`.

## Cloud vs local (short)

- **Cloud-friendly**: literature digests, course-prep drafts, chores, batch figure regen
- **Stay local / HPC**: interactive writing, exploratory analysis, heavy simulations
- **Mixed**: data-analysis scripts in-repo → cloud; large raw data stays outside git

## Notes

- No Docker/`start` unless services appear.
- After changing `requirements.txt`, next run refreshes via `install`.
