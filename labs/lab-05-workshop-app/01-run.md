# Run with kit

The workspace must be `workshop-app/` (the folder with `package.json`). `--kit` applies the mixin only at **create** time:

```bash terminal-id=host
cd docker-sandbox-workshop/workshop-app
```

```bash terminal-id=host
sbx run cursor . --kit ../customize/kit/workshop-app-nextjs --name lab5-kit
```

Wait about a minute on first run. The kit startup script runs `npm ci` and starts the Next.js dev server on port 3000 inside the VM.
