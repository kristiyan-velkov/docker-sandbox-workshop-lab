# Clean up

Removing a clone-mode sandbox deletes the in-VM clone. Fetch first if you still need the branch.

Remove the direct-mode sandbox:

```bash terminal-id=host
sbx rm lab4-direct --force
```

Expected: `Deleting sandbox lab4-direct...` then `Sandbox 'lab4-direct' removed`.

Remove the clone-mode sandbox:

```bash terminal-id=host
sbx rm lab4-clone --force
```

Expected: `Deleting sandbox lab4-clone...` then `Sandbox 'lab4-clone' removed`.

Drop the fetch remote `sbx` added on the host:

```bash terminal-id=host
git remote remove sandbox-lab4-clone
```

→ [Clone workflow docs](https://docs.docker.com/ai/sandboxes/usage/#clone-mode)
