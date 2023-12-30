from pytube import YouTube
import whisper
import os
import re
import warnings

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

def save_transcription(transcription, folder_path, file_name='transcription.txt'):
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(transcription)
    return file_path

def download_youtube_audio(url, folder_path):
    yt = YouTube(url)
    video_title = sanitize_filename(yt.title)
    folder_path = os.path.join(folder_path, video_title)
    os.makedirs(folder_path, exist_ok=True)

    audio_path = os.path.join(folder_path, 'audio.mp3')
    yt.streams.filter(only_audio=True).first().download(filename=audio_path)
    return audio_path, folder_path

def transcribe_audio(audio_path, model_name='base'):
    warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)
    return result['text']

video_url = input("Enter the YouTube video URL: ")
folder_path = 'Downloaded_Audios'

audio_path, folder_path = download_youtube_audio(video_url, folder_path)
transcription = transcribe_audio(audio_path)
transcription_file_path = save_transcription(transcription, folder_path)

print(f"Transcription saved to: {transcription_file_path}")
print("\nTranscription:\n")
print(transcription)
