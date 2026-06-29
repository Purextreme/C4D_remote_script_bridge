# 文件导入导出

> 来源：`c4d.documents` / `c4d.storage`
> 文档：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/

## c4d.documents.SaveDocument(doc, name, saveflags, format)

- **用途**：保存文档到文件
- **写法**：
```python
c4d.documents.SaveDocument(doc, "C:/temp/test.c4d",
    c4d.SAVEDOCUMENTFLAGS_DIALOGSALLOWED, c4d.FORMAT_C4DEXPORT)
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/index.html#c4d.documents.SaveDocument

## c4d.documents.MergeDocument(doc, name, loadflags, thread)

- **用途**：合并文件到当前文档
- **写法**：
```python
c4d.documents.MergeDocument(doc, "C:/temp/other.c4d",
    c4d.SCENEFILTER_OBJECTS | c4d.SCENEFILTER_MATERIALS, None)
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/index.html#c4d.documents.MergeDocument

## c4d.documents.LoadDocument(name, loadflags, thread)

- **用途**：加载文档（不显示在编辑器中）
- **写法**：
```python
new_doc = c4d.documents.LoadDocument("C:/temp/test.c4d",
    c4d.SCENEFILTER_NONE, None)
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/index.html#c4d.documents.LoadDocument

## c4d.documents.LoadFile(name)

- **用途**：加载文件并在 C4D 中打开
- **写法**：`c4d.documents.LoadFile("C:/temp/test.c4d")`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/index.html#c4d.documents.LoadFile

## c4d.storage.LoadDialog() / c4d.storage.SaveDialog()

- **用途**：打开文件选择对话框
- **写法**：
```python
path = c4d.storage.LoadDialog(c4d.FILESELECTTYPE_SCENES, "选择文件")
path = c4d.storage.SaveDialog(c4d.FILESELECTTYPE_SCENES, "保存文件")
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.storage/index.html#c4d.storage.LoadDialog
