# Docker Sandboxes Workshop Lab — Agent Rules

Simspace + Labspace workshop on [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/).

## Repo layout

| Path | Purpose |
|------|---------|
| `labs/` | Simspace entries — `labspace.yaml`, `simulator.yaml`, `*.md` per lab |
| `docs/` | Labspace live-track guides (real `sbx` commands) |
| `labspace.yaml` | Labspace manifest for `start-labspace.sh` |
| `customize/` | Sandbox templates and `workshop-app-nextjs` kit |
| `kit-template/` | Blank kit for Lab 6 |

Playground for labs 4–6 (not in this repo):

```bash
git clone https://github.com/kristiyan-velkov/docker-sandbox-workshop.git
cd docker-sandbox-workshop/workshop-app
npm install
```

## Two tracks

1. **Simspace** — `docker compose up dev` → http://localhost:5173 (simulated terminal)
2. **Labspace** — `bash start-labspace.sh` → http://localhost:3030 (real sbx)

## Authoring Simspace labs

```bash
sbx env run                    # agent with authoring skills
docker compose up dev          # preview at :5173
docker compose run --rm validate
```

Edit `labs/<id>/`:
- `labspace.yaml` — title, sections, steps, files, terminals
- `simulator.yaml` — command scenarios, state, agent prompts
- `*.md` — instruction sections (use `terminal-id=host` on code blocks)

Labs and live-track docs are authored in `labs/` and `docs/`. Validate with `docker compose run --rm validate`.

## Security

- Never commit API keys or `.env.local`
- Use fake hosts in examples (`evil.example.com`)
- Do not disable network deny rules in lab scenarios

## References

- [Simspace specs](https://github.com/dockersamples/simspace/tree/main/spec)
- [Docker Sandboxes docs](https://docs.docker.com/ai/sandboxes/)
- [sbx CLI reference](https://docs.docker.com/reference/cli/sbx/)
