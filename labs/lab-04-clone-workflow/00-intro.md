# Lab 4 — Direct & Clone Mode

**GitHub lab:** [lab-04-clone-workflow](https://github.com/kristiyan-velkov/docker-sandbox-workshop/tree/main/lab-04-clone-workflow) — follow **[GUIDE.md](https://github.com/kristiyan-velkov/docker-sandbox-workshop/blob/main/lab-04-clone-workflow/GUIDE.md)** on your machine.

Repo: [docker-sandbox-workshop](https://github.com/kristiyan-velkov/docker-sandbox-workshop)

This Simspace version runs the same flow in a simulated terminal.

## Why this lab matters

In Lab 1 you used **direct mode** — the sandbox mounts your host folder; agent edits appear immediately. That is fine for exploration, but risky for Git: the agent can commit, stash, or dirty your main checkout.

**Clone mode** gives the sandbox a **private Git clone**. The agent branches and commits inside the VM. When done, you `git fetch sandbox-<name>` on the host, review, push, and merge.

## What you'll do

1. Edit a file in **direct mode** and see it on the host immediately
2. Start a sandbox with **`--clone`** and work in an isolated Git checkout
3. Fetch agent commits back to the host with `git fetch sandbox-<name>`

Use the **Host** terminal.
