# GUI 操作

> 来源：`c4d.gui`
> 文档：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.gui/

## c4d.gui.MessageDialog(text, type)

- **用途**：显示消息对话框
- **写法**：
```python
c4d.gui.MessageDialog("Hello from C4D!")
c4d.gui.MessageDialog("确认操作？", c4d.GEMB_OKCANCEL)
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.gui/index.html#c4d.gui.MessageDialog
- **按钮类型**：`GEMB_OK`, `GEMB_OKCANCEL`, `GEMB_YESNOCANCEL`, `GEMB_YESNO`
- **返回值**：`GEMB_R_V_OK`, `GEMB_R_V_CANCEL`, `GEMB_R_V_YES`, `GEMB_R_V_NO`

## c4d.gui.QuestionDialog(text)

- **用途**：显示 Yes/No 问题对话框
- **写法**：
```python
if c4d.gui.QuestionDialog("确定要继续吗？"):
    pass  # 用户点了 Yes
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.gui/index.html#c4d.gui.QuestionDialog
- **返回值**：`True` = Yes, `False` = No

## c4d.gui.InputDialog(title, preset)

- **用途**：显示输入对话框
- **写法**：
```python
text = c4d.gui.InputDialog("请输入名称", "默认值")
```
- **来源**：https://developers.maxon.net/docs/py/2024_4_0a/modules/c4d.gui/index.html#c4d.gui.InputDialog
