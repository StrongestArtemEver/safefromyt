from cx_Freeze import setup, Executable
import sys

# Опции для сборки
build_exe_options = {
    "packages": ["tkinter", "yt_dlp"],
    "excludes": [],
    "include_files": []
}

# base="Win32GUI" используется только для Windows GUI приложений
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="SafeFromYT",
    version="0.1",
    description="YouTube video downloader",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)
