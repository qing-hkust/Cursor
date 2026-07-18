# AGENTS.md

<<<<<<< HEAD
## Cursor Cloud specific instructions

This repository ("Cursor Agents") is currently a bare-bones project with only a `README.md`. There are no application services, dependencies, build steps, lint configs, or test frameworks configured.

### Current state

- **No source code or application logic** exists yet.
- **No package manager lockfile** (`package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `requirements.txt`, etc.).
- **No Docker/container configuration**.
- **No CI/CD pipelines**.

### When code is added

Once the codebase is populated, update this section with:
- How to install dependencies (e.g. `pnpm install`, `pip install -r requirements.txt`).
- How to run lint, tests, and the dev server.
- Any non-obvious startup caveats or environment requirements.
=======
Academic agent workspace. Categories are **folders** + **Cursor subagents** under `.cursor/agents/`.

| Category | Folder | Subagent |
| --- | --- | --- |
| Simulation | `simulation/` | `.cursor/agents/simulation.md` |
| Data analysis | `data-analysis/` | `.cursor/agents/data-analysis.md` |
| Literature | `literature/` | `.cursor/agents/literature.md` |
| Writing | `writing/` | `.cursor/agents/writing.md` |
| Course prep | `course-prep/` | `.cursor/agents/course-prep.md` |
| Chore | `chore/` | `.cursor/agents/chore.md` |

Delegate with the Task tool / `@` to the matching subagent. Each folder also has its own `AGENTS.md`.

Details: [docs/agent-organization.md](docs/agent-organization.md).

## Markdown math

Use GitHub-friendly delimiters in notes: inline `$...$`, display `$$...$$` (not `\(...\)` / `\[...\]`).

## Environment

- Python 3.12; deps in `requirements.txt`; install via `.cursor/environment.json` (keep lean)

## Verify

```bash
python3 data-analysis/example_scientific_plot.py
```

## Cloud vs local

- **Cloud:** literature, course-prep, chore, batch data-analysis
- **Local/HPC:** interactive writing, exploratory analysis, heavy simulation
>>>>>>> origin/main
