# Docker Sandboxes Workshop — Live Track

Welcome! This track runs **real `sbx` commands** on your machine in the terminal panel.

## Prerequisites

- [sbx CLI](https://docs.docker.com/ai/sandboxes/get-started/) installed
- [ttyd](https://github.com/tsl0922/ttyd): `brew install ttyd`
- Cursor API key stored: `sbx secret set -g cursor`

## Quick start

```bash
bash start-labspace.sh
```

Open **http://localhost:3030** — instructions on the left, your terminal on the right.

## Two tracks in this repo

| Track | How to run | Terminal |
|-------|------------|----------|
| **Self-paced (Simspace)** | `docker compose up dev` → http://localhost:5173 | Simulated in browser |
| **Live workshop (Labspace)** | `bash start-labspace.sh` → http://localhost:3030 | Real sbx on your Mac |

Work through labs 1–6 in order. Each lab maps to the original workshop GUIDE.
