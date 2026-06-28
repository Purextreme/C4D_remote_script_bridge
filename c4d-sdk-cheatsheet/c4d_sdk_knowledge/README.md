# C4D SDK Cheatsheet

Lightweight Python SDK knowledge base for the local Cinema 4D remote bridge and Codex agents.

The goal is to reduce API guessing and context bloat. This is not a full SDK mirror; it contains high-frequency APIs, small recipes, verification notes, and unresolved items.

## How Agents Should Use It

1. Read `index.json`.
2. Pick the smallest relevant `api/*.md` and `recipes/*.md` files.
3. Prefer content marked `verified in C4D 2024.5.1`.
4. Check `pending_verify.md` only when the task touches uncertain APIs.
5. Write focused C4D probe scripts before using pending APIs.
6. Use official Maxon SDK docs only when the local cheatsheet and probes are insufficient.

Do not load the whole knowledge base for normal script writing.

## Current Granularity

The current split is intentionally coarse enough to keep related context together:

- `api/*.md`: small topic files such as object, document, material, tag, layer, constants.
- `recipes/*.md`: task-focused snippets.
- `index.json`: keyword to file map.
- `pending_verify.md`: APIs that must not be treated as confirmed.
- `verify_scripts/`: reusable C4D probe scripts.
- `verify_report.md`: detailed result from the latest verification round.
- `CURRENT_STATUS.md`: short project status and next work list.

Do not split further unless a file grows past roughly 150-200 lines, mixes unrelated topics, or causes agents to read too much irrelevant context.

## Verification Status

The first C4D verification round was run in Cinema 4D 2024.5.1 through:

```powershell
py -3.12 client/send_to_c4d.py <script.py>
```

Verified areas include:

- Primitive object constants: `Onull`, `Ocube`, `Oplane`, `Osphere`, `Ocylinder`, `Otorus`
- Material/tag constants: `Mmaterial`, `Ttexture`, `Tphong`
- Selection: `doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)`
- Materials: `doc.GetMaterials()`
- Layers: `LayerObject`, `obj.SetLayerObject(layer)`
- Bitmap shader basics: `Xbitmap`, `BITMAPSHADER_FILENAME`, `mat.GetFirstShader()`

See `verify_report.md` for details.

## Directory Layout

```text
c4d_sdk_knowledge/
  AGENTS.md
  README.md
  CURRENT_STATUS.md
  index.json
  pending_verify.md
  verify_report.md
  api/
  recipes/
  verify_scripts/
```

## Maintenance Rules

- Keep verified API in `api/*.md` or `recipes/*.md`, not in `pending_verify.md`.
- Keep uncertain API in `pending_verify.md` with the reason.
- Add or update a `verify_scripts/*.py` file when behavior must be proven inside C4D.
- Update `index.json` when adding a new topic or important keyword.
- Keep entries short. Link related recipes instead of expanding into tutorials.

## Official Resources

| Resource | URL |
|----------|-----|
| Python SDK docs | https://developers.maxon.net/docs/py/2024_4_0a/ |
| Resource Index | https://developers.maxon.net/docs/py/2024_4_0a/classic_resource/resource_overview.html |
| Symbol Index | https://developers.maxon.net/docs/py/2024_4_0a/types/index.html |
| GitHub examples | https://github.com/Maxon-Computer/Cinema-4D-Python-API-Examples |
