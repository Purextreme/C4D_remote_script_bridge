# 获取选中对象

## 适用场景

需要获取用户当前选中的对象进行操作

## 依赖 API

- `c4d.documents.GetActiveDocument()`
- `doc.GetActiveObject()`
- `doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)` — 多选，verified in C4D 2024.5.1

## 最小脚本

```python
import c4d

def main():
    doc = c4d.documents.GetActiveDocument()
    obj = doc.GetActiveObject()
    if obj is None:
        c4d.gui.MessageDialog("请先选择一个对象")
        return
    print(f"选中: {obj.GetName()}")

main()
```

## 注意事项

- `GetActiveObject()` 返回单个活动对象，多选用 `GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)`
- 本轮实测多选返回 `list` 且数量正确；顺序可能是后选对象优先。
