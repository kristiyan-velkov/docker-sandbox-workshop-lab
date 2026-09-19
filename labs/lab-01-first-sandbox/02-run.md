# First run

`sbx run` creates a microVM, mounts the current directory (`.`) as the workspace, and attaches you to Cursor. `--name my-sandbox` gives it a stable identity so you can `ls` and `rm` it later ([usage](https://docs.docker.com/ai/sandboxes/usage/#start-stop-and-remove)).

On first start, Cursor asks you to approve permissions. You do **not** need `sbx secret set` for this lab.

```bash terminal-id=host
sbx run cursor . --name my-sandbox
```

When it returns, the sandbox is running.

## Simple prompt

Type this in the Host terminal (or click Run):

```bash terminal-id=host
Say hello and tell me where you are running.
```

The reply should say it is Cursor inside a Linux microVM, and that it can only see the workspace mount.

## Create a file in the workspace

```bash terminal-id=host
Create a file named hello.txt in this workspace with a one-line greeting, then show me the file contents.
```

Because this is **direct mode**, `hello.txt` appears on the host under `workspace/`.
