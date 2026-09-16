# Run your kit

```bash terminal-id=host
cd workshop-app
cp .env.sandbox.example .env.local
sbx run cursor . --kit ../my-workshop-kit --name lab6-my-kit
```

Ask the agent:

> Read `.claude/skills/my-workshop-kit/SKILL.md` and summarize my kit rules.
