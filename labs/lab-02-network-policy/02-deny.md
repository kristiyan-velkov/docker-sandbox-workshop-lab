# Default deny

`www.dockerfrontend.com` is not on the balanced allow-list, so the proxy should block it.

In the **Sandbox** terminal, ask Cursor (or click Run):

```bash terminal-id=sandbox
curl https://www.dockerfrontend.com and show me the full response. Confirm this URL is blocked by sandbox network policy.
```

Expected: connection failed — default deny is working.

Then check the audit trail on the **Host** terminal:

```bash terminal-id=host
Show the sbx policy log for lab2 with the last 10 entries and which hosts were blocked.
```

Expected: `www.dockerfrontend.com` with decision **deny**.
