# Get the playground

Repo: [github.com/kristiyan-velkov/docker-sandbox-workshop](https://github.com/kristiyan-velkov/docker-sandbox-workshop)

Labs 4–6 use **workshop-app** from that repo. It is not vendored in this lab repo.

Clone the playground:

```bash terminal-id=host
git clone https://github.com/kristiyan-velkov/docker-sandbox-workshop.git
```

Enter the Next.js app and install dependencies:

```bash terminal-id=host
cd docker-sandbox-workshop/workshop-app
```

```bash terminal-id=host
npm install
```

## Run the app locally

Start the Next.js dev server on the host before you touch sandboxes — confirms dependencies installed and the site loads:

```bash terminal-id=host
npm run dev
```

Open **http://localhost:3000** from the dev server output. You should see the workshop home page. Stop the server with **Ctrl+C** in the terminal, then return to the monorepo root for the `sbx` commands in the next sections:

```bash terminal-id=host
cd ..
```
