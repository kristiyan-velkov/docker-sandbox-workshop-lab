# Lab 2 — Network Policy

**GitHub lab:** [lab-02-network-policy](https://github.com/kristiyan-velkov/docker-sandbox-workshop/tree/main/lab-02-network-policy) — follow **[GUIDE.md](https://github.com/kristiyan-velkov/docker-sandbox-workshop/blob/main/lab-02-network-policy/GUIDE.md)** on your machine.

This Simspace version runs the same flow in a simulated terminal.

## Why this lab matters

Agents need network access — but unrestricted outbound traffic is how supply-chain attacks and data exfiltration happen. Sandboxes route HTTP(S) through a **host-side proxy** with an allow-list. You will curl `www.dockerfrontend.com`, confirm policy blocks it by default, allow that host, then block it again for this sandbox only.

## What you'll do

1. Initialize the **balanced** preset on the host
2. Prove `www.dockerfrontend.com` is blocked by default
3. Add an allow rule and curl again
4. Remove the allow rule, add a global deny, and confirm curl is blocked again

Use the **Host** tab for `sbx policy` commands and the **Sandbox** tab for the agent session.
