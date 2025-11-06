import whisper
from .utils import format_timestamp

def transcribe_translate(audio_path: str, model_size="medium"):
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path, task="translate", language="ru")
    print("[✓] Transcription & translation complete.")
    return result

def save_srt(result, output_file: str):
    with open(output_file, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"], 1):
            f.write(f"{i}\n")
            f.write(f"{format_timestamp(segment['start'])} --> {format_timestamp(segment['end'])}\n")
            f.write(f"{segment['text'].strip()}\n\n")
    print(f"[✓] Subtitles saved to: {output_file}")