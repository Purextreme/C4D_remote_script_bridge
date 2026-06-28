# 把多个对象放到 Null 下

## 适用场景

将选中的多个对象分组到一个 Null 对象下

## 依赖 API

- `doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)` — verified in C4D 2024.5.1
- `c4d.BaseObject(c4d.Onull)` — verified in C4D 2024.5.1
- `obj.InsertUnder(parent)`
- `doc.AddUndo(c4d.UNDOTYPE_HIERARCHY_PSR, obj)`

## 最小脚本

```python
import c4d

def main():
    doc = c4d.documents.GetActiveDocument()
    sel = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)
    if not sel:
        return

    doc.StartUndo()

    null = c4d.BaseObject(c4d.Onull)
    null.SetName("Group")
    doc.InsertObject(null)
    doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, null)

    for obj in sel:
        doc.AddUndo(c4d.UNDOTYPE_HIERARCHY_PSR, obj)
        obj.InsertUnder(null)

    doc.EndUndo()
    c4d.EventAdd()

main()
```

## 注意事项

- `GETACTIVEOBJECTFLAGS_0 == 0`，verified in C4D 2024.5.1
- 多选返回数量正常，但返回顺序可能是后选对象优先；不要依赖顺序。
- 层级变更使用 `UNDOTYPE_HIERARCHY_PSR`
