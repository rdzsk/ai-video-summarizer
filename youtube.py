import yt_dlp
from pathlib import Path

def download_video(video_url: str) -> Path:
    output_dir = Path("downloads")
    output_dir.mkdir(exist_ok=True)
    
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "quiet":True,
        "no_warnings":True,
        "js_runtimes": {
            "node": {}
        },
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality":"64",
            }
        ],
        "postprocessor_args": [
            "-ac", "1",
            "-ar", "16000",
        ],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            video_id = info["id"]
            video_name = info["title"]
    except Exception as e:
        print(f"ERROR {e}")
    return video_name,video_id
