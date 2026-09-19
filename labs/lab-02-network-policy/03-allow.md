# Allow and verify

`sbx policy allow network <host>` adds a global allow rule. New connections to that host pass the proxy ([local policy](https://docs.docker.com/ai/sandboxes/governance/local/)):

```bash terminal-id=host
sbx policy allow network www.dockerfrontend.com
```

Expected: `Rule added to policy local (scope: global): … (www.dockerfrontend.com)`

In the **Sandbox** terminal, ask Cursor to curl again (or click Run):

```bash terminal-id=sandbox
curl https://www.dockerfrontend.com again and show me the response. Confirm the request is allowed now.
```

Expected: **Confirmed allowed. Status is HTTP 200 (not 403).** with response headers showing **HTTP/1.0 200 Connection established**.

The policy log should show **allow** for the same host.
