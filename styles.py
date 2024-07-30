import tkinter as tk
from tkinter import ttk

def apply_styles(root):
  style = ttk.Style()
  
  for widget in root.winfo_children():
        if isinstance(widget, tk.Button):
            widget.configure(bg="#4CAF50", fg="white", font=("Helvetica", 12),border=10)
        elif isinstance(widget, tk.Label):
            widget.configure(bg="#FFFFFF", fg="#333333", font=("Helvetica", 12),border=10)
        elif isinstance(widget, tk.Entry):
            widget.configure(font=("Helvetica", 12),border=10)
  
  
  style.configure("TProgressbar",
                    thickness=20,
                    troughcolor='#FFFFFF',
                    background='#4CAF50')