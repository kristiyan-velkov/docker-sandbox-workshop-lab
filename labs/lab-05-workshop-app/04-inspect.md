# Inspect kit

Ask the agent:

> What did the workshop-app-nextjs kit add to this workspace? List `.cursor/rules/` and `.claude/skills/` files. Summarize `network.allowedDomains` and `commands.startup` from the kit spec.yaml.

```bash terminal-id=host
sbx exec lab5-kit -- curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:3000
```

Expected: `200`
