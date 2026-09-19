# Store GitHub token

Store a GitHub token on the host with `sbx secret set`. The sandbox sees a **sentinel** value; the host proxy injects the real token only for approved GitHub hosts ([stored secrets](https://docs.docker.com/ai/sandboxes/security/credentials/#stored-secrets)).

## Install the GitHub CLI

On macOS with Homebrew:

```bash terminal-id=host
brew install gh
```

Other platforms: [GitHub CLI installation](https://github.com/cli/cli#installation).

## Sign in to GitHub on the host

```bash terminal-id=host
gh auth login
```

Follow the prompts (GitHub.com → HTTPS → browser or token). Confirm you are logged in:

```bash terminal-id=host
gh auth status
```

You should see `Logged in to github.com account test-user`.

## Store the secret for sandboxes

Prompts for the token value (input is hidden). Use a placeholder in this lab — e.g. `gho_test_token`:

```bash terminal-id=host
sbx secret set github
```

Expected: `Enter secret:` then `Saved secret for service "github" in scope "(global)"`.

List stored secrets — `github` should show `SOURCE value`:

```bash terminal-id=host
sbx secret ls
```

## Start the sandbox

Global secrets apply when the sandbox is **created**. Run this after `sbx secret set`:

```bash terminal-id=host
sbx run cursor . --name lab3
```

On first start, Cursor may ask you to approve permissions — same as Lab 1.
