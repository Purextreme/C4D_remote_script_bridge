---
name: c4d-remote-executor
description: Operate a running Cinema 4D instance through the local C4D Python Remote Executor bridge, with optional version-aware checks against official Maxon Python SDK documentation for complex or unresolved API issues. Use when the user asks Codex to directly create, delete, select, modify, inspect, or script Cinema 4D scene objects, materials, cameras, lights, SDK API calls, or other C4D Python operations from a Codex session.
---

# C4D Remote Executor

## Overview

Use the local bridge project to send Python scripts from Codex to a running Cinema 4D process. The bridge listens on `127.0.0.1:4567` and executes scripts inside C4D with `exec(code, globals_dict)`.

## Script Execution Caveat

The bridge executes submitted files with `exec(code, globals_dict)`, so do not rely on `if __name__ == "__main__"` to run task logic. Define helper functions if useful, but call the entry point at top level, for example `main()`, so the operation actually runs inside C4D. Apply the same rule to verification scripts; an `OK` response only proves the submitted code executed without raising, not that a guarded `main()` body ran.

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
8. For simple, common operations, do not search the SDK docs. When a task uses complex or version-sensitive API behavior, or when an `ERROR` traceback remains unclear after one local fix attempt, run the version probe:

```powershell
py -3.12 client/send_to_c4d.py scripts\probe_c4d_version.py
```

Use the returned `sdk_docs_hint` as the first official Maxon Python SDK documentation target only when SDK lookup is warranted. For Cinema 4D 2024.x, prefer `https://developers.maxon.net/docs/py/2024_4_0a/index.html` unless a closer official docs page is found. Restrict SDK lookup to official Maxon documentation under `https://developers.maxon.net/docs/py/` and official Maxon examples when possible. If network access is unavailable, state that SDK lookup was not verified online.
9. Delete only temporary cache files created by checks, such as `__pycache__`.

## Existing Useful Scripts

- `scripts/test_create_cube.py`: create a cube named `Remote_Test_Cube`.
- `scripts/create_remote_demo_scene.py`: create a small demo scene with primitives, materials, light, and camera.
- `scripts/delete_selected_objects.py`: delete currently selected objects with undo support.
- `scripts/probe_c4d_version.py`: return C4D version metadata and a first-choice official SDK docs URL.

## Guardrails

- The bridge is local-only. Do not suggest exposing it to a network unless the user explicitly requests a security review and accepts the risk.
- Avoid long-running scripts unless the user expects C4D to be busy.
- For destructive actions, make the operation narrow and use undo when practical.
- If connection fails, ask the user whether Cinema 4D is open and whether the plugin console shows `C4D Remote Executor listening on 127.0.0.1:4567`.
