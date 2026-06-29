# Tag / TextureTag 操作

> 来源：`c4d.TextureTag` / `c4d.BaseTag`
> 文档：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/

## c4d.TextureTag()

- **用途**：创建 Texture Tag
- **写法**：
```python
tag = c4d.TextureTag()
tag.SetMaterial(mat)
obj.InsertTag(tag)
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/TextureTag/index.html

## tag.SetMaterial(mat) / tag.GetMaterial()

- **用途**：设置/获取 Texture Tag 关联的材质
- **写法**：
```python
tag.SetMaterial(mat)
current_mat = tag.GetMaterial()
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/TextureTag/index.html#TextureTag.SetMaterial

## tag.SetPos(v) / tag.GetPos()

- **用途**：设置/获取贴图投影位置
- **写法**：`tag.SetPos(c4d.Vector(0, 0, 0))`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/TextureTag/index.html#TextureTag.SetPos

## tag.SetScale(v) / tag.GetScale()

- **用途**：设置/获取贴图投影缩放
- **写法**：`tag.SetScale(c4d.Vector(1, 1, 1))`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/TextureTag/index.html#TextureTag.SetScale

## tag.SetRot(v) / tag.GetRot()

- **用途**：设置/获取贴图投影旋转
- **写法**：`tag.SetRot(c4d.Vector(0, 0, 0))`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseTag/TextureTag/index.html#TextureTag.SetRot

## obj.MakeTag(tagtype)

- **用途**：创建并插入 Tag（便捷方法）
- **写法**：`tag = obj.MakeTag(c4d.Ttexture)`
- **状态**：`c4d.Ttexture` verified in C4D 2024.5.1

## c4d.BaseTag(type)

- **用途**：按类型创建 Tag
- **写法**：
```python
tex_tag = c4d.BaseTag(c4d.Ttexture)
phong_tag = c4d.BaseTag(c4d.Tphong)
```
- **状态**：`c4d.Ttexture` / `c4d.Tphong` verified in C4D 2024.5.1

## obj.GetTag(type) / obj.GetFirstTag() / obj.GetTags()

- **用途**：获取对象上的 Tag
- **写法**：
```python
tex_tag = obj.GetTag(c4d.Ttexture)
first_tag = obj.GetFirstTag()
all_tags = obj.GetTags()
```

## obj.InsertTag(tag)

- **用途**：将已创建的 Tag 插入对象
- **写法**：`obj.InsertTag(tag)`

## obj.KillTag(type)

- **用途**：删除对象上指定类型的 Tag
- **写法**：`obj.KillTag(c4d.Ttexture)`
