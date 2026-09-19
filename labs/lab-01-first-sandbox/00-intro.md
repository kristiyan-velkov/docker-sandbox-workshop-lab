# Lab 1 — Run Your First Docker Sandbox

**GitHub lab:** [lab-01-first-sandbox](https://github.com/kristiyan-velkov/docker-sandbox-workshop/tree/main/lab-01-first-sandbox) — clone the folder and follow **[GUIDE.md](https://github.com/kristiyan-velkov/docker-sandbox-workshop/blob/main/lab-01-first-sandbox/GUIDE.md)** on your machine.

This Simspace version runs the same flow in a simulated terminal — no install required.

## Why this lab matters

This is the foundation of the workshop. Before network policy or secrets, you need to see what a sandbox **is**: a separate microVM with its own kernel. The agent runs inside that VM; only `workspace/` syncs from your disk — files outside that folder stay on the host.

## What you'll do

1. Install the `sbx` CLI and sign in to Docker
2. Start a named sandbox — Cursor asks for permissions on first run
3. Create `hello.txt` in the workspace
4. Prove `delete-me.txt` outside the workspace cannot be deleted
5. List sandboxes and remove the sandbox

Use the **Host** terminal on the right. Click **Run** on each block, or type the command yourself.
