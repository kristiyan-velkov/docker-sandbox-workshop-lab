# Store GitHub token

```bash terminal-id=host
echo "gho_simulated_token" | sbx secret set -g github
sbx secret ls
sbx run cursor . --name lab3
```
