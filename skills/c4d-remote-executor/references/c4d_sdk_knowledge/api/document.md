# Document 操作

> 来源：`c4d.documents` 模块 / `c4d.documents.BaseDocument`
> 文档：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/

## c4d.documents.GetActiveDocument()

- **用途**：获取当前活动文档
- **写法**：`doc = c4d.documents.GetActiveDocument()`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/index.html#c4d.documents.GetActiveDocument
- **注意**：脚本环境中也可直接用内置变量 `doc`

## doc.StartUndo() / doc.EndUndo()

- **用途**：开始/结束 Undo 事务
- **写法**：
```python
doc.StartUndo()
# ... 操作 ...
doc.EndUndo()
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/BaseDocument/index.html#BaseDocument.StartUndo
- **注意**：必须成对调用；EndUndo 前必须有 AddUndo

## doc.AddUndo(type, data)

- **用途**：为对象添加撤销记录
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/BaseDocument/index.html#BaseDocument.AddUndo
- **时序**：
  - 修改已有对象：**先** AddUndo **再** 修改
  - 新建对象：**先** InsertObject **再** AddUndo
  - 删除对象：**先** AddUndo **再** Remove
- **常用类型**：
  - `c4d.UNDOTYPE_CHANGE` — 通用修改（修改前调用）
  - `c4d.UNDOTYPE_NEWOBJ` — 新建对象（Insert后调用）
  - `c4d.UNDOTYPE_DELETEOBJ` — 删除对象（删除前调用）
  - `c4d.UNDOTYPE_CHANGE_SMALL` — 仅 data container（修改前调用）
  - `c4d.UNDOTYPE_HIERARCHY_PSR` — 层级/PSR修改（修改前调用）

## c4d.EventAdd()

- **用途**：通知 C4D 刷新视图和界面
- **写法**：`c4d.EventAdd()`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/index.html#c4d.EventAdd
- **注意**：几乎所有脚本最后都必须调用

## doc.GetFirstObject()

- **用途**：获取场景中第一个顶级对象
- **写法**：`first = doc.GetFirstObject()`
- **返回**：`c4d.BaseObject` 或 `None`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/BaseDocument/index.html#BaseDocument.GetFirstObject

## doc.GetObjects()

- **用途**：返回所有顶级对象（不含子对象）
- **写法**：`top_objects = doc.GetObjects()`
- **返回**：列表
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/BaseDocument/index.html#BaseDocument.GetObjects

## doc.GetActiveObject()

- **用途**：获取当前选中的活动对象（单个）
- **写法**：`obj = doc.GetActiveObject()`
- **返回**：`c4d.BaseObject` 或 `None`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/BaseDocument/index.html#BaseDocument.GetActiveObject

## doc.GetActiveObjects(flags)

- **用途**：获取当前多选对象列表
- **写法**：`objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)`
- **状态**：`c4d.GETACTIVEOBJECTFLAGS_0 == 0`，verified in C4D 2024.5.1
- **注意**：本轮实测多选 3 个对象时返回 `list` 且数量正确；返回顺序为后选对象优先，不要依赖顺序。

## doc.InsertObject(obj, parent, pred, checknames)

- **用途**：将对象插入文档的对象层级
- **写法**：
```python
doc.InsertObject(obj)                    # 插入为顶级
doc.InsertObject(obj, parent)            # 插入为 parent 的子级
doc.InsertObject(obj, parent, pred)      # 插入到 pred 之后
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/BaseDocument/index.html#BaseDocument.InsertObject
- **注意**：插入后要 AddUndo(UNDOTYPE_NEWOBJ) 和 EventAdd

## doc.InsertMaterial(mat)

- **用途**：将材质插入文档的材质列表
- **写法**：`doc.InsertMaterial(mat)`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/BaseDocument/index.html#BaseDocument.InsertMaterial

## doc.GetFirstMaterial()

- **用途**：获取文档中第一个材质
- **写法**：`first_mat = doc.GetFirstMaterial()`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/BaseDocument/index.html#BaseDocument.GetFirstMaterial

## doc.GetMaterials()

- **用途**：获取当前文档所有材质
- **写法**：`materials = doc.GetMaterials()`
- **返回**：`list`
- **状态**：verified in C4D 2024.5.1
- **注意**：本轮实测能返回插入文档的材质；返回顺序不要作为业务逻辑依赖。

## c4d.StopAllThreads()

- **用途**：在修改场景前停止后台线程
- **状态**：API exists in C4D 2024.5.1
- **谨慎结论**：在本 bridge 脚本测试中，创建/删除简单对象不调用 `StopAllThreads()` 未观察到明显问题；涉及建模器、动画刷新、复杂文档操作时仍可保守调用。

## doc.SearchMaterial(name) / doc.SearchObject(name)

- **用途**：按名称搜索材质/对象
- **写法**：
```python
mat = doc.SearchMaterial("MyMaterial")
obj = doc.SearchObject("MyObject")
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.documents/BaseDocument/index.html#BaseDocument.SearchMaterial
- **注意**：名称区分大小写
