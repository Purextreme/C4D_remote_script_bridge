# 替换 Bitmap Shader 图片路径

## 适用场景

修改材质中 Bitmap Shader 的纹理文件路径

## 依赖 API

- `c4d.BaseShader(c4d.Xbitmap)` — verified in C4D 2024.5.1
- `mat.InsertShader(shader)` — verified in C4D 2024.5.1
- `mat.GetFirstShader()` / `shader.GetNext()` — verified in C4D 2024.5.1
- `shader[c4d.BITMAPSHADER_FILENAME]` — verified in C4D 2024.5.1

## 最小脚本

**状态：verified in C4D 2024.5.1**

```python
import c4d

def iter_bitmap_shaders(mat):
    shd = mat.GetFirstShader()
    while shd:
        if shd.GetType() == c4d.Xbitmap:
            yield shd
        shd = shd.GetNext()

def main():
    doc = c4d.documents.GetActiveDocument()
    mat = doc.GetFirstMaterial()
    new_path = r"D:\textures\replacement.png"

    if mat is None:
        return

    doc.StartUndo()
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, mat)

    for shader in iter_bitmap_shaders(mat):
        shader[c4d.BITMAPSHADER_FILENAME] = new_path
        shader.Message(c4d.MSG_UPDATE)

    mat.Message(c4d.MSG_UPDATE)
    mat.Update(True, True)
    doc.EndUndo()
    c4d.EventAdd()

main()
```

## 注意事项

- `c4d.Xbitmap == 5833`
- `c4d.BITMAPSHADER_FILENAME == 1000`
- 本 recipe 只遍历材质直接挂载的 shader；嵌套 shader 树需要单独递归处理。
