# Denied sites

`network.deniedDomains` blocks Google and LinkedIn even if the balanced preset would allow them. Type this in the Host terminal (or click Run):

```bash terminal-id=host
Search Google for Kristiyan Velkov and fetch LinkedIn profile info. Report what worked and what failed.
```

`sbx policy log` is the audit trail for this sandbox — HOST and DECISION for each request:

```bash terminal-id=host
sbx policy log lab5-kit --limit 15
```

You should see `kristiyanvelkov.com` / `leanpub.com` ALLOWED and `google.com` / `linkedin.com` BLOCKED.
