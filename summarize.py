from google import genai
import os 

client = genai.Client(api_key=os.getenv("GEMINI_API"))
def vtt_to_txt(video_id):
    with open(f"{video_id}.vtt",'rb') as f:
        file = f.read()
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"Привіт зроби вижимку всього тексту з таймкодами {file}",
    )

    return response.text

