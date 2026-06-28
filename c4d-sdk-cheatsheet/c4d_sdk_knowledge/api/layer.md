# Layer 操作

> 来源：`c4d.documents.LayerObject` / `c4d.documents.BaseDocument`
> 文档：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/LayerObject/index.html

## doc.GetLayerObjectRoot()

- **用途**：获取文档层列表的根
- **写法**：
```python
layer_root = doc.GetLayerObjectRoot()
first_layer = layer_root.GetDown()  # 获取第一个层
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/BaseDocument/index.html#BaseDocument.GetLayerObjectRoot
- **注意**：层的遍历使用 `GetDown()` / `GetNext()`

## LayerObject

- **用途**：代表一个层
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/LayerObject/index.html
- **常用方法**：层对象继承自 BaseList2D，有 `GetName()` / `SetName()` 等方法

## 设置对象的层

- **API**：`obj.SetLayerObject(layer)`
- **状态**：verified in C4D 2024.5.1
- **写法**：
```python
root = doc.GetLayerObjectRoot()
layer = c4d.documents.LayerObject()
layer.SetName("MyLayer")
layer.InsertUnder(root)

doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
obj.SetLayerObject(layer)
```
- **验证点**：`obj.SetLayerObject(layer)` 返回 `True`，`obj.GetLayerObject(doc)` 可读回该层。
