# Undo + EventAdd 标准模板

## 适用场景

所有需要修改场景的脚本的标准写法

## 依赖 API

- `doc.StartUndo()` / `doc.EndUndo()`
- `doc.AddUndo(type, obj)`
- `c4d.EventAdd()`

## 最小脚本

```python
import c4d

def main():
    doc = c4d.documents.GetActiveDocument()

    # 1. 开始 Undo 事务
    doc.StartUndo()

    # 2. 创建对象
    obj = c4d.BaseObject(c4d.Ocube)
    obj.SetName("NewCube")
    obj.SetRelPos(c4d.Vector(0, 100, 0))

    # 3. 插入文档
    doc.InsertObject(obj)

    # 4. 为新建对象添加 Undo（新建对象在 Insert 之后调用）
    doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, obj)

    # 5. 结束 Undo 事务
    doc.EndUndo()

    # 6. 刷新视图（必须！）
    c4d.EventAdd()

main()
```

## 注意事项

- 修改已有对象：**先** AddUndo(UNDOTYPE_CHANGE) **再** 修改
- 新建对象：**先** InsertObject **再** AddUndo(UNDOTYPE_NEWOBJ)
- 删除对象：**先** AddUndo(UNDOTYPE_DELETEOBJ) **再** Remove
- 结尾必须 `c4d.EventAdd()`
