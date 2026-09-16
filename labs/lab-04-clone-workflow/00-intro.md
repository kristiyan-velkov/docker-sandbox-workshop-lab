# Lab 4 — Direct vs Clone Mode

| Mode | Command | Host working tree |
|------|---------|-------------------|
| **Direct** | `sbx run cursor workshop-app/` | Edits sync immediately |
| **Clone** | `sbx run --clone cursor .` | Host stays clean; fetch branch from sandbox remote |

Both modes use the monorepo at `docker-sandbox-workshop-lab/`.
