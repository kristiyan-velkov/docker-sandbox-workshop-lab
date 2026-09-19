# Prove GitHub access

The host stores your GitHub token with `sbx secret set github`. Inside the sandbox, Cursor sees a **sentinel** value — the proxy swaps it for the real token only on approved GitHub hosts.

Ask Cursor to prove it can reach GitHub (or click Run):

```bash terminal-id=host
Prove you have access to GitHub from this sandbox. Run gh auth status or git ls-remote against a public repo and show me the result.
```

Expected: `gh auth status` shows your GitHub account, or `git ls-remote` returns refs — credentials came through the host proxy, not a token pasted in the repo.
