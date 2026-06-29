# 材质操作

> 来源：`c4d.Material` / `c4d.BaseMaterial`
> 文档：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/

## c4d.BaseMaterial(type)

- **用途**：创建新材质
- **写法**：
```python
mat = c4d.BaseMaterial(c4d.Mmaterial)
mat.SetName("MyMaterial")
doc.InsertMaterial(mat)
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/Material/index.html
- **状态**：`c4d.Mmaterial` / `c4d.BaseMaterial(c4d.Mmaterial)` verified in C4D 2024.5.1

## mat.SetChannelState(channel, state)

- **用途**：启用/禁用材质通道
- **写法**：
```python
mat.SetChannelState(c4d.CHANNEL_COLOR, True)       # 启用颜色通道
mat.SetChannelState(c4d.CHANNEL_LUMINANCE, False)   # 禁用发光通道
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/Material/index.html#Material.SetChannelState
- **通道常量**：
  - `c4d.CHANNEL_COLOR` — 颜色
  - `c4d.CHANNEL_LUMINANCE` — 发光
  - `c4d.CHANNEL_TRANSPARENCY` — 透明
  - `c4d.CHANNEL_REFLECTION` — 反射
  - `c4d.CHANNEL_BUMP` — 凹凸
  - `c4d.CHANNEL_ALPHA` — Alpha
  - `c4d.CHANNEL_NORMAL` — 法线

## mat.GetChannelState(channel)

- **用途**：获取材质通道是否启用
- **写法**：`enabled = mat.GetChannelState(c4d.CHANNEL_COLOR)`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/Material/index.html#Material.GetChannelState

## mat.Update(preview, rttm)

- **用途**：更新材质预览和内部值
- **写法**：`mat.Update(True, True)`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseMaterial/index.html#BaseMaterial.Update
- **注意**：`preview=True` 更新缩略图，`rttm=True` 更新实时纹理贴图

## Bitmap Shader 路径替换

- **关键 API**：
  - `c4d.BaseShader(c4d.Xbitmap)`
  - `mat.InsertShader(shader)`
  - `mat.GetFirstShader()`
  - `shader[c4d.BITMAPSHADER_FILENAME]`
- **状态**：`c4d.Xbitmap == 5833`，`c4d.BITMAPSHADER_FILENAME == 1000`，verified in C4D 2024.5.1
- **注意**：把 shader 挂到材质通道后调用 `mat.Message(c4d.MSG_UPDATE)` 和 `mat.Update(True, True)`。
