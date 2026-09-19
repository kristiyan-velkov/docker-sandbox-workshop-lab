# Step 2 · Fill in spec.yaml

Set your kit name, `permissions.network.allow`, env vars, and skill. See the lab [GUIDE.md](https://github.com/kristiyan-velkov/docker-sandbox-workshop/blob/main/lab-06-customize-stack/GUIDE.md) for the blank template reference.

Review the starting spec:

```bash terminal-id=host
cat my-workshop-kit/spec.yaml
```

Edit `my-workshop-kit/spec.yaml` in the IDE. Key blocks:

| Block | What to set |
|-------|-------------|
| `name` / `displayName` | Your kit id |
| `permissions.network.allow` | Domains your team needs |
| `permissions.network.deny` | Domains to block |
| `files/workspace/` | Cursor rules, Claude skills |

The bootstrap script lives at `files/home/.local/bin/workshop-bootstrap.sh`. If you change `name` in `spec.yaml`, rename the skill folder under `files/workspace/.claude/skills/` to match.
