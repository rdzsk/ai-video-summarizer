import os
from pathlib import Path
from youtube import download_video
from summarize import vtt_to_txt
from local import audio_to_txt

def summarize_video(video_url: str, obsidian: Path):
    project_root=Path.cwd()
    download_dir=project_root / "downloads"
    video_name,video_id =download_video(video_url) 
    video_file=download_dir/f"{video_id}.mp3"

    try:
        audio_to_txt(video_id)
        return {
            "summary":vtt_to_txt(video_id,video_name,obsidian)
        }

    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        Path(f"{project_root}/{video_id}.vtt").unlink()
        for file in download_dir.iterdir():
            if file.is_file():
                file.unlink()






        


if __name__ == "__main__":
    while True:
        url = input("URL: ")
        obsidian = Path(input("Obsidian vault path: "))
        try:
            summarize_video(url,obsidian)
            break
        except Exception as e:
            print(f"ERROR {e}")
            if input("Retry? (y/n): ").lower() != "y":
                break



