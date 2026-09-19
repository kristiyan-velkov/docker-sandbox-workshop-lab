# Deny after removing the allow rule

Rules are **not updated in place**. If `www.dockerfrontend.com` is already allowed, a global deny conflicts with the existing allow rule.

Try denying on the **Host** terminal:

```bash terminal-id=host
sbx policy deny network www.dockerfrontend.com
```

Expected: an error naming the conflicting allow rule UUID.

Remove the allow rule by **resource** first:

```bash terminal-id=host
sbx policy rm network --resource www.dockerfrontend.com
```

Expected: `Rule removed from policy local: resources=www.dockerfrontend.com`.

Now add the global deny:

```bash terminal-id=host
sbx policy deny network www.dockerfrontend.com
```

In the **Sandbox** terminal, ask Cursor to curl again (or click Run):

```bash terminal-id=sandbox
curl https://www.dockerfrontend.com again and show the response. Confirm the request is blocked by policy again.
```

Expected: blocked — the global deny is active after the allow rule was removed.
