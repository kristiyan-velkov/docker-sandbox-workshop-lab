# Lab 3 — Secrets & Credential Proxy

API keys are stored on the **host** and injected into outbound HTTP headers by a proxy. Inside the VM, credentials appear as **sentinel values** — shaped like tokens but useless if exfiltrated.

You still need `sbx secret set -g cursor` from Lab 1 for the agent.
