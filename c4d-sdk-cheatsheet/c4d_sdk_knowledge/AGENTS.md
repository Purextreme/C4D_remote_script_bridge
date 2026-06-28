# Agent Rules for C4D SDK Cheatsheet

This knowledge base is a lightweight lookup layer for C4D bridge scripts. It is not a full copy of the Maxon SDK.

## Lookup Flow

1. Start with `index.json`.
2. Use task keywords to pick the smallest relevant set of `api/*.md` and `recipes/*.md` files.
3. Read only those selected files.
4. Read `pending_verify.md` only when the task touches an uncertain API or the selected files refer to it.
5. Read `verify_report.md` or `CURRENT_STATUS.md` only when you need project history or verification status.
6. Do not read the full knowledge base by default.
7. Use official Maxon SDK web pages only after local docs and focused C4D probes are insufficient.

## API Rules

- Use APIs documented in this knowledge base whenever possible.
- Prefer entries marked `verified in C4D 2024.5.1`.
- Do not invent method names, constants, parameter IDs, or resource IDs.
- If an API is still in `pending_verify.md`, write and run a small C4D verification script before using it in an operational script.
- If a parameter ID is unknown, inspect it with C4D (`GetDescription()`, container printout, or a focused probe) before writing a recipe.
- When verification succeeds, move the API out of `pending_verify.md` and into the relevant `api/*.md` or `recipes/*.md`.
- When behavior remains uncertain, keep it in `pending_verify.md` with the observed reason.

## Bridge Script Structure

The remote bridge executes files with `exec(code, globals_dict)`. Do not rely on `if __name__ == "__main__"` as the only entry point.

Use this shape:

```python
import traceback

import c4d


def main():
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    try:
        # Scene changes here.
        pass
    except Exception:
        print(traceback.format_exc())
        raise
    finally:
        doc.EndUndo()
        c4d.EventAdd()


main()
```

For read-only probes, `StartUndo()` is not required.

## Undo Timing

- Modify existing object/material/tag: call `doc.AddUndo(c4d.UNDOTYPE_CHANGE, node)` before modification.
- Create object/material/tag: insert it first, then call `doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, node)`.
- Delete object/material/tag: call `doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, node)` before `Remove()`.
- Hierarchy or PSR changes: use `c4d.UNDOTYPE_HIERARCHY_PSR` or the narrower documented type when known.

## Verification Scripts

- Put reusable verification scripts in `verify_scripts/`.
- Keep each script small and focused on one topic.
- Print `hasattr`, constant values, return types, and readback results where useful.
- Catch and print exception type/message or traceback.
- Prefer temporary names with a clear prefix and clean them up.
- Keep scripts repeatable.

## Common Hallucination Checks

| Wrong | Use |
|-------|-----|
| `obj.SetPosition()` | `obj.SetRelPos(c4d.Vector(...))` |
| `doc.GetAllObjects()` | `doc.GetObjects()` or hierarchy traversal |
| `c4d.CreateCube()` | `c4d.BaseObject(c4d.Ocube)` |
| `c4d.O_CUBE` | `c4d.Ocube` |
| `c4d.NULL_OBJECT` | `c4d.Onull` |

## Output Expectations

- Keep operational scripts suitable for `py -3.12 client/send_to_c4d.py <script.py>`.
- Call `main()` at top level.
- Keep generated scripts and documentation short enough for targeted lookup.
