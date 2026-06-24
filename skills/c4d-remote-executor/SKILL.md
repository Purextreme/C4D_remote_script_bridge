---
name: c4d-remote-executor
description: Operate a running Cinema 4D instance through the local C4D Python Remote Executor bridge. Use when the user asks Codex to directly create, delete, select, modify, inspect, or script Cinema 4D scene objects, materials, cameras, lights, or other C4D Python operations from a Codex session.
---

# C4D Remote Executor

## Overview

Use the local bridge project to send Python scripts from Codex to a running Cinema 4D process. The bridge listens on `127.0.0.1:4567` and executes scripts inside C4D with `exec(code, globals_dict)`.

## Default Context

- Project path: `D:\YANQ\AI_Explorer\C4D_remote_script_bridge`
- Client command: `py -3.12 client/send_to_c4d.py <script.py>`
- C4D plugin file: `c4d_plugin/remote_executor.pyp`
- Installed plugin path normally used on this machine: `C:\Users\6730\AppData\Roaming\Maxon\Maxon Cinema 4D 2024_A5DBFF93\plugins\remote_executor\remote_executor.pyp`

## Workflow

1. Assume Cinema 4D must already be open and the `remote_executor.pyp` plugin loaded.
2. Create or edit a task-specific script under the project `scripts/` directory.
3. Keep the script small and focused on the requested C4D operation.
4. Prefer C4D undo support for destructive operations:

```python
doc.StartUndo()
try:
    doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, obj)
    obj.Remove()
finally:
    doc.EndUndo()
c4d.EventAdd()
```

5. Run a syntax check for scripts that can compile outside C4D:

```powershell
py -3.12 -m py_compile scripts\your_script.py
```

6. Send the script to C4D:

```powershell
py -3.12 client/send_to_c4d.py scripts\your_script.py
```

7. Treat `OK` as successful bridge execution. If the client prints `ERROR` with traceback, fix the C4D Python script and send it again.
8. Delete only temporary cache files created by checks, such as `__pycache__`.

## Existing Useful Scripts

- `scripts/test_create_cube.py`: create a cube named `Remote_Test_Cube`.
- `scripts/create_remote_demo_scene.py`: create a small demo scene with primitives, materials, light, and camera.
- `scripts/delete_selected_objects.py`: delete currently selected objects with undo support.

## Guardrails

- The bridge is local-only. Do not suggest exposing it to a network unless the user explicitly requests a security review and accepts the risk.
- Avoid long-running scripts unless the user expects C4D to be busy.
- For destructive actions, make the operation narrow and use undo when practical.
- If connection fails, ask the user whether Cinema 4D is open and whether the plugin console shows `C4D Remote Executor listening on 127.0.0.1:4567`.
