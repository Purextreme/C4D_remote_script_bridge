# Transform 操作

> 来源：`c4d.BaseObject` / `c4d.Vector` / `c4d.Matrix`
> 文档：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/

## 位置

### obj.SetRelPos(v) / obj.GetRelPos()

- **用途**：设置/获取相对位置（相对于父对象）
- **写法**：
```python
obj.SetRelPos(c4d.Vector(100, 0, 0))
pos = obj.GetRelPos()
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.SetRelPos

### obj.SetAbsPos(v) / obj.GetAbsPos()

- **用途**：设置/获取绝对位置（相对于父对象的绝对坐标）
- **写法**：
```python
obj.SetAbsPos(c4d.Vector(0, 100, 0))
pos = obj.GetAbsPos()
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.SetAbsPos

## 缩放

### obj.SetRelScale(v) / obj.GetRelScale()

- **用途**：设置/获取相对缩放
- **写法**：
```python
obj.SetRelScale(c4d.Vector(2, 2, 2))
scale = obj.GetRelScale()
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.SetRelScale

### obj.SetAbsScale(v) / obj.GetAbsScale()

- **用途**：设置/获取绝对缩放
- **写法**：`obj.SetAbsScale(c4d.Vector(1, 1, 1))`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.SetAbsScale

## 旋转

### obj.SetRelRot(v) / obj.GetRelRot()

- **用途**：设置/获取相对 HPB 旋转
- **写法**：
```python
import math
obj.SetRelRot(c4d.Vector(math.radians(45), 0, 0))  # H旋转45度
rot = obj.GetRelRot()
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.SetRelRot
- **注意**：HPB = Heading/Pitch/Bank，单位是**弧度**

### obj.SetAbsRot(v) / obj.GetAbsRot()

- **用途**：设置/获取绝对 HPB 旋转
- **写法**：`obj.SetAbsRot(c4d.Vector(math.radians(90), 0, 0))`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.SetAbsRot

## 矩阵

### obj.SetMg(m) / obj.GetMg()

- **用途**：设置/获取世界矩阵（全局矩阵）
- **写法**：
```python
mg = obj.GetMg()       # 获取世界矩阵
obj.SetMg(new_matrix)  # 设置世界矩阵
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.GetMg
- **注意**：对象必须已插入文档才能使用 GetMg

### obj.SetMl(m) / obj.GetMl()

- **用途**：设置/获取本地矩阵
- **写法**：
```python
ml = obj.GetMl()       # 获取本地矩阵
obj.SetMl(new_matrix)  # 设置本地矩阵
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d/C4DAtom/GeListNode/BaseList2D/BaseObject/index.html#BaseObject.GetMl

### c4d.Vector(x, y, z)

- **用途**：创建 3D 向量
- **写法**：
```python
v = c4d.Vector(100, 0, 0)
v_zero = c4d.Vector(0)   # 零向量 (0,0,0)
v_one = c4d.Vector(1)    # (1,1,1)
```

### c4d.Matrix()

- **用途**：创建 4x4 变换矩阵
- **写法**：
```python
m = c4d.Matrix()               # 单位矩阵
m.off = c4d.Vector(100, 0, 0)  # 设置位移
```
- **注意**：`off` = 位移, `v1` = X轴, `v2` = Y轴, `v3` = Z轴
