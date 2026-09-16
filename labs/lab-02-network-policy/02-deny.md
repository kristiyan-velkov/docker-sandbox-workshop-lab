# Default deny

In the sandbox, ask Cursor:

> curl https://www.dockerfrontend.com and show me the full response. Confirm this URL is blocked by sandbox network policy.

Or run curl directly:

```bash terminal-id=sandbox
curl https://www.dockerfrontend.com
```

Check the audit log on the host:

```bash terminal-id=host
sbx policy log lab2 --limit 10
```
