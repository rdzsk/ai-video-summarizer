import whisper
from whisper.utils import get_writer
def audio_to_txt(video_id):
    model = whisper.load_model("small")
    result = model.transcribe(
        f"downloads/{video_id}.mp3",
    
        
    )
    
    vtt_writer = get_writer("vtt",".")
    vtt_writer(result,video_id)
