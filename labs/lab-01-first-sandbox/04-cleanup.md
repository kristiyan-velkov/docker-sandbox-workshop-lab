# Clean up

List the sandbox, then delete it. Host files stay — `workspace/hello.txt` and `delete-me.txt` remain on disk.

## List sandboxes

```bash terminal-id=host
sbx ls
```

## Remove the sandbox

`--force` skips the confirmation prompt if a session is still attached ([usage](https://docs.docker.com/ai/sandboxes/usage/#start-stop-and-remove)):

```bash terminal-id=host
sbx rm my-sandbox --force
```

Expected: `Deleting sandbox my-sandbox...` then `Sandbox 'my-sandbox' removed`.

**Done when:** `hello.txt` exists in `workspace/`, `delete-me.txt` is still at the lab root, and `sbx ls` no longer lists `my-sandbox`.

→ [Get started](https://docs.docker.com/ai/sandboxes/get-started/) · [Usage](https://docs.docker.com/ai/sandboxes/usage/) · [CLI reference](https://docs.docker.com/reference/cli/sbx/)
