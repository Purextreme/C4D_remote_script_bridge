---
name: c4d-remote-executor
description: Operate a running Cinema 4D instance through the local C4D Python Remote Executor skill. Use when Codex needs to create, inspect, modify, organize, or validate Cinema 4D scene content by sending Python scripts to C4D; use the bundled C4D SDK cheatsheet first, verify uncertain APIs inside C4D, and consult official Maxon SDK docs only when local knowledge and focused probes are insufficient.
---

# C4D Remote Executor

## Overview

Use this self-contained skill to send Python scripts from Codex to a running Cinema 4D process. The C4D plugin listens on `127.0.0.1:4567`, and the client script sends a `.py` file to C4D for execution with `exec(code, globals_dict)`.

## Skill Resources

- Client: `scripts/send_to_c4d.py`
- C4D plugin asset: `assets/c4d_plugin/remote_executor.pyp`
- Reusable C4D scripts: `scripts/c4d/`
- SDK cheatsheet: `references/c4d_sdk_knowledge/`
- SDK index: `references/c4d_sdk_knowledge/index.json`

When running from this repository, use paths relative to the repository root. When this skill has been copied to a Codex skills directory, use paths relative to the copied `c4d-remote-executor` skill folder.

## Knowledge Lookup Policy

Before writing a C4D script, use the bundled cheatsheet as the first source of API truth.

1. Read `references/c4d_sdk_knowledge/index.json`.
2. Map the task keywords to the smallest relevant set of `api/*.md` and `recipes/*.md` files.
3. Read only those selected files.
4. Read `pending_verify.md` only when the task touches uncertain or flagged APIs.
5. Prefer entries marked `verified in C4D 2024.5.1`.
6. Do not read the whole cheatsheet unless the user explicitly asks for a broad audit.
7. Do not invent C4D API names. If the cheatsheet does not cover an API, write a focused probe script or consult official Maxon docs.
8. Use web lookup only after the local cheatsheet and focused C4D tests are insufficient. Restrict SDK lookup to official Maxon sources under `https://developers.maxon.net/docs/py/` and official examples when possible.

## Script Execution Caveat

The bridge executes submitted files with `exec(code, globals_dict)`, so do not rely on `if __name__ == "__main__"` to run task logic. Define helper functions if useful, but call the entry point at top level, for example `main()`. An `OK` response proves the submitted code executed without raising; it does not prove a guarded `main()` body ran.

## Workflow

1. Assume Cinema 4D must already be open and `remote_executor.pyp` must be installed and loaded.
2. Use the cheatsheet lookup policy above to gather only the needed API/recipe context.
3. Create or edit a task-specific script in a suitable workspace path.
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
py -3.12 -m py_compile path\to\your_script.py
```

7. Send the script to C4D from the repository root:

```powershell
py -3.12 skills\c4d-remote-executor\scripts\send_to_c4d.py path\to\your_script.py
```

8. If working directly inside the installed skill folder, send scripts with:

```powershell
py -3.12 scripts\send_to_c4d.py path\to\your_script.py
```

9. Treat `OK` as successful bridge execution. If the client prints `ERROR` with traceback, fix the C4D Python script and send it again.
10. For version-sensitive behavior, run the bundled probe:

```powershell
py -3.12 skills\c4d-remote-executor\scripts\send_to_c4d.py skills\c4d-remote-executor\scripts\c4d\probe_c4d_version.py
```

Use the returned `sdk_docs_hint` only when official SDK lookup is warranted.

## Verification Rules

- If an API is listed in `pending_verify.md`, write a small verification script before using it in production-style scene scripts.
- Reusable verification scripts belong in `references/c4d_sdk_knowledge/verify_scripts`.
- Print clear results, catch exceptions, and clean up temporary scene data when practical.
- When verification succeeds, move the result into the relevant `api/*.md` or `recipes/*.md`, shorten `pending_verify.md`, and update `index.json` only when keywords or file routes change.

## Useful Bundled Scripts

- `scripts/c4d/test_create_cube.py`: create a cube named `Remote_Test_Cube`.
- `scripts/c4d/create_remote_demo_scene.py`: create a small demo scene with primitives, materials, light, and camera.
- `scripts/c4d/delete_selected_objects.py`: delete currently selected objects with undo support.
- `scripts/c4d/probe_c4d_version.py`: return C4D version metadata and a first-choice official SDK docs URL.
- `scripts/c4d/create_verified_cheatsheet_demo.py`: create a small demo using verified object, material, tag, layer, and hierarchy APIs.

## Guardrails

- The bridge is local-only. Do not suggest exposing it to a network unless the user explicitly requests a security review and accepts the risk.
- Avoid long-running scripts unless the user expects C4D to be busy.
- For destructive actions, make the operation narrow and use undo when practical.
- If connection fails, ask whether Cinema 4D is open and whether the plugin console shows `C4D Remote Executor listening on 127.0.0.1:4567`.
