# Pending Verification — 未验证 API 隔离区

以下内容在本轮 C4D 2024.5.1 bridge 实测后仍不应写成绝对结论。

---

## 1. StopAllThreads 是否在所有脚本中必需

- **API**：`c4d.StopAllThreads()`
- **本轮结果**：API 存在；简单创建/删除对象脚本在调用和不调用时都成功。
- **状态**：行为结论仍需复杂场景人工验证。
- **谨慎表述**：在本 bridge 脚本测试中，未观察到不调用 `StopAllThreads()` 导致的问题；但涉及建模器、动画刷新、复杂文档操作时仍可保守调用。

**已执行脚本**：`verify_scripts/verify_stop_all_threads.py`

---

## 本轮已移出 pending 的项目

以下项目已通过 C4D 2024.5.1 实测，并同步到对应 `api/` 或 `recipes/` 文档：

- `c4d.Oplane`
- `c4d.Osphere`
- `c4d.Ocube`
- `c4d.Ocylinder`
- `c4d.Otorus`
- `c4d.Onull`
- `c4d.Mmaterial`
- `c4d.Ttexture`
- `c4d.Tphong`
- `c4d.GETACTIVEOBJECTFLAGS_0`
- `doc.GetMaterials()`
- `obj.SetLayerObject(layer)`
- `c4d.Xbitmap`
- `c4d.BITMAPSHADER_FILENAME`
- `mat.GetFirstShader()` / `shader.GetNext()`
- `recipes/replace_bitmap_shader_path.md`
