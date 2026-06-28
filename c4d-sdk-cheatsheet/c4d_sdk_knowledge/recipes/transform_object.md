# 设置对象位置/缩放/旋转

## 适用场景

修改对象的 PSR（Position/Scale/Rotation）

## 依赖 API

- `obj.SetRelPos(v)` / `obj.SetRelScale(v)` / `obj.SetRelRot(v)`
- `doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)`

## 最小脚本

```python
import c4d
import math

def main():
    doc = c4d.documents.GetActiveDocument()
    obj = doc.GetActiveObject()
    if obj is None:
        return

    doc.StartUndo()
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

    obj.SetRelPos(c4d.Vector(100, 50, 0))
    obj.SetRelScale(c4d.Vector(2, 2, 2))
    obj.SetRelRot(c4d.Vector(math.radians(45), 0, 0))

    doc.EndUndo()
    c4d.EventAdd()

main()
```

## 注意事项

- 旋转单位是**弧度**，用 `math.radians()` 或 `c4d.utils.DegToRad()` 转换
- HPB = Heading/Pitch/Bank
- 修改前必须 `AddUndo(UNDOTYPE_CHANGE, obj)`
