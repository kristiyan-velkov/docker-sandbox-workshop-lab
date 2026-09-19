# Step 5 · Verify

Confirm HTTP 200, kit skill in workspace, and the agent reads your kit instructions.

List sandboxes:

```bash terminal-id=host
sbx ls
```

Check the dev server responds inside the VM:

```bash terminal-id=host
sbx exec lab6-my-kit -- curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:3000
```

Expected: `200`.

Confirm the kit skill was copied into the workspace:

```bash terminal-id=host
sbx exec lab6-my-kit -- test -f .claude/skills/my-workshop-kit/SKILL.md && echo "skill OK"
```

Expected: `skill OK`.

Type this in the Host terminal (or click Run):

```bash terminal-id=host
Read .claude/skills/my-workshop-kit/SKILL.md and summarize my kit rules.
```
