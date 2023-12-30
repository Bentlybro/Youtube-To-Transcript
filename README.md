# YouTube to Transcript
This Python script offers a convenient and automated way to transcribe audio from YouTube videos and shorts. Utilizing OpenAI's Whisper model, the script simplifies the process of transcribing any YouTube content. Here's how it works:

1. **Start the Script**: Upon running the script, it automatically fetches the base OpenAI Whisper model, setting up the foundation for accurate transcription.
2. **Input the YouTube URL**: Users can input the URL of any YouTube video or short they wish to transcribe.
3. **Automatic Audio Download and Transcription**: The script handles the downloading of the video's audio and then proceeds to transcribe it using the Whisper model.
4. **Saving Files**: Both the audio file and the transcription text are saved in a folder named after the YouTube video or short.

## Features
- **Support for Various YouTube Content**: Works with standard YouTube videos as well as YouTube shorts.
- **Automated Download and Transcription**: Streamlines the process of audio extraction and transcription.
- **Easy Storage and Organization**: Automatically creates and organizes files in dedicated folders.

## Usage
To use the script, simply follow these steps:
1. Clone the repository.
2. Install the necessary dependencies. ```pip install -r requirements.txt```
3. Run the script and follow the on-screen instructions to input the YouTube URL. ```python script.py```

## Requirements
- Python 3.x
- Necessary Python libraries (listed in `requirements.txt`)

## Contributions and Feedback
Contributions to enhance the script are welcome! If you encounter any issues or have suggestions, please feel free to open an issue or submit a pull request.

---
