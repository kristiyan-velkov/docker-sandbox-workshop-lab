# Lab 6 — Step-by-step

From **docker-sandbox-workshop** monorepo root (Lab 4 clone). Final lab — create your custom kit.

## Step 1 · Copy kit template

Copy the Lab 6 kit template to `my-workshop-kit/` at repo root. Inspect `spec.yaml` and `files/` before editing.

```bash
cd docker-sandbox-workshop
cp -r lab-06-customize-stack/kit-template ./my-workshop-kit
ls my-workshop-kit/
```

You should see `spec.yaml`, `README.md`, and `files/home/` + `files/workspace/`.

## Step 2 · Fill in spec.yaml

Set your kit name, `permissions.network.allow`, env vars, and skill.

```bash
cat my-workshop-kit/spec.yaml
```

Edit each block:

| Block | What to set |
|-------|-------------|
| `name` / `displayName` | Your kit id — e.g. `acme-nextjs-kit` |
| `description` | Short summary for `sbx kit inspect` |
| `permissions.network.allow` | Domains your team needs (`registry.npmjs.org`, APIs, docs) |
| `permissions.network.deny` | Domains to block (`google.com`, `linkedin.com`, …) |
| `environment.variables` | Non-secret env in the VM |
| `setup.startup` | Pre-wired to `workshop-bootstrap.sh` — tweak `description` if you like |

Bootstrap script is already in `files/home/.local/bin/workshop-bootstrap.sh` — `cd ${WORKDIR}`, `npm ci`, `npm run dev :3000`.

## Step 3 · Customize & validate

Edit `my-workshop-kit/files/workspace/.claude/skills/my-workshop-kit/SKILL.md` with your team rules. If you change `name` in `spec.yaml`, rename the skill folder to match.

```bash
sbx kit validate ./my-workshop-kit
sbx kit inspect ./my-workshop-kit
```

Fix every error before running.

## Step 4 · Run your kit

Launch Cursor on `workshop-app/` with your custom kit. Wait for `npm ci` and the background dev server.

```bash
cp workshop-app/.env.sandbox.example workshop-app/.env.local
cd workshop-app
sbx run cursor . --kit ../my-workshop-kit --name lab6-my-kit
```

## Step 5 · Verify

Confirm HTTP 200, kit skill in workspace, and the agent reads your kit instructions.

```bash
sbx ls
sbx exec lab6-my-kit -- curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:3000
sbx exec lab6-my-kit -- test -f .claude/skills/my-workshop-kit/SKILL.md && echo "skill OK"
```

Agent prompt:

> Read `.claude/skills/my-workshop-kit/SKILL.md` and summarize my kit rules.

## Step 6 · Clean up

```bash
sbx rm lab6-my-kit --force
```

Keep `./my-workshop-kit/` — reuse it on any project with `--kit ../my-workshop-kit`.

---

## Blank template reference

Starting point in `kit-template/spec.yaml`:

```yaml
schemaVersion: "2"
kind: mixin
name: my-workshop-kit
displayName: My workshop kit
description: >-
  Custom kit template for Lab 6

permissions:
  network:
    allow:
      - registry.npmjs.org
    deny:
      - google.com

environment:
  variables:
    NEXT_TELEMETRY_DISABLED: "1"

setup:
  startup:
    - command: [sh, /home/agent/.local/bin/workshop-bootstrap.sh]
      user: "1000"
      background: true
      description: npm ci (if needed) and Next.js dev server on :3000
```

### Block-by-block

| Block | What it does |
|-------|----------------|
| `schemaVersion: "2"` | Required. Kit spec v2 — [kit-reference](https://docs.docker.com/ai/sandboxes/customize/kit-reference/). |
| `kind: mixin` | Extends an existing agent (`cursor`). Use `kind: sandbox` + `sandbox:` block for a full custom agent. |
| `name` / `displayName` / `description` | Identity — `name` is the CLI identifier. |
| `permissions.network.allow` | Domains the proxy permits. |
| `permissions.network.deny` | Explicit blocks — deny wins over allow. |
| `environment.variables` | Non-secret env in the VM. |
| `files/home/` | Bootstrap script → `/home/agent/` — npm ci + dev server. |
| `setup.startup` | Runs every start; `background: true` for dev server. |
| `setup.install` | Agent/tool installs (`curl \| bash`) at create time — not `npm ci` in mounted workspaces. |
| `files/workspace/` | Static files copied into workspace — rules, skills, `.env` examples. |

Full field reference: [Kit spec reference](https://docs.docker.com/ai/sandboxes/customize/kit-reference/) · [SPEC-REFERENCE.md](../customize/SPEC-REFERENCE.md)

---

## Docker docs

| Topic | Link |
|-------|------|
| Customize | [Templates, kits, and mixins](https://docs.docker.com/ai/sandboxes/customize/) |
| Kit reference | [Kit spec reference](https://docs.docker.com/ai/sandboxes/customize/kit-reference/) |
