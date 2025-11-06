import os
import subprocess

def download_audio(video_url: str, output_path: str):
    os.makedirs(output_path, exist_ok=True)
    command = [
        "yt-dlp",
        "-f", "bestaudio[ext=m4a]",
        "--output", f"{output_path}/audio.%(ext)s",
        video_url
    ]
    subprocess.run(command, check=True)
    print(f"[✓] Downloaded audio to: {output_path}")
    return os.path.join(output_path, "audio.m4a")