# 对象操作

> 来源：`c4d.BaseObject` / `c4d.GeListNode` / `c4d.BaseList2D`
> 文档：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/

## c4d.BaseObject(type)

- **用途**：创建新对象
- **已确认类型**：
  - `c4d.Onull` — Null 对象，verified in C4D 2024.5.1
  - `c4d.Ocube` — 立方体，verified in C4D 2024.5.1
  - `c4d.Osphere` — 球体，verified in C4D 2024.5.1
  - `c4d.Otorus` — 圆环，verified in C4D 2024.5.1
  - `c4d.Oplane` — 平面，verified in C4D 2024.5.1
  - `c4d.Ocylinder` — 圆柱，verified in C4D 2024.5.1
- **写法**：
```python
null = c4d.BaseObject(c4d.Onull)
cube = c4d.BaseObject(c4d.Ocube)
sphere = c4d.BaseObject(c4d.Osphere)
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.__init__

## obj.SetName(name) / obj.GetName()

- **用途**：设置/获取对象名称
- **写法**：
```python
obj.SetName("MyCube")
name = obj.GetName()
```
- **注意**：继承自 BaseList2D，所有场景元素都有此方法

## obj.GetDown() / obj.GetNext() / obj.GetUp()

- **用途**：遍历对象层级
- **写法**：
```python
child = obj.GetDown()      # 第一个子对象
sibling = obj.GetNext()    # 下一个兄弟对象
parent = obj.GetUp()       # 父对象
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/index.html
- **注意**：返回 `None` 如果没有对应对象

## obj.Remove()

- **用途**：从文档中移除对象
- **写法**：
```python
doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, obj)
obj.Remove()
```
- **注意**：移除前必须 AddUndo；移除后对象内存会被释放

## obj.InsertUnder(parent)

- **用途**：将对象移动到 parent 下作为子对象
- **写法**：
```python
doc.AddUndo(c4d.UNDOTYPE_HIERARCHY_PSR, obj)
obj.InsertUnder(parent)
```

## obj.GetMp()

- **用途**：获取 Bounding Box 中心（本地空间）
- **写法**：`center = obj.GetMp()`
- **返回**：`c4d.Vector`（本地坐标）
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.GetMp

## obj.GetRad()

- **用途**：获取 Bounding Box 半径（x/y/z 尺寸的一半）
- **写法**：`radius = obj.GetRad()`
- **返回**：`c4d.Vector`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.GetRad
- **注意**：比手动遍历多边形快

## obj.SetEditorMode(mode) / obj.GetEditorMode()

- **用途**：设置/获取编辑器显示状态
- **写法**：
```python
obj.SetEditorMode(c4d.MODE_OFF)   # 编辑器隐藏
obj.SetEditorMode(c4d.MODE_ON)    # 编辑器显示
obj.SetEditorMode(c4d.MODE_UNDEF) # 跟随父级
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.SetEditorMode

## obj.SetRenderMode(mode) / obj.GetRenderMode()

- **用途**：设置/获取渲染可见性
- **写法**：
```python
obj.SetRenderMode(c4d.MODE_OFF)   # 渲染不可见
obj.SetRenderMode(c4d.MODE_ON)    # 渲染可见
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.SetRenderMode

## obj.MakeTag(tagtype, pred)

- **用途**：创建并插入 Tag 到对象
- **写法**：`tag = obj.MakeTag(c4d.Ttexture)`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.MakeTag
- **状态**：`c4d.Ttexture` / `c4d.Tphong` verified in C4D 2024.5.1

## obj.GetTag(type, nr) / obj.GetFirstTag() / obj.GetTags()

- **用途**：获取对象上的 Tag
- **写法**：
```python
tex_tag = obj.GetTag(c4d.Ttexture)      # 获取第一个 Texture Tag
first_tag = obj.GetFirstTag()            # 获取第一个 Tag
all_tags = obj.GetTags()                 # 获取所有 Tag
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.GetTag

## obj.InsertTag(tag, pred)

- **用途**：将已创建的 Tag 插入对象
- **写法**：
```python
tag = c4d.BaseTag(c4d.Ttexture)
obj.InsertTag(tag)
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.InsertTag

## obj.KillTag(type, nr)

- **用途**：删除对象上指定类型的 Tag
- **写法**：`obj.KillTag(c4d.Ttexture)`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.KillTag
