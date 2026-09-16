# Live API call

```bash terminal-id=host
sbx exec lab3 -- curl -s -o /dev/null -w "HTTP %{http_code}\n" -H "Authorization: Bearer $GH_TOKEN" https://api.github.com/user
```

Expected: `HTTP 200` — the proxy swaps the sentinel for your real token.
