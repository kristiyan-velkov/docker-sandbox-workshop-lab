# Step 1 · Copy kit template

Copy the Lab 6 kit template to `my-workshop-kit/` at repo root. Inspect `spec.yaml` and `files/` before editing.

From home, enter the monorepo (clone it in Lab 4 if you have not already):

```bash terminal-id=host
cd docker-sandbox-workshop
```

Copy the template — never edit `lab-06-customize-stack/kit-template/` in place:

```bash terminal-id=host
cp -r lab-06-customize-stack/kit-template ./my-workshop-kit
```

Confirm the layout:

```bash terminal-id=host
ls my-workshop-kit/
```

Expected: `spec.yaml`, `README.md`, and `files/home/` + `files/workspace/`.
