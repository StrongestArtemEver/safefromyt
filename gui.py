import tkinter as tk
from tkinter import filedialog, ttk
from downloader import download_video
from styles import apply_styles
import utils

root = tk.Tk()
root.title("SafeFromYT")
root.configure(bg="#EFF3EC")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width / 2)
window_height = int(screen_height / 2)
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

utils.enable_high_dpi()
utils.enable_retina_display()

root.save_directory = ""

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        label.config(text=f"Save directory is: {folder_path}")
        root.save_directory = folder_path

def start_download():
    url = urlInput.get()
    if not root.save_directory:
        error_label.config(text="Please select a save directory first.")
        return
    if not url:
        error_label.config(text="Please enter a YouTube URL.")
        return
    try:
        error_label.config(text="")
        download_video(url, root.save_directory, progress_callback)
    except Exception as e:
        error_label.config(text=f"Error: {e}")

def progress_callback(d):
    if d['status'] == 'downloading':
        total_size = d.get('total_bytes') or d.get('total_bytes_estimate')
        bytes_downloaded = d['downloaded_bytes']
        percentage = (bytes_downloaded / total_size) * 100
        progress_var.set(percentage)
        speed_label.config(text=f"Downloaded: {bytes_downloaded} bytes")

label = tk.Label(root, text="Press button to choose save directory!")
label.pack(pady=20)

button = tk.Button(root, text="Press Me!", command=select_folder)
button.pack(pady=20)

urlLabel = tk.Label(root, text="Put your link below")
urlLabel.pack(pady=20)

urlInput = tk.Entry(root, width=50)
urlInput.pack(pady=20)

downloadButton = tk.Button(root, text="Download", command=start_download)
downloadButton.pack(pady=20)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(pady=20)

speed_label = tk.Label(root, text="")
speed_label.pack(pady=20)

error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=20)

apply_styles(root)

def create_main_window():
    root.mainloop()

if __name__ == "__main__":
    create_main_window()
