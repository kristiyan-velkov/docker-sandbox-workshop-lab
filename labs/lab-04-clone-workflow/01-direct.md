# Direct mode

Direct mode is the default. `sbx run` bind-mounts the host folder into the VM. Agent edits land on disk immediately — there is no fetch step ([Git workspace modes](https://docs.docker.com/ai/sandboxes/usage/#git-workspace-modes)).

Run from the **docker-sandbox-workshop** repo root (after `cd ..` in setup). The prompt should show `docker-sandbox-workshop$`. `workshop-app/` is the workspace path. `--name lab4-direct` is the stable id for later `rm`:

```bash terminal-id=host
sbx run cursor workshop-app/ --name lab4-direct
```

Type this in the Host terminal (or click Run):

```bash terminal-id=host
Update the hero tagline in src/components/home-hero.tsx to mention Docker Sandboxes. Show me the new line.
```

The edit appears on the host immediately — open :filelink[home-hero.tsx]{path="workshop-app/src/components/home-hero.tsx"}.
