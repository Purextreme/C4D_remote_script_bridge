---
name: c4d-remote-executor
description: Operate a running Cinema 4D instance through the local C4D Python Remote Executor bridge. Use the bundled C4D SDK cheatsheet first, verify uncertain APIs inside C4D, and consult official Maxon SDK docs only when local knowledge and tests are insufficient.
---

# C4D Remote Executor

## Overview

Use the local bridge project to send Python scripts from Codex to a running Cinema 4D process. The bridge listens on `127.0.0.1:4567` and executes scripts inside C4D with `exec(code, globals_dict)`.

## Default Context

- Project path: `D:\YANQ\AI_Explorer\C4D_remote_script_bridge`
- Client command: `py -3.12 client/send_to_c4d.py <script.py>`
- C4D plugin file: `c4d_plugin/remote_executor.pyp`
- Installed plugin path normally used on this machine: `C:\Users\6730\AppData\Roaming\Maxon\Maxon Cinema 4D 2024_A5DBFF93\plugins\remote_executor\remote_executor.pyp`
- SDK cheatsheet: `c4d-sdk-cheatsheet\c4d_sdk_knowledge`

## Knowledge Lookup Policy

Before writing a C4D script, use the local cheatsheet as the first source of API truth.

1. Read `c4d-sdk-cheatsheet\c4d_sdk_knowledge\index.json`.
2. Map the task keywords to the smallest relevant set of `api/*.md` and `recipes/*.md` files.
3. Read only those selected files, plus `pending_verify.md` only when the API is uncertain or flagged.
4. Prefer entries marked `verified in C4D 2024.5.1`.
5. Do not read the whole cheatsheet unless the user explicitly asks for a broad audit.
6. Do not invent C4D API names. If the cheatsheet does not cover an API, write a focused probe script or consult official Maxon docs.
7. Use web lookup only after the local cheatsheet and focused C4D tests are insufficient. Restrict SDK lookup to official Maxon sources under `https://developers.maxon.net/docs/py/` and official examples when possible.

## Script Execution Caveat

The bridge executes submitted files with `exec(code, globals_dict)`, so do not rely on `if __name__ == "__main__"` to run task logic. Define helper functions if useful, but call the entry point at top level, for example `main()`. An `OK` response proves the submitted code executed without raising; it does not prove a guarded `main()` body ran.

## Workflow

1. Assume Cinema 4D must already be open and the `remote_executor.pyp` plugin loaded.
2. Use the cheatsheet lookup policy above to gather only the needed API/recipe context.
3. Create or edit a task-specific script under the project `scripts/` directory.
4. Keep scripts small, focused, and repeatable.
5. Use Undo support for scene modifications:

```python
doc.StartUndo()
try:
    doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, obj)
    obj.Remove()
finally:
    doc.EndUndo()
c4d.EventAdd()
```

6. Run a syntax check for scripts that can compile outside C4D:

```powershell
py -3.12 -m py_compile scripts\your_script.py
```

7. Send the script to C4D:

```powershell
py -3.12 client/send_to_c4d.py scripts\your_script.py
```

8. Treat `OK` as successful bridge execution. If the client prints `ERROR` with traceback, fix the C4D Python script and send it again.
9. For version-sensitive behavior, run:

```powershell
py -3.12 client/send_to_c4d.py scripts\probe_c4d_version.py
```

Use the returned `sdk_docs_hint` only when official SDK lookup is warranted.
10. Delete only temporary cache files created by checks, such as `__pycache__`.

## Verification Rules

- If an API is listed in `pending_verify.md`, write a small verification script before using it in production-style scene scripts.
- Verification scripts should live near the knowledge base when they are reusable: `c4d-sdk-cheatsheet\c4d_sdk_knowledge\verify_scripts`.
- Print clear results, catch exceptions, and clean up temporary scene data when practical.
- When a verification succeeds, update the relevant `api/*.md` or `recipes/*.md`, shorten `pending_verify.md`, and note the result in `verify_report.md` or `CURRENT_STATUS.md`.

## Existing Useful Scripts

- `scripts/test_create_cube.py`: create a cube named `Remote_Test_Cube`.
- `scripts/create_remote_demo_scene.py`: create a small demo scene with primitives, materials, light, and camera.
- `scripts/delete_selected_objects.py`: delete currently selected objects with undo support.
- `scripts/probe_c4d_version.py`: return C4D version metadata and a first-choice official SDK docs URL.
- `scripts/create_verified_cheatsheet_demo.py`: create a small demo using verified object, material, tag, layer, and hierarchy APIs.

## Guardrails

- The bridge is local-only. Do not suggest exposing it to a network unless the user explicitly requests a security review and accepts the risk.
- Avoid long-running scripts unless the user expects C4D to be busy.
- For destructive actions, make the operation narrow and use undo when practical.
- If connection fails, ask whether Cinema 4D is open and whether the plugin console shows `C4D Remote Executor listening on 127.0.0.1:4567`.
