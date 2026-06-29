# 创建 Null 并插入文档

## 适用场景

创建一个 Null 对象并插入场景

## 依赖 API

- `c4d.BaseObject(c4d.Onull)`
- `doc.InsertObject()`
- `doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, obj)`

## 最小脚本

```python
import c4d

def main():
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()

    null = c4d.BaseObject(c4d.Onull)
    null.SetName("MyNull")
    null.SetRelPos(c4d.Vector(0, 100, 0))

    doc.InsertObject(null)
    doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, null)

    doc.EndUndo()
    c4d.EventAdd()

main()
```

## 注意事项

- 新建对象的 AddUndo 在 InsertObject **之后**调用
- 结尾必须 `c4d.EventAdd()`
