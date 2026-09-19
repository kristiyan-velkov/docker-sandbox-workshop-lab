# Workspace boundary

The workspace mount is the only host path the sandbox can change. :filelink[delete-me.txt]{path="delete-me.txt"} sits **outside** that mount — one level above `workspace/`.

From inside the sandbox the path is `../delete-me.txt`. Ask Cursor to delete it (or click Run):

```bash terminal-id=host
Try to delete ../delete-me.txt from this workspace and report whether it worked.
```

The agent runs `rm` and gets **Permission denied**. The file is not in the sandbox workspace, so it stays on the host.
