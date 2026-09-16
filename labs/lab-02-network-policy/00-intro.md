# Lab 2 — Network Policy

Sandboxes use **default-deny** network policy. Traffic leaves the VM only through a host proxy that evaluates allow/deny rules.

You will:

1. Initialize the **balanced** preset on the host
2. Prove `www.dockerfrontend.com` is blocked by default
3. Add an allow rule and curl again
4. Apply a **sandbox-scoped** deny rule

Use the **Host** tab for `sbx policy` commands and the **Sandbox** tab for the agent session.
