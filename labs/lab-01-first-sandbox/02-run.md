# Secrets and first run

Store your Cursor API key on the **host** — never in a repo file:

```bash terminal-id=host
sbx secret set -g cursor
sbx secret ls
```

Start your first sandbox from the workspace folder:

```bash terminal-id=host
sbx run cursor . --name my-sandbox
```

When Cursor starts, ask the agent:

> Create a file named `hello.txt` in this workspace with a one-line greeting, then show me the file contents.
