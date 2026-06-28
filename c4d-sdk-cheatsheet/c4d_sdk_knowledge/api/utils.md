# Utils 工具函数

> 来源：`c4d.utils`
> 文档：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.utils/

## c4d.utils.SendModelingCommand(command, list, mode, bc, doc, flags)

- **用途**：执行建模命令（如挤压、连接等）
- **写法**：
```python
result = c4d.utils.SendModelingCommand(
    command=c4d.MCOMMAND_CURRENTSTATETOOBJECT,
    list=[obj],
    mode=c4d.MODELINGCOMMANDMODE_ALL,
    bc=c4d.BaseContainer(),
    doc=doc
)
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.utils/index.html#c4d.utils.SendModelingCommand
- **注意**：必须在主线程调用；某些命令如 MCOMMAND_JOIN 必须传 doc 参数

## c4d.utils.DegToRad(d) / c4d.utils.RadToDeg(r)

- **用途**：角度/弧度转换
- **写法**：
```python
rad = c4d.utils.DegToRad(45)   # 45度 -> 弧度
deg = c4d.utils.RadToDeg(1.57) # 弧度 -> 度
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.utils/index.html#c4d.utils.DegToRad

## c4d.utils.GetBBox(pObj, mg)

- **用途**：计算层级的 Bounding Box
- **写法**：
```python
center, radius = c4d.utils.GetBBox(obj, obj.GetMg())
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.utils/index.html#c4d.utils.GetBBox
- **返回**：(center: Vector, radius: Vector) 元组

## c4d.utils.MatrixRotX / MatrixRotY / MatrixRotZ

- **用途**：创建绕 X/Y/Z 轴的旋转矩阵
- **写法**：
```python
m = c4d.utils.MatrixRotX(c4d.utils.DegToRad(45))
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.utils/index.html#c4d.utils.MatrixRotX

## c4d.utils.HPBToMatrix(hpb)

- **用途**：从 HPB 旋转角构造矩阵
- **写法**：
```python
import math
m = c4d.utils.HPBToMatrix(c4d.Vector(math.radians(45), 0, 0))
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.utils/index.html#c4d.utils.HPBToMatrix

## c4d.utils.MatrixToHPB(m)

- **用途**：从矩阵提取 HPB 旋转角
- **写法**：`hpb = c4d.utils.MatrixToHPB(m)`
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.utils/index.html#c4d.utils.MatrixToHPB
