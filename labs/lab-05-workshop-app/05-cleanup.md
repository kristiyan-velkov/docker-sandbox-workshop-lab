# Clean up

`--force` is required if the agent session is still attached. Host files stay; only the microVM is deleted:

```bash terminal-id=host
sbx rm lab5-kit --force
```

Expected: `Deleting sandbox lab5-kit...` then `Sandbox 'lab5-kit' removed`.

→ [Kits docs](https://docs.docker.com/ai/sandboxes/customize/kits/)
