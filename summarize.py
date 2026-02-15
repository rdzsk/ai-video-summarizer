from google import genai
import os 

client = genai.Client(api_key=os.getenv("GEMINI_API"))
def vtt_to_txt(video_id,video_name,obsidian):
    with open(f"{video_id}.vtt",'rb') as f:
        file = f.read()
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"Make a summarize with timecodes in markdown (LANGUAGE SAME WITH TEXT): {file}",
    )

    with open(f'{obsidian}/{video_name}.md','w') as file:
        file.write(response.text)

