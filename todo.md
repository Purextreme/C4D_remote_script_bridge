请帮我开发一个最小可用的 C4D Python Remote Executor。

目标：
让我可以在外部命令行运行：
python client/send_to_c4d.py scripts/test_create_cube.py

然后把这个 Python 脚本发送给正在运行的 Cinema 4D，并在 C4D 内部执行，避免我手动复制粘贴到 Script Manager。

项目结构：

- c4d_plugin/remote_executor.pyp
- client/send_to_c4d.py
- scripts/test_create_cube.py
- README.md

要求：

1. C4D 插件启动后在 localhost / 127.0.0.1 上监听端口 4567。
2. 只接受本机连接，不允许外网访问。
3. client 读取指定 .py 文件内容，通过 socket 发送给 C4D。
4. C4D 端接收代码后执行 exec(code, globals_dict)。
5. 执行前后需要调用 c4d.EventAdd()。
6. 捕获异常并返回 traceback 给 client。
7. client 在终端打印 C4D 返回结果。
8. 提供一个 test_create_cube.py，用来在场景中创建一个 Cube，命名为 Remote_Test_Cube。
9. README 写清楚如何安装插件、如何运行 client。
10. 先不要实现复杂 MCP、JSON-RPC、GUI、认证、对象查询等功能，只做最小闭环。
