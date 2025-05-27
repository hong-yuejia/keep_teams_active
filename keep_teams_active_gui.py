import pyautogui
import time
import random
import tkinter as tk
from threading import Thread, Event
import logging

# 设置日志
logging.basicConfig(filename='teams_active.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# 设置 pyautogui
pyautogui.FAILSAFE = False  # 禁用 FAILSAFE
pyautogui.PAUSE = 0.5

# 全局停止事件
stop_event = Event()

def keep_active():
    while not stop_event.is_set():
        try:
            # 记录当前鼠标位置
            current_x, current_y = pyautogui.position()
            message = f"当前鼠标位置: ({current_x}, {current_y})"
            logging.info(message)
            
            # 随机移动鼠标
            x = random.randint(-10, 10)
            y = random.randint(-10, 10)
            pyautogui.moveRel(x, y, duration=0.2)
            message = f"鼠标移动: ({x}, {y})"
            label_status.config(text=message)
            logging.info(message)
            
            # 模拟键盘活动
            pyautogui.press('scrolllock')
            logging.info("模拟按键: ScrollLock")
            
        except Exception as e:
            message = f"错误: {e}"
            label_status.config(text=message)
            logging.error(message)
        
        time.sleep(180)

def start_script():
    global thread
    stop_event.clear()
    thread = Thread(target=keep_active)
    thread.start()
    label_status.config(text="脚本运行中...")
    button_start.config(state="disabled")
    button_stop.config(state="normal")
    logging.info("脚本启动")

def stop_script():
    stop_event.set()
    label_status.config(text="脚本已停止")
    button_start.config(state="normal")
    button_stop.config(state="disabled")
    logging.info("脚本停止")

# 创建 GUI
root = tk.Tk()
root.title("Teams 保持在线")
root.geometry("300x150")

label_status = tk.Label(root, text="点击开始运行脚本", font=("Arial", 12))
label_status.pack(pady=10)

button_start = tk.Button(root, text="开始", command=start_script, width=10)
button_start.pack(pady=5)

button_stop = tk.Button(root, text="停止", command=stop_script, width=10, state="disabled")
button_stop.pack(pady=5)

# 运行 GUI
root.mainloop()