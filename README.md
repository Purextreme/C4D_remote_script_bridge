# C4D Remote Executor Skill

面向 Codex agent 的 Cinema 4D Python 本机桥接 skill。它把运行时 client、C4D 插件资产和 C4D Python SDK 速查表放在同一个 skill 目录中，方便复制到新机器使用。

## 文件结构

```text
skills/c4d-remote-executor/
  SKILL.md
  agents/openai.yaml
  scripts/send_to_c4d.py
  scripts/c4d/
  assets/c4d_plugin/remote_executor.pyp
  references/c4d_sdk_knowledge/
```

## 安装 Skill

在本仓库根目录运行：

```powershell
Copy-Item -Recurse -Force .\skills\c4d-remote-executor $env:USERPROFILE\.codex\skills\c4d-remote-executor
```

新 Codex 会话中可以直接使用：

```text
用 $c4d-remote-executor 在 C4D 里创建几个对象
```

## 安装 C4D 插件

1. 在 C4D 中打开 `Edit > Preferences > Open Preferences Folder`。
2. 进入或创建 `plugins` 目录。
3. 在 `plugins` 中创建 `remote_executor` 文件夹。
4. 复制 `skills/c4d-remote-executor/assets/c4d_plugin/remote_executor.pyp` 到该文件夹。
5. 重启 Cinema 4D。

启动成功后，C4D 控制台会输出：

```text
C4D Remote Executor listening on 127.0.0.1:4567
```

插件只绑定 `127.0.0.1:4567`，用于限制为本机访问。

## 手动运行 Client

在本仓库根目录打开 PowerShell：

```powershell
py -3.12 skills\c4d-remote-executor\scripts\send_to_c4d.py skills\c4d-remote-executor\scripts\c4d\test_create_cube.py
```

成功时终端会打印：

```text
OK
```

C4D 当前场景中会创建一个 Cube，名称为 `Remote_Test_Cube`。

运行版本探针：

```powershell
py -3.12 skills\c4d-remote-executor\scripts\send_to_c4d.py skills\c4d-remote-executor\scripts\c4d\probe_c4d_version.py
```

发送自定义脚本：

```powershell
py -3.12 skills\c4d-remote-executor\scripts\send_to_c4d.py path\to\your_script.py
```

## 速查表使用原则

SDK 速查表位于 `skills/c4d-remote-executor/references/c4d_sdk_knowledge/`。

Agent 正常写 C4D 脚本时应先读 `index.json`，再按需读取最小相关的 `api/*.md` 或 `recipes/*.md`。只有遇到未验证 API 时才读 `pending_verify.md`，本地速查表和 C4D 实测都不足时再查官方 Maxon SDK。

## 当前状态

- 已完成第一轮 C4D 2024.5.1 实测验证。
- 已验证常用对象、材质、tag、选中对象、文档材质、layer、bitmap shader 路径替换等高频 API。
- 仍需谨慎对待 `StopAllThreads()` 在复杂建模器、动画刷新、大型文档操作中的必要性。
- 后续优化重点是继续补充小型 verified recipes，而不是扩大成完整 SDK 镜像。
