# Inspect kit

Type this in the Host terminal (or click Run):

```bash terminal-id=host
What did the workshop-app-nextjs kit add to this workspace? List .cursor/rules/ and .claude/skills/ files. Summarize network.allowedDomains and commands.startup from the kit spec.yaml.
```

Confirm the sandbox is still running:

```bash terminal-id=host
sbx ls
```

Probe the kit's Next.js server from inside the VM. `sbx exec` runs the curl in the sandbox, not on your Mac:

```bash terminal-id=host
sbx exec lab5-kit -- curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:3000
```

Expected: `200`.
