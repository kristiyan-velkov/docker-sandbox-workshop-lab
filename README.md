# Docker Sandboxes Workshop — Lab

Interactive Docker Sandboxes workshop built on [Simspace](https://github.com/dockersamples/simspace). Six browser labs mirror the hands-on **[GitHub workshop labs](https://github.com/kristiyan-velkov/docker-sandbox-workshop)** — each card links to the matching folder (e.g. [lab-01-first-sandbox](https://github.com/kristiyan-velkov/docker-sandbox-workshop/tree/main/lab-01-first-sandbox)). A featured **Canva presentation** callout sits above **Choose a lab**.

Two delivery tracks:

| Track | Command | URL | Terminal |
|-------|---------|-----|----------|
| **Self-paced (Simspace)** | `docker compose up dev` | http://localhost:5173 | Simulated in browser — no install |
| **Live workshop (Labspace)** | `bash start-labspace.sh` | http://localhost:3030 | Real `sbx` on your machine |

## Catalog

| Entry | Simspace id | Topic | Time |
|-------|-------------|-------|------|
| Presentation | Canva (landing callout) | Workshop overview | ~5 min |
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

The landing page shows a featured **Your workshop presentation** callout (Canva link, author credit) above **Choose a lab** and the six hands-on lab cards. Author: Kristiyan Velkov · Docker Captain · [LinkedIn](https://www.linkedin.com/in/kristiyanvelkov) · [X](https://x.com/krisvelkov).

Validate all labs:

```bash
docker compose run --rm validate
```

Edit content under `labs/<id>/` — each lab has `labspace.yaml`, `simulator.yaml`, and markdown sections. Push to `main` to validate and build the static site; deploy runs when GitHub Pages is enabled (**Settings → Pages → Source: GitHub Actions**). Private repos need a plan that includes Pages, or make the repo public.

## Live workshop (Labspace)

Requires `sbx`, `ttyd`, and a Cursor API key (`sbx secret set cursor`).

```bash
bash start-labspace.sh
# → http://localhost:3030
```

Instructions in the left panel; real terminal on the right. Content in `docs/` and `labspace.yaml`.

## Playground app (labs 4–6)

This repo does not include the Next.js app. Clone it and install packages:

```bash
git clone https://github.com/kristiyan-velkov/docker-sandbox-workshop.git
cd docker-sandbox-workshop/workshop-app
npm install
```

Source: [github.com/kristiyan-velkov/docker-sandbox-workshop](https://github.com/kristiyan-velkov/docker-sandbox-workshop)

## Repo layout

```
labs/                    # Simspace — 6 browser labs
slides/                  # Optional in-browser deck (authoring reference)
public/                  # Landing-page callout (config + promo assets)
docs/                    # Labspace — real sbx step guides
labspace.yaml            # Labspace manifest
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
