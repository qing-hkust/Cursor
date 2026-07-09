# AGENTS.md

## Cursor Cloud specific instructions

Small Python repo for scientific matplotlib figures. Cloud agents should start quickly with the committed `.cursor/environment.json`.

### Environment

- **Runtime**: Python 3.12 on Ubuntu (provided by Cursor Cloud)
- **Dependencies**: `matplotlib` (see `requirements.txt`)
- **Install**: handled automatically by `.cursor/environment.json` before each run

### Verify the setup

```bash
python3 example_scientific_plot.py
```

This writes `example_scientific_plot.png` in the repo root. No display server is required; figures are saved with matplotlib's default headless backend.

### Project layout

- `scientific_plot.py` — shared matplotlib style helpers (Arial 18 pt, inward ticks, legend helpers)
- `example_scientific_plot.py` — runnable example that generates a sample figure

### Notes for agents

- Keep `.cursor/environment.json` lean: only dependency install, no long-running services.
- Do not add Docker or `start` commands unless the project gains services that need them.
- After changing `requirements.txt`, the next agent run will refresh deps via `install`.
