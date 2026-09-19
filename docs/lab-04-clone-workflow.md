# Lab 4 — Step-by-step

## Setup (host)

Clone the playground (it is not vendored in this lab repo):

```bash
git clone https://github.com/kristiyan-velkov/docker-sandbox-workshop.git
```

```bash
cd docker-sandbox-workshop/workshop-app
```

```bash
npm install
```

```bash
npm run dev
```

Open the **Local** URL from the output (often **http://localhost:3000**, or **3001** if 3000 is in use) — confirm the site loads. Stop with **Ctrl+C**, then return to the repo root:

```bash
cd ..
```

All `sbx` commands below run from `docker-sandbox-workshop/` (monorepo root).

---

## Part A — Direct mode

### 1. Start sandbox

```bash
sbx run cursor workshop-app/ --name lab4-direct
```

Direct mode mounts `workshop-app/` **read-write**. Agent edits appear on the host immediately.

### 2. Agent task

> Update the hero tagline in `src/components/home-hero.tsx` to mention Docker Sandboxes. Show me the new line.

On the host, open `workshop-app/src/components/home-hero.tsx` — the edit should already be there (no fetch needed).

### 3. Clean up

```bash
sbx rm lab4-direct --force
```

---

## Part B — Clone mode

`--clone` requires the **Git repository root**. Use `.` from the monorepo root — not `workshop-app/` (that subfolder has no `.git`).

### 4. Start sandbox with `--clone`

```bash
sbx run --clone cursor . --name lab4-clone
```

Clone mode gives the agent a **private Git clone** of the whole monorepo inside the VM. Your host `main` stays read-only — remote `sandbox-lab4-clone` is added on the host.

### 5. Agent task

> Create branch `feat/lab4-test`. Add a one-line comment at the top of `workshop-app/src/lib/workshop-data.ts` noting this was edited in clone mode. Commit with message `docs: clone mode test`.

While the agent works, `git status` on host `main` should stay clean.

### 6. Fetch and review on the host

```bash
git fetch sandbox-lab4-clone
```

```bash
git log sandbox-lab4-clone/feat/lab4-test --oneline -3
```

```bash
git diff main..sandbox-lab4-clone/feat/lab4-test
```

```bash
git status
```

### 7. Push and merge into main

```bash
git checkout -b feat/lab4-test sandbox-lab4-clone/feat/lab4-test
```

```bash
git push -u origin feat/lab4-test
```

Merge (pick one):

- **PR:** GitHub → merge PR → `git checkout main && git pull origin main`
- **Local:** `git checkout main && git merge feat/lab4-test && git push origin main`

### 8. Clean up

```bash
sbx rm lab4-clone --force
```

```bash
git remote remove sandbox-lab4-clone
```

---

## Done when

- Direct mode: hero edit visible on host without fetch
- Clone mode: host `main` never dirty during agent work
- Agent commit on `origin/feat/lab4-test`, reviewed, merged into `main`

---

## Docker docs

| Topic | Link |
|-------|------|
| Workflow patterns | [Direct, clone, and worktree modes](https://docs.docker.com/ai/sandboxes/workflows/) |
| Clone mode | [Isolated Git clone in the VM](https://docs.docker.com/ai/sandboxes/workflows/#clone-mode) |
| Git workflows | [Fetch sandbox remotes on the host](https://docs.docker.com/ai/sandboxes/workflows/#git-workflows) |
