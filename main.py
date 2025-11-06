import os
from config import OUTPUT_DIR, MODEL_SIZE
from getShorts import download_audio
from utils.translateShorts import transcribe_translate, save_srt

def run_pipeline(video_url):
    raw_dir = os.path.join(OUTPUT_DIR, "raw")
    srt_path = os.path.join(OUTPUT_DIR, "translated_en.srt")

    print("[→] Step 1: Downloading...")
    audio_path = download_audio(video_url, raw_dir)

    print("[→] Step 2: Translating...")
    result = transcribe_translate(audio_path, MODEL_SIZE)

    print("[→] Step 3: Saving subtitles...")
    save_srt(result, srt_path)

if __name__ == "__main__":
    url = input("Enter the YouTube Shorts URL: ").strip()
    run_pipeline(url)