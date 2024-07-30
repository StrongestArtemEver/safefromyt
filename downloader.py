import yt_dlp as youtube_dl
import logging

logging.basicConfig(level=logging.INFO)

def download_video(url, save_path, progress_callback):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'progress_hooks': [progress_callback]
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            logging.info(f"Video downloaded successfully: {url}")
    except Exception as e:
        logging.error(f"Error downloading video: {e}")
        raise
