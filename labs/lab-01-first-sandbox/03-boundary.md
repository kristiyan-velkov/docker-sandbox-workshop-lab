# Workspace boundary

The file :filelink[delete-me.txt]{path="delete-me.txt"} lives **outside** the synced workspace.

Ask the agent:

> Try to delete `../delete-me.txt` from this workspace. Report whether it worked and explain why sandbox workspace mounts limit what you can change on the host.

The file should remain — the agent cannot remove paths outside the workspace mount.
