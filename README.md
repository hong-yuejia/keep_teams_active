1. 介绍 keep_teams_active_gui.py
keep_teams_active_gui.py 是一个 Python 脚本，旨在通过模拟鼠标移动和键盘操作，保持 Microsoft Teams 的在线状态（绿色图标）。它解决了之前的问题（“停止后重新开始无法保持在线”），具有以下功能：

GUI 界面：基于 tkinter，提供“开始”和“停止”按钮，状态标签显示操作信息。
保持在线：每 15 秒随机移动鼠标（小幅度，如 ±5 像素）和模拟按键（如 shift），防止 Teams 超时。
线程管理：使用 threading.Event 和 Thread，确保“停止”后重新“开始”仍有效。
鲁棒性：禁用 pyautogui.FAILSAFE，捕获异常，防止手动鼠标移动中断。
日志记录：操作和错误记录到 teams_active.log，便于调试。
跨平台：支持 Windows 和 Mac（Linux 需额外配置）。
代码概述（基于 artifact ID 5c5fa003-eb50-47e5-b162-c0ad5350bac8，稍作调整以匹配 keep_teams_active_gui.py）：


2. 生成 .exe 可执行文件
为使 keep_teams_active_gui.py 可在无 Python 环境的 Windows 上运行，使用 cx_Freeze 生成 .exe（避免之前的 PyInstaller 问题）。


安装 cx_Freeze 和 pyautogui：
pip install cx_Freeze pyautogui

步骤 2：创建 setup.py
在 keep_teams_active_gui.py 所在目录（如 ~/Desktop/teams-keep-active）创建 setup.py：

步骤 3：使用 build 语句生成 .exe
运行 build 命令：
cd ~/Desktop/teams-keep-active
python setup.py build

输出：build/exe.win-amd64-5.x 文件夹（x 为 Python 版本），包含 TeamsKeepActive.exe 和依赖文件。
验证 .exe：
双击 build/exe.win-amd64-5.x/TeamsKeepActive.exe。
