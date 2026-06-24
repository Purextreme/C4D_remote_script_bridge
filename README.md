# C4D Python Remote Executor

面向 AI agent 的 Cinema 4D Python 本机桥接工具。目标是让 Codex 这类 agent 可以把脚本直接发送到正在运行的 Cinema 4D 执行，避免用户在 Script Manager 里手动复制粘贴。

它也可以手动从外部命令行运行：

```powershell
python client/send_to_c4d.py scripts/test_create_cube.py
```

然后把脚本内容发送到正在运行的 Cinema 4D，并在 C4D 内部执行。

## 文件结构

```text
c4d_plugin/remote_executor.pyp
client/send_to_c4d.py
scripts/test_create_cube.py
scripts/create_remote_demo_scene.py
scripts/delete_selected_objects.py
skills/c4d-remote-executor/
README.md
```

## Agent 使用方式

推荐给 Codex 安装本仓库内置 skill：

```powershell
Copy-Item -Recurse -Force .\skills\c4d-remote-executor $env:USERPROFILE\.codex\skills\c4d-remote-executor
```

安装后，新会话中可以直接让 agent 使用 `$c4d-remote-executor` 操作 C4D，例如：

```text
用 $c4d-remote-executor 在 C4D 里创建几个对象
```

这个 skill 会告诉 agent：

- 项目默认路径
- client 发送命令
- 插件监听地址 `127.0.0.1:4567`
- 常用脚本位置
- 出错时如何查看 `OK` / traceback

## 安装 C4D 插件

1. 找到 Cinema 4D 的插件目录。
   - 通常可以在 C4D 中打开 `Edit > Preferences > Open Preferences Folder`，然后进入 `plugins` 目录。
2. 在 `plugins` 目录下创建一个文件夹，例如：

```text
remote_executor
```

3. 把 `c4d_plugin/remote_executor.pyp` 复制到该文件夹中。
4. 重启 Cinema 4D。
5. 启动成功后，C4D 控制台会输出：

```text
C4D Remote Executor listening on 127.0.0.1:4567
```

插件只绑定 `127.0.0.1:4567`，用于限制为本机访问。

## 手动运行 client

在本项目根目录打开 PowerShell：

```powershell
python client/send_to_c4d.py scripts/test_create_cube.py
```

成功时终端会打印：

```text
OK
```

C4D 当前场景中会创建一个 Cube，名称为 `Remote_Test_Cube`。

也可以运行 demo 场景脚本：

```powershell
python client/send_to_c4d.py scripts/create_remote_demo_scene.py
```

删除当前选中对象：

```powershell
python client/send_to_c4d.py scripts/delete_selected_objects.py
```

## 运行自定义脚本

把要在 C4D 中执行的 Python 代码保存为 `.py` 文件，然后发送：

```powershell
python client/send_to_c4d.py path\to\your_script.py
```

脚本在 C4D 内部通过：

```python
exec(code, globals_dict)
```

执行。异常会被捕获，并以 traceback 形式返回到 client 终端。

## 范围

当前版本只做最小闭环：

- socket 监听 `127.0.0.1:4567`
- client 读取 `.py` 并发送到 C4D
- C4D 执行代码并返回 `OK` 或 traceback
- 执行前后调用 `c4d.EventAdd()`
- 提供 Codex skill，方便新会话知道如何操作这个桥接工具

暂不包含 MCP、JSON-RPC、GUI、认证、对象查询等复杂能力。

## 换电脑安装

1. 克隆这个仓库。
2. 按上面的步骤安装 `c4d_plugin/remote_executor.pyp` 到 C4D plugins 目录。
3. 把 `skills/c4d-remote-executor` 复制到新机器的 Codex skills 目录。
4. 重启 Cinema 4D，并在新的 Codex 会话中使用 `$c4d-remote-executor`。
