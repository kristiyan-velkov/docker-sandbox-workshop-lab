# Clean up

Remove the global deny rule if you added one:

```bash terminal-id=host
sbx policy rm network --resource www.dockerfrontend.com
```

Expected: `Rule removed from policy local: resources=www.dockerfrontend.com`.

Delete the sandbox. Host files are untouched ([usage](https://docs.docker.com/ai/sandboxes/usage/#start-stop-and-remove)):

```bash terminal-id=host
sbx rm lab2 --force
```

Expected: `Deleting sandbox lab2...` then `Sandbox 'lab2' removed`.

→ [Local policy docs](https://docs.docker.com/ai/sandboxes/governance/local/)
