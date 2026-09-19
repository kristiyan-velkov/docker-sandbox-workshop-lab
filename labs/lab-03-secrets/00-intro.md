# Lab 3 — Secrets & Credential Proxy

**GitHub lab:** [lab-03-secrets](https://github.com/kristiyan-velkov/docker-sandbox-workshop/tree/main/lab-03-secrets) — follow **[GUIDE.md](https://github.com/kristiyan-velkov/docker-sandbox-workshop/blob/main/lab-03-secrets/GUIDE.md)** on your machine.

This Simspace version runs the same flow in a simulated terminal.

## Why this lab matters

Agents need tokens to work — but putting credentials in a Dockerfile, `.env` committed to git, or inside the VM filesystem is how workshops become breach demos. Sandboxes use a **credential proxy**: the VM receives a sentinel placeholder, and the host overwrites the auth header on outbound HTTPS to allowed domains.

## What you'll do

1. Store a GitHub token on the host with `sbx secret set`
2. Echo `$GH_TOKEN` inside the VM and see the sentinel value
3. Make a live GitHub API call through the proxy
4. Clean up the secret

Use the **Host** terminal for `sbx secret` commands.
