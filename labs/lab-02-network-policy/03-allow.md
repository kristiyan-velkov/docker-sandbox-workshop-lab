# Allow and verify

Enable the control in **Settings**, or run on the host:

```bash terminal-id=host
sbx policy allow network www.dockerfrontend.com
```

Ask Cursor to curl again, or:

```bash terminal-id=sandbox
curl https://www.dockerfrontend.com
```
