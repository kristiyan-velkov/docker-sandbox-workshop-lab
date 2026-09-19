# Step 3 · Customize & validate

Edit the skill `SKILL.md`, then validate until zero errors.

Open `my-workshop-kit/files/workspace/.claude/skills/my-workshop-kit/SKILL.md` and add your team rules.

Validate the kit:

```bash terminal-id=host
sbx kit validate ./my-workshop-kit
```

Inspect the resolved kit — name, network allow/deny, and startup:

```bash terminal-id=host
sbx kit inspect ./my-workshop-kit
```

Fix every error before the next step.
