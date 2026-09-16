# Customize spec.yaml

Edit `my-workshop-kit/spec.yaml`:

| Block | What to set |
|-------|-------------|
| `name` / `displayName` | Your kit id |
| `network.allowedDomains` | Domains your team needs |
| `network.deniedDomains` | Domains to block |
| `files/workspace/` | Cursor rules, Claude skills |

Bootstrap script: `files/home/.local/bin/workshop-bootstrap.sh`
