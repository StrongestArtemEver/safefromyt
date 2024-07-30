import ctypes
import tkinter

def enable_high_dpi():
    try:
      ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception as e:
      print(f"Ошибка при включении DPI: {e}")


def enable_retina_display():
  if tkinter.TkVersion >= 8.6:
      from ctypes import cdll, c_int

      try:
          libtk = cdll.LoadLibrary('/System/Library/Frameworks/Tk.framework/Tk')
          libtk.Tk_SetOptions(None, c_int(1), None)
      except Exception as e:
          print(f"Ошибка при включении Retina: {e}") 