# 获取对象 Bounding Box

## 适用场景

获取对象的边界盒尺寸和中心

## 依赖 API

- `obj.GetMp()` — 本地空间中心
- `obj.GetRad()` — 本地空间半径
- `c4d.utils.GetBBox(obj, mg)` — 层级 Bounding Box

## 最小脚本

```python
import c4d

def main():
    doc = c4d.documents.GetActiveDocument()
    obj = doc.GetActiveObject()
    if obj is None:
        return

    center = obj.GetMp()
    radius = obj.GetRad()

    print(f"中心: {center}")
    print(f"半径: {radius}")
    print(f"尺寸: {radius * 2}")

main()
```

## 注意事项

- `GetMp()` 和 `GetRad()` 返回本地空间坐标
- `c4d.utils.GetBBox()` 可计算整个层级的 Bounding Box
- 尺寸 = `GetRad() * 2`
