# Lab 1 — Step-by-step

Work from **`lab-01-first-sandbox/workspace/`** unless noted. This track runs **real** `sbx` on your machine ([get started](https://docs.docker.com/ai/sandboxes/get-started/), [usage](https://docs.docker.com/ai/sandboxes/usage/)).

## 1. Trust the Homebrew tap

Tells Homebrew that `docker/tap` is a trusted source. Use **`brew trust`** — not `docker tap` (that is not a Docker CLI command):

```bash
brew trust docker/tap
```

## 2. Install the sbx CLI

You do not need Docker Desktop. `sbx` is a standalone CLI ([install](https://docs.docker.com/ai/sandboxes/install/)). Keep the cask path as one token:

```bash
brew install docker/tap/sbx
```

Windows 11: `winget install -h Docker.sbx` — [guide](https://docs.docker.com/ai/sandboxes/install/#install-on-windows).

Ubuntu 24.04+: add Docker's apt repo, then `sudo apt install docker-sbx` — [guide](https://docs.docker.com/ai/sandboxes/install/#install-on-ubuntu).

## 3. Sign in to Docker

Opens a browser for Docker OAuth. Required to pull images and use the credential proxy:

```bash
sbx login
```

## 4. Confirm the install

```bash
sbx version
```

Expect `sbx version 0.43.0` or newer.

## 5. Start your first sandbox

On first start, Cursor asks you to approve permissions. You do not need `sbx secret set` for this lab.

```bash
cd lab-01-first-sandbox/workspace
```

```bash
sbx run cursor . --name my-sandbox
```

## 6. Simple hello prompt

```bash
Say hello and tell me where you are running.
```

## 7. Create `hello.txt`

```bash
Create a file named hello.txt in this workspace with a one-line greeting, then show me the file contents.
```

## 8. Workspace boundary

`delete-me.txt` is outside the workspace mount. Ask Cursor to delete it:

```bash
Try to delete ../delete-me.txt from this workspace and report whether it worked.
```

Expected: `Permission denied`. The file is not in the sandbox, so it stays on the host.

## 9. List and remove the sandbox

```bash
sbx ls
```

```bash
sbx rm my-sandbox --force
```

**Done when:** `hello.txt` exists in `workspace/`, `delete-me.txt` is still at the lab root, and `sbx ls` no longer lists `my-sandbox`.

---

## Docker docs

| Topic | Link |
|-------|------|
| Install | [macOS, Windows, Ubuntu, packages](https://docs.docker.com/ai/sandboxes/install/) |
| Get started | [Install sbx and first sandbox](https://docs.docker.com/ai/sandboxes/get-started/) |
| Cursor agent | [API key and configuration](https://docs.docker.com/ai/sandboxes/agents/cursor/) |
| Credentials | [Stored secrets (`sbx secret set`)](https://docs.docker.com/ai/sandboxes/security/credentials/#stored-secrets) |
| Usage | [Start, stop, exec, clone mode](https://docs.docker.com/ai/sandboxes/usage/) |
| Architecture | [MicroVM isolation model](https://docs.docker.com/ai/sandboxes/architecture/) |
| CLI reference | [sbx command reference](https://docs.docker.com/reference/cli/sbx/) |
