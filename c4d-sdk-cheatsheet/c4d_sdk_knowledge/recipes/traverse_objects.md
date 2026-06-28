# 遍历场景所有对象

## 适用场景

需要递归遍历场景中所有对象

## 依赖 API

- `doc.GetFirstObject()`
- `obj.GetDown()` / `obj.GetNext()`

## 最小脚本

```python
import c4d

def iterate_objects(op):
    while op:
        print(op.GetName())
        iterate_objects(op.GetDown())
        op = op.GetNext()

def main():
    doc = c4d.documents.GetActiveDocument()
    iterate_objects(doc.GetFirstObject())

main()
```

## 注意事项

- 使用 `GetDown()` 进入子层级，`GetNext()` 遍历同级
- 返回 `None` 表示没有更多对象
