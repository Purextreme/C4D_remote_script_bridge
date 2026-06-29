# 常量速查表

> 来源：Cinema 4D 2024.4 Python SDK
> 参考：https://developers.maxon.net/docs/py/2024_4_0a/types/

## 对象类型

| 常量 | 值 | 说明 | 状态 |
|------|----|------|------|
| `c4d.Onull` | `5140` | Null 对象 | verified in C4D 2024.5.1 |
| `c4d.Ocube` | `5159` | 立方体 | verified in C4D 2024.5.1 |
| `c4d.Osphere` | `5160` | 球体 | verified in C4D 2024.5.1 |
| `c4d.Otorus` | `5163` | 圆环 | verified in C4D 2024.5.1 |
| `c4d.Oplane` | `5168` | 平面 | verified in C4D 2024.5.1 |
| `c4d.Ocylinder` | `5170` | 圆柱 | verified in C4D 2024.5.1 |

完整列表：https://developers.maxon.net/docs/py/2024_4_0a/types/objects.html

## 材质 / Tag 类型

| 常量 | 值 | 说明 | 状态 |
|------|----|------|------|
| `c4d.Mmaterial` | `5703` | 经典材质类型，可用于 `c4d.BaseMaterial()` | verified in C4D 2024.5.1 |
| `c4d.Ttexture` | `5616` | Texture Tag，可用于 `c4d.BaseTag()` / `obj.MakeTag()` | verified in C4D 2024.5.1 |
| `c4d.Tphong` | `5612` | Phong Tag，可用于 `c4d.BaseTag()` / `obj.MakeTag()` | verified in C4D 2024.5.1 |

## 选择 Flags

| 常量 | 值 | 说明 | 状态 |
|------|----|------|------|
| `c4d.GETACTIVEOBJECTFLAGS_0` | `0` | `doc.GetActiveObjects(flags)` 的基础 flags | verified in C4D 2024.5.1 |

## Shader 类型 / 参数 ID

| 常量 | 值 | 说明 | 状态 |
|------|----|------|------|
| `c4d.Xbitmap` | `5833` | Bitmap Shader 类型，可用于 `c4d.BaseShader()` | verified in C4D 2024.5.1 |
| `c4d.BITMAPSHADER_FILENAME` | `1000` | Bitmap Shader 文件路径参数 | verified in C4D 2024.5.1 |

## Undo 类型

| 常量 | 说明 | 调用时机 |
|------|------|----------|
| `c4d.UNDOTYPE_CHANGE` | 通用修改 | 修改前 |
| `c4d.UNDOTYPE_CHANGE_SMALL` | 仅 data container | 修改前 |
| `c4d.UNDOTYPE_NEWOBJ` | 新建对象/Tag/材质 | Insert后 |
| `c4d.UNDOTYPE_DELETEOBJ` | 删除对象 | 删除前 |
| `c4d.UNDOTYPE_HIERARCHY_PSR` | 层级/PSR修改 | 修改前 |

## 显示模式

| 常量 | 说明 |
|------|------|
| `c4d.MODE_ON` | 始终显示 |
| `c4d.MODE_OFF` | 始终隐藏 |
| `c4d.MODE_UNDEF` | 跟随父级 |

## 材质通道

| 常量 | 说明 |
|------|------|
| `c4d.CHANNEL_COLOR` | 颜色 |
| `c4d.CHANNEL_LUMINANCE` | 发光 |
| `c4d.CHANNEL_TRANSPARENCY` | 透明 |
| `c4d.CHANNEL_REFLECTION` | 反射 |
| `c4d.CHANNEL_BUMP` | 凹凸 |
| `c4d.CHANNEL_ALPHA` | Alpha |
| `c4d.CHANNEL_NORMAL` | 法线 |

## 文件格式

| 常量 | 说明 |
|------|------|
| `c4d.FORMAT_C4DEXPORT` | C4D 导出 |
| `c4d.FORMAT_C4DIMPORT` | C4D 导入 |
| `c4d.FORMAT_OBJ2EXPORT` | OBJ 导出 (R17+) |
| `c4d.FORMAT_OBJ2IMPORT` | OBJ 导入 (R17+) |
| `c4d.FORMAT_FBX_EXPORT` | FBX 导出 (S22+) |
| `c4d.FORMAT_FBX_IMPORT` | FBX 导入 (S22+) |
| `c4d.FORMAT_ABCEXPORT` | Alembic 导出 |
| `c4d.FORMAT_ABCIMPORT` | Alembic 导入 |
| `c4d.FORMAT_GLTFEXPORT` | glTF 导出 (S22+) |
| `c4d.FORMAT_STL_EXPORT` | STL 导出 (S22+) |
| `c4d.FORMAT_STL_IMPORT` | STL 导入 (S22+) |

## 场景过滤 Flags

| 常量 | 说明 |
|------|------|
| `c4d.SCENEFILTER_NONE` | 无 |
| `c4d.SCENEFILTER_OBJECTS` | 加载/保存对象 |
| `c4d.SCENEFILTER_MATERIALS` | 加载/保存材质 |
| `c4d.SCENEFILTER_MERGESCENE` | 合并场景标记 |
| `c4d.SCENEFILTER_DIALOGSALLOWED` | 允许对话框 |
