# 隐藏对象或设置渲染不可见

## 适用场景

控制对象在编辑器和渲染中的可见性

## 依赖 API

- `obj.SetEditorMode(c4d.MODE_OFF)`
- `obj.SetRenderMode(c4d.MODE_OFF)`

## 最小脚本

```python
import c4d

def main():
    doc = c4d.documents.GetActiveDocument()
    obj = doc.GetActiveObject()
    if obj is None:
        return

    doc.StartUndo()
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

    obj.SetEditorMode(c4d.MODE_OFF)
    obj.SetRenderMode(c4d.MODE_OFF)

    doc.EndUndo()
    c4d.EventAdd()

main()
```

## 注意事项

- `MODE_ON` = 始终显示，`MODE_OFF` = 始终隐藏，`MODE_UNDEF` = 跟随父级
- 恢复显示用 `MODE_UNDEF`
