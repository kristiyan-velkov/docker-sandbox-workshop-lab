# Initialize policy

`sbx policy init balanced` writes the global default-deny preset. It applies to every sandbox on this machine until you change it ([get started](https://docs.docker.com/ai/sandboxes/get-started/#control-what-the-agent-can-reach)):

```bash terminal-id=host
sbx policy init balanced
```

Expected: `Global network policy initialized to "balanced".`

`sbx policy ls` prints the active preset and rules:

```bash terminal-id=host
sbx policy ls
```

Start Cursor from the **Sandbox** tab. `.` is the workspace; `--name lab2` lets you target this sandbox in later `policy` and `rm` commands:

```bash terminal-id=sandbox
sbx run cursor . --name lab2
```
