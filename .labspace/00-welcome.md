# Docker Sandboxes Workshop — Live Track

Welcome! This track runs **real `sbx` commands** on your machine in the terminal panel.

## Prerequisites

- [sbx CLI](https://docs.docker.com/ai/sandboxes/get-started/) installed
- [ttyd](https://github.com/tsl0922/ttyd): `brew install ttyd`
- Cursor API key stored: `sbx secret set cursor`

## Quick start

```bash
bash start-labspace.sh
```

Open **http://localhost:3030** — instructions on the left, your terminal on the right.

## Workshop presentation

**Start here if this is your first time.** The slide deck introduces Docker Sandboxes, the lab flow, and what you will build across all six hands-on exercises.

[Open the slide deck on Canva](https://canva.link/iz4w15t36689isb)

**Author:** Kristiyan Velkov  
Docker Captain  
[LinkedIn](https://www.linkedin.com/in/kristiyanvelkov) · [X](https://x.com/krisvelkov)

## Two tracks in this repo

| Track | How to run | Terminal |
|-------|------------|----------|
| **Self-paced (Simspace)** | `docker compose up dev` → http://localhost:5173 | Simulated in browser |
| **Live workshop (Labspace)** | `bash start-labspace.sh` → http://localhost:3030 | Real sbx on your Mac |

Work through labs 1–6 in order. Each lab maps to the original workshop GUIDE.
