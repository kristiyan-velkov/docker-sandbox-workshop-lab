# Clone mode

`--clone` gives the agent a **private Git clone** inside the VM. Host `main` stays clean. The host repo is also mounted read-only at `/run/sandbox/source` ([clone mode](https://docs.docker.com/ai/sandboxes/usage/#clone-mode)).

Clone mode is fixed at create time. Run this from the **docker-sandbox-workshop** repo root (the folder that contains `.git`), not from `workshop-app/`:

```bash terminal-id=host
sbx run --clone cursor . --name lab4-clone
```

`sbx` adds a host remote named `sandbox-lab4-clone` so you can fetch the agent's branch later.

Type this in the Host terminal (or click Run):

```bash terminal-id=host
Create branch feat/lab4-test. Add a one-line comment at the top of workshop-app/src/lib/workshop-data.ts noting this was edited in clone mode. Commit with message docs: clone mode test.
```
