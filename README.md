# Teams Keep Active

## 简介

`Teams Keep Active` 是一个工具，用于保持 Microsoft Teams 在线状态（绿色图标）。通过模拟鼠标移动和键盘操作，防止 Teams 因长时间无活动而变为“离开”或“离线”。程序提供简单的图形界面，易于启动和停止。

### 功能特点

- **图形界面**：基于 `tkinter`，包含“开始”和“停止”按钮，实时显示状态。
- **保持在线**：每 15 秒随机小幅度移动鼠标并模拟按键（如 `Shift`）。
- **可靠管理**：支持停止后重新开始，无需重启程序。
- **日志记录**：操作和错误保存至 `teams_active.log`，便于排查问题。
- **跨平台**：主要支持 Windows，Mac 可测试运行。

## 安装与依赖

### 前置条件
- **Python**：版本 3.8 至 3.11，建议从 [Python 官网](https://www.python.org/downloads/) 下载。
  - 安装时勾选“Add Python to PATH”。
- **依赖库**：`pyautogui` 和 `cx_Freeze`。

### 安装依赖
在项目目录下运行以下命令安装所需库：
```bash
pip install pyautogui cx_Freeze
```

验证 Python 安装：
```bash
python --version
```

## 生成 .exe 可执行文件

在 Windows 上，可将 `keep_teams_active_gui.py` 打包为独立 `.exe` 文件，无需 Python 环境即可运行。

### 步骤 1：创建 `setup.py`
在 `keep_teams_active_gui.py` 所在目录创建 `setup.py` 文件，内容包括：

- 配置 `cx_Freeze` 以打包程序及其依赖。
- 指定生成 Windows GUI 应用（无命令行窗口）。
- 输出可执行文件名为 `TeamsKeepActive.exe`。

### 步骤 2：运行构建命令
执行以下命令生成 `.exe`：
```bash
cd ~/Desktop/teams-keep-active  # 替换为你的项目目录
python setup.py build
```

- **输出**：生成 `build/exe.win-amd64-5.x` 文件夹（`x` 取决于 Python 版本），包含 `TeamsKeepActive.exe` 和依赖文件。
- **验证**：双击 `build/exe.win-amd64-5.x/TeamsKeepActive.exe`，启动 GUI，点击“开始”确保 Teams 保持在线，检查 `teams_active.log`。

## 使用说明
1. 运行 `TeamsKeepActive.exe` 或 `python keep_teams_active_gui.py`。
2. 点击“开始”按钮启动脚本，Teams 将保持在线状态。
3. 点击“停止”暂停脚本，可随时重新开始。
4. 检查 `teams_active.log` 查看操作记录。

## 注意事项
- **合规性**：确保公司允许使用此类工具。
- **测试环境**：建议在非生产环境测试。
- **调整频率**：若 Teams 未保持在线，可参考日志调整脚本间隔（需修改源代码）。

