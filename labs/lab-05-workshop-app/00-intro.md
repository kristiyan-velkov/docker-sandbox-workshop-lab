# Lab 5 — Run with Kit

**GitHub lab:** [lab-05-workshop-app](https://github.com/kristiyan-velkov/docker-sandbox-workshop/tree/main/lab-05-workshop-app) — follow **[GUIDE.md](https://github.com/kristiyan-velkov/docker-sandbox-workshop/blob/main/lab-05-workshop-app/GUIDE.md)** on your machine.

Repo: [docker-sandbox-workshop](https://github.com/kristiyan-velkov/docker-sandbox-workshop)

This Simspace version runs the same flow in a simulated terminal.

## Why this lab matters

A **kit** extends an agent with network rules, startup commands, and workspace files — without a custom Docker image. The workshop kit boots a Next.js dev server and enforces allow/deny domains so you can see network policy in a real app context.

Run `sbx` from **inside** `workshop-app/` with `.` as the workspace path.

## What you'll do

1. Start Cursor with the workshop kit attached
2. Ask the agent to research allowed domains (bio + books)
3. Trigger blocked requests to denied domains
4. Inspect kit network rules and audit log

Use the **Host** terminal.
