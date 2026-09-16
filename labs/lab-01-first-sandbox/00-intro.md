# Lab 1 — Your First Sandbox

Docker Sandboxes run AI coding agents in **isolated microVMs**. Each sandbox gets its own filesystem, Docker daemon, and network — the agent can build, install, and edit without touching your host.

In this lab you will:

1. Install and sign in with `sbx`
2. Store your Cursor API key as a host secret
3. Run `sbx run cursor` and create a file in the workspace
4. Prove the agent **cannot** modify files outside the workspace mount

> **Simulated mode:** commands run in a browser terminal with scripted output. For real `sbx`, use the **Live workshop** track (`bash start-labspace.sh`).
