from cx_Freeze import setup, Executable
import sys

build_exe_options = {
    "packages": ["pyautogui", "tkinter"],
    "include_files": []
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="TeamsKeepActive",
    version="1.0",
    description="Keep Microsoft Teams Active",
    options={"build_exe": build_exe_options},
    executables=[Executable("keep_teams_active_gui.py", base=base, target_name="TeamsKeepActive.exe")]
)