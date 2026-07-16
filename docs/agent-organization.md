# Agent organization

## Categories (created in this workspace)

Each category has:

1. A **work folder** for files
2. A **Cursor subagent** at `.cursor/agents/<name>.md` (delegatable)
3. A nested **`AGENTS.md`** in that folder

| Category | Folder | Subagent |
| --- | --- | --- |
| Simulation | `simulation/` | `simulation` |
| Data analysis | `data-analysis/` | `data-analysis` |
| Literature | `literature/` | `literature` |
| Writing | `writing/` | `writing` |
| Course prep | `course-prep/` | `course-prep` |
| Chore | `chore/` | `chore` |
| Shared libs | `shared/` | (no primary agent) |

## How to use

- **Local / Cloud parent agent:** Task tool or `@` → pick `literature`, `data-analysis`, etc.
- **Cloud run:** point the run at this repo; ask it to use the matching category folder/subagent.
- **Dashboard cloud runs** cannot be filed into folders — organize by **which subagent/folder** you invoke, not by renaming historical runs.

## Local vs cloud

| Category | Prefer |
| --- | --- |
| Literature, course-prep, chore | Cloud |
| Data analysis | Mixed |
| Writing | Local (+ cloud drafts) |
| Simulation | Local / HPC (+ cloud for scripts) |

## File moves already done

| From | To |
| --- | --- |
| `scientific_plot.py` | `shared/scientific_plot.py` |
| Example plot | `data-analysis/` |

Moving more of your laptop files: copy them into the matching folder and push so Cloud agents can see them. Large raw data stays gitignored.
