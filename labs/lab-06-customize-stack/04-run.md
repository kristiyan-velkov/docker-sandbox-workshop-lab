# Step 4 · Run your kit

Launch Cursor on `workshop-app/` with your custom kit. Wait for `npm ci` and the background dev server.

From the monorepo root, copy the env file the bootstrap script expects:

```bash terminal-id=host
cp workshop-app/.env.sandbox.example workshop-app/.env.local
```

Enter the app directory and start Cursor with your kit:

```bash terminal-id=host
cd workshop-app
```

```bash terminal-id=host
sbx run cursor . --kit ../my-workshop-kit --name lab6-my-kit
```

First run may take about a minute while the kit startup script runs `npm ci` and starts Next.js on port 3000 inside the VM.
