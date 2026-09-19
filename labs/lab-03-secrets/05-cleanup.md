# Clean up

List the sandbox, remove it, then drop the GitHub secret on a shared machine.

## List sandboxes

```bash terminal-id=host
sbx ls
```

You should still see `lab3` running or stopped.

## Remove the sandbox

Deletes the microVM. Host files stay ([usage](https://docs.docker.com/ai/sandboxes/usage/#start-stop-and-remove)):

```bash terminal-id=host
sbx rm lab3 --force
```

Expected: `Deleting sandbox lab3...` then `Sandbox 'lab3' removed`.

## Remove the GitHub secret

On a shared machine, remove the secret so the next user does not inherit your GitHub credential:

```bash terminal-id=host
sbx secret rm github --force
```

Expected: `Removed secret for service "github" from scope "(global)"`.

## Confirm

```bash terminal-id=host
sbx ls
```

```bash terminal-id=host
sbx secret ls
```

**Done when:** `lab3` is gone from `sbx ls` and `github` no longer appears in `sbx secret ls`.

→ [Credentials docs](https://docs.docker.com/ai/sandboxes/security/credentials/)
