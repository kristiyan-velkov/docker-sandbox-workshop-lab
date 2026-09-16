# Docker Sandboxes Workshop — Lab

Interactive Docker Sandboxes workshop built on [Simspace](https://github.com/dockersamples/simspace). Six labs covering install, network policy, secrets, clone workflow, pre-built kits, and custom kit authoring.

Two delivery tracks:

| Track | Command | URL | Terminal |
|-------|---------|-----|----------|
| **Self-paced (Simspace)** | `docker compose up dev` | http://localhost:5173 | Simulated in browser — no install |
| **Live workshop (Labspace)** | `bash start-labspace.sh` | http://localhost:3030 | Real `sbx` on your machine |

## Labs

| # | Simspace entry | Topic | Time |
|---|----------------|-------|------|
| 1 | `lab-01-first-sandbox` | Install, first sandbox, workspace boundary | ~25 min |
| 2 | `lab-02-network-policy` | Default deny, allow/deny, audit log | ~35 min |
| 3 | `lab-03-secrets` | GitHub credential proxy, sentinel values | ~20 min |
| 4 | `lab-04-clone-workflow` | Direct vs `--clone` Git workflow | ~25 min |
| 5 | `lab-05-workshop-app` | Pre-built kit, dev server, network demo | ~20 min |
| 6 | `lab-06-customize-stack` | Build your own mixin kit | ~25 min |

## Self-paced preview (Simspace)

Requires Docker only.

```bash
docker compose up dev
# → http://localhost:5173
```

Validate all labs:

```bash
docker compose run --rm validate
```

Edit content under `labs/<id>/` — each lab has `labspace.yaml`, `simulator.yaml`, and markdown sections. Push to `main` to deploy to GitHub Pages (enable Pages → Source: GitHub Actions).

## Live workshop (Labspace)

Requires `sbx`, `ttyd`, and a Cursor API key (`sbx secret set -g cursor`).

```bash
bash start-labspace.sh
# → http://localhost:3030
```

Instructions in the left panel; real terminal on the right. Content in `docs/` and `labspace.yaml`.

## Repo layout

```
labs/                    # Simspace — 6 browser labs
docs/                    # Labspace — real sbx step guides
labspace.yaml            # Labspace manifest
workshop-app/            # Next.js playground (labs 4–6)
customize/               # Templates and workshop-app-nextjs kit
kit-template/            # Blank kit scaffold for Lab 6
start-labspace.sh        # Launch live workshop track
```

## Authoring with an agent

```bash
sbx env run
```

Uses the [simspace-authoring-kit](https://hub.docker.com/r/dockersamples/simspace-authoring-kit) from `.sbxenv.yaml`. See [AGENTS.md](./AGENTS.md).

## Learn more

- [Docker Sandboxes docs](https://docs.docker.com/ai/sandboxes/)
- [Simspace specs](https://github.com/dockersamples/simspace/tree/main/spec)
- [simspace-starter](https://github.com/dockersamples/simspace-starter)
