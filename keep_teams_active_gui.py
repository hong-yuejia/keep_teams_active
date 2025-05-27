import pyautogui
import time
import random
import logging
import tkinter as tk
from threading import Thread, Event

# 设置日志
logging.basicConfig(
    filename='teams_active.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    encoding='utf-8'
)

# 设置 PyAutoGUI
pyautogui.FAILSAFE = False  # 禁用 FAILSAFE，防止手动鼠标移动中断
pyautogui.PAUSE = 0.3  # 每次操作后暂停 0.3 秒

# 全局变量
stop_event = None  # 线程控制事件
thread = None  # 当前线程

def keep_active():
    """保持 Teams 在线的线程函数"""
    while not stop_event.is_set():
        try:
            # 记录鼠标位置
            current_x, current_y = pyautogui.position()
            logging.info(f"Mouse position: ({current_x}, {current_y})")
            # 随机移动鼠标（小幅度）
            x_offset = random.randint(-5, 5)
            y_offset = random.randint(-5, 5)
            pyautogui.moveRel(x_offset, y_offset, duration=0.0)
            logging.info(f"Mouse moved: ({x_offset}, {y_offset})")
            label_status.config(text=f"鼠标移动: ({x_offset}, {y_offset})")
            # 模拟键盘操作
            pyautogui.press('shift')
            logging.info("Simulated key press: Shift")
            # 每 15 秒活动一次
            time.sleep(15)
        except Exception as e:
            logging.error(f"Error: {e}")
            label_status.config(text=f"错误: {e}")
            time.sleep(2)  # 出错后稍等，避免频繁错误

def start_script():
    """启动脚本"""
    global stop_event, thread
    # 初始化停止事件
    if stop_event is None or stop_event.is_set():
        stop_event = Event()
    # 确保上一个线程已结束
    if thread is not None and thread.is_alive():
        stop_event.set()
        thread.join()
    # 启动新线程
    thread = Thread(target=keep_active)
    thread.daemon = True  # 守护进程线程，随程序退出
    thread.start()
    label_status.config(text="脚本运行中...")
    button_start.config(state="disabled")
    button_stop.config(state="normal")
    logging.info("Script started")

def stop_script():
    """停止脚本"""
    global stop_event
    if stop_event is not None:
        stop_event.set()
        if thread is not None and thread.is_alive():
            thread.join()
        label_status.config(text="脚本已停止")
        button_start.config(state="normal")
        button_stop.config(state="disabled")
        logging.info("Script stopped")

# 创建 GUI
root = tk.Tk()
root.title("Teams 保持在线")
root.geometry("300x150")
root.resizable(False, False)  # 固定窗口大小

# 状态标签
label_status = tk.Label(root, text="点击开始运行脚本", font=("Arial", 12))
label_status.pack(pady=10)

# 按钮框架
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# 开始按钮
button_start = tk.Button(button_frame, text="开始", command=start_script, width=10, font=("Arial", 10))
button_start.pack(side=tk.LEFT, padx=5)

# 停止按钮
button_stop = tk.Button(button_frame, text="停止", command=stop_script, width=10, font=("Arial", 10), state="disabled")
button_stop.pack(side=tk.LEFT, padx=5)

# 窗口关闭处理
def on_closing():
    """窗口关闭时清理线程"""
    if stop_event is not None:
        stop_event.set()
        if thread is not None and thread.is_alive():
            thread.join()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# 运行 GUI
root.mainloop()