# Current Status

## Done

- Split the original large SDK notes into indexed topic files:
  - `api/*.md`
  - `recipes/*.md`
  - `index.json`
  - `pending_verify.md`
- Ran the first C4D 2024.5.1 bridge verification round.
- Moved verified high-priority APIs out of `pending_verify.md`.
- Added reusable verification scripts in `verify_scripts/`.
- Verified `recipes/replace_bitmap_shader_path.md` for direct Bitmap Shader traversal and filename replacement.
- Updated the `c4d-remote-executor` skill workflow so agents use this cheatsheet before official web docs.

## Current Assumptions

- Target runtime is Cinema 4D 2024.5.1 on Windows.
- Bridge command is:

```powershell
py -3.12 client/send_to_c4d.py <script.py>
```

- Bridge scripts must call `main()` at top level because the bridge executes code with `exec(code, globals_dict)`.
- Normal agent usage should start from `index.json` and read only selected topic files.

## Not Done Yet

- Complex `c4d.StopAllThreads()` behavior has not been tested in heavy scenes, animation refresh, or modeling-command workflows.
- Recursive traversal of nested shader trees has not been verified.
- More object, deformer, generator, camera, light, render-setting, and file import/export APIs remain outside the cheatsheet.
- No automated CI exists for validating Markdown links or JSON schema beyond manual checks.

## Suggested Next Round

1. Add focused verification for nested shader trees.
2. Add focused verification for cameras, lights, and render settings.
3. Add focused verification for file import/export recipes.
4. Add a tiny local validation script for `index.json` and stale pending markers.
5. Revisit document granularity only when a file grows past roughly 150-200 lines or agents start loading too much unrelated context.
