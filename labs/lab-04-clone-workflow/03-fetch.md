# Fetch and merge

The agent's commits live in the VM clone until you fetch them. `git fetch` pulls refs from the `sandbox-lab4-clone` remote that `sbx` added on the host:

```bash terminal-id=host
git fetch sandbox-lab4-clone
```

Inspect the branch without checking it out:

```bash terminal-id=host
git log sandbox-lab4-clone/feat/lab4-test --oneline -3
```

Confirm host `main` has no clone-mode commits — only the direct-mode hero edit from earlier may show as unstaged:

```bash terminal-id=host
git status
```

Expected: `modified: workshop-app/src/components/home-hero.tsx` from direct mode; no commit from clone mode on host `main`. Merge or cherry-pick when you want the clone branch on the host.
