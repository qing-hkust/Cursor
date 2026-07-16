# AGENTS.md

Short index for Cursor Cloud agents in this repo. Full taxonomy and migration steps: [docs/agent-organization.md](docs/agent-organization.md).

## Categories (use in agent titles)

| Prefix | Use for |
| --- | --- |
| `[impl]` | Scoped code changes / features |
| `[review]` | Diff critique, security, style |
| `[chore]` | Deps, digests, cleanup |
| `[research]` | Papers, model choice, docs |
| `[domain]` | Scientific matplotlib / plot style |

Example title: `[domain] cursor: adjust inward-tick defaults`

## Environment

- **Runtime**: Python 3.12 on Ubuntu (Cursor Cloud)
- **Dependencies**: `matplotlib` (see `requirements.txt`)
- **Install**: `.cursor/environment.json` (keep lean — no HF/torch here)

## Verify

```bash
python3 example_scientific_plot.py
```

Writes `example_scientific_plot.png` in the repo root (headless; no display server).

## Layout

- `scientific_plot.py` — shared style helpers (Arial 18 pt, inward ticks, legend helpers)
- `example_scientific_plot.py` — sample figure generator
- `.cursor/rules/{core,domain,quality}/` — categorized project rules
- `docs/agent-organization.md` — reorganization proposal

## Notes

- Keep `.cursor/environment.json` lean: dependency install only, no long-running services.
- Do not add Docker or `start` commands unless the project gains services that need them.
- After changing `requirements.txt`, the next agent run refreshes deps via `install`.
- Prefer one category and one outcome per agent run.
