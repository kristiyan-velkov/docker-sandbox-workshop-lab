# Lab 3 — Step-by-step

Work from **`lab-03-secrets/workspace/`** unless noted.

## 1. Store the GitHub token on the host

Requires the **GitHub CLI** (`gh`) installed and logged in. Run this **before** `sbx run` — global secrets apply when the sandbox is created.

Install `gh` (macOS):

```bash
brew install gh
```

Sign in and confirm:

```bash
gh auth login
```

```bash
gh auth status
```

Register the dynamic secret — `sbx` stores the command, not the token ([dynamic secrets](https://docs.docker.com/ai/sandboxes/security/credentials/#use-a-dynamic-secret-source)):

```bash
sbx secret set github --command 'gh auth token'
```

```bash
sbx secret ls
```

Never commit tokens to this repository.

## 2. Start Cursor from the workspace

```bash
cd lab-03-secrets/workspace
```

```bash
sbx run cursor . --name lab3
```

## 3. Prove GitHub access

Ask Cursor to confirm GitHub works through the credential proxy:

```bash
Prove you have access to GitHub from this sandbox. Run gh auth status or git ls-remote against a public repo and show me the result.
```

Expected: `gh auth status` or `git ls-remote` succeeds — credentials came from the host, not a token in the repo.

## 4. Clean up

```bash
sbx ls
```

```bash
sbx rm lab3 --force
```

On a shared machine, remove the GitHub secret:

```bash
sbx secret rm github --force
```

Confirm:

```bash
sbx ls
```

```bash
sbx secret ls
```

---

## Docker docs

| Topic | Link |
|-------|------|
| Credential proxy | [Secrets and outbound injection](https://docs.docker.com/ai/sandboxes/security/credentials/) |
| GitHub token | [GitHub service in credentials docs](https://docs.docker.com/ai/sandboxes/security/credentials/#github-token) |
| Security | [Sandbox security model](https://docs.docker.com/ai/sandboxes/security/) |
| Network policy | [Local governance and allow-lists](https://docs.docker.com/ai/sandboxes/governance/local/) |
