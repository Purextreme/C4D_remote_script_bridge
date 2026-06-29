# 创建材质并赋给对象

## 适用场景

创建新材质并通过 TextureTag 赋给对象

## 依赖 API

- `c4d.BaseMaterial(c4d.Mmaterial)` — verified in C4D 2024.5.1
- `doc.InsertMaterial(mat)`
- `c4d.BaseTag(c4d.Ttexture)` — verified in C4D 2024.5.1
- `tag.SetMaterial(mat)`
- `obj.InsertTag(tag)`

## 最小脚本

```python
import c4d

def main():
    doc = c4d.documents.GetActiveDocument()
    obj = doc.GetActiveObject()
    if obj is None:
        return

    doc.StartUndo()

    mat = c4d.BaseMaterial(c4d.Mmaterial)
    mat.SetName("MyMaterial")
    doc.InsertMaterial(mat)
    doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, mat)

    tag = c4d.BaseTag(c4d.Ttexture)
    tag.SetMaterial(mat)
    obj.InsertTag(tag)
    doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, tag)

    doc.EndUndo()
    c4d.EventAdd()

main()
```

## 注意事项

- `c4d.Mmaterial == 5703`，`c4d.Ttexture == 5616`，verified in C4D 2024.5.1
- 材质和 Tag 都是新建对象，AddUndo 在 Insert 之后调用
