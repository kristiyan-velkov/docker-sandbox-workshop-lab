# Install and sign in

You do **not** need Docker Desktop. `sbx` is a standalone CLI ([install guide](https://docs.docker.com/ai/sandboxes/install/)).

Requires macOS Sonoma 14+ on Apple silicon.

## Trust Docker's Homebrew tap

Tells Homebrew that `docker/tap` is a trusted source for casks. This is a **Homebrew** command — there is no `docker tap` CLI subcommand:

```bash terminal-id=host
brew trust docker/tap
```

On older Homebrew you may see `brew tap docker/tap` instead of `brew trust` — either works in this lab.

## Install the CLI

Downloads and installs `sbx` from the tap (keep `docker/tap/sbx` as one path — do not split it into separate words):

```bash terminal-id=host
brew install docker/tap/sbx
```

## Sign in to Docker

`sbx login` opens a browser for Docker OAuth. Sign-in is required so sandboxes can pull images and use the credential proxy ([why sign-in](https://docs.docker.com/ai/sandboxes/install/#sign-in)).

When the terminal asks for **Your Docker Hub username**, enter yours (the same handle you use on Docker Hub — e.g. `krisvelkov`):

```bash terminal-id=host
sbx login
```

## Confirm the install

Prints the CLI version and whether the local daemon is running:

```bash terminal-id=host
sbx version
```

## Other machines

| Platform | Install | Guide |
|----------|---------|-------|
| Windows 11 | `winget install -h Docker.sbx` | [Install on Windows](https://docs.docker.com/ai/sandboxes/install/#install-on-windows) |
| Ubuntu 24.04+ | `curl -fsSL https://get.docker.com \| sudo REPO_ONLY=1 sh` then `sudo apt install docker-sbx` | [Install on Ubuntu](https://docs.docker.com/ai/sandboxes/install/#install-on-ubuntu) |

Full packages: [Install Docker Sandboxes](https://docs.docker.com/ai/sandboxes/install/).
