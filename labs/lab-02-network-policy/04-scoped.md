# Sandbox-scoped deny

Deny `www.dockerfrontend.com` for **lab2 only**:

```bash terminal-id=host
sbx policy deny network --sandbox lab2 www.dockerfrontend.com
```

Curl from the sandbox again — it should be blocked even if globally allowed.
