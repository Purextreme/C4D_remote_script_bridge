# C4D SDK Cheatsheet Verify Report

## 测试环境

- Cinema 4D：2024.5.1（`c4d.GetC4DVersion() == 2024501`）
- Bridge：`127.0.0.1:4567`
- 执行方式：`py -3.12 client/send_to_c4d.py <script.py>`
- 验证脚本目录：`verify_scripts/`

## 已验证成功的 API

- 基础对象常量：`c4d.Oplane`、`c4d.Osphere`、`c4d.Ocube`、`c4d.Ocylinder`、`c4d.Otorus`、`c4d.Onull`
- 材质 / Tag 常量：`c4d.Mmaterial`、`c4d.Ttexture`、`c4d.Tphong`
- 创建 API：`c4d.BaseObject(type)`、`c4d.BaseMaterial(c4d.Mmaterial)`、`c4d.BaseTag(c4d.Ttexture)`、`c4d.BaseTag(c4d.Tphong)`
- 选择 API：`doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)`，多选数量正确；返回顺序不要依赖。
- 文档材质 API：`doc.GetMaterials()` 存在，返回 `list`，能包含当前文档材质。
- Layer API：`c4d.documents.LayerObject()`、`obj.SetLayerObject(layer)`、`obj.GetLayerObject(doc)`
- Bitmap Shader：`c4d.Xbitmap`、`c4d.BITMAPSHADER_FILENAME`、`c4d.BaseShader(c4d.Xbitmap)`、`mat.InsertShader(shader)`、`mat.GetFirstShader()`、`shader.GetNext()`
- `c4d.StopAllThreads()`：API 存在。

## 验证失败的 API

- 本轮没有发现明确失败的目标 API。

## 行为不确定的 API

- `c4d.StopAllThreads()`：简单创建/删除对象脚本在调用和不调用时都成功；复杂建模器、动画刷新、复杂文档操作下是否必须仍需人工场景验证。
- Bitmap Shader 递归遍历：本轮只验证了材质直接挂载的 Bitmap Shader；嵌套 shader 树需单独测试。

## 已修改的文件

- `pending_verify.md`
- `index.json`
- `api/constants.md`
- `api/object.md`
- `api/document.md`
- `api/material.md`
- `api/tag.md`
- `api/layer.md`
- `recipes/group_under_null.md`
- `recipes/create_material_assign.md`
- `recipes/get_selected_objects.md`
- `recipes/replace_bitmap_shader_path.md`
- `verify_scripts/*.py`

## 仍需人工测试

- 在复杂场景、动画刷新或建模命令前后对比 `c4d.StopAllThreads()` 的必要性。
- 带嵌套 shader 的材质中递归替换 Bitmap Shader 路径。
