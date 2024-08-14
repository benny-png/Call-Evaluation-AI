import whisper
import os

def transcribe_audio(audio_path):
    try:
        model = whisper.load_model("base")
        print("Model loaded successfully")
    except Exception as e:
        print(f"Error loading Whisper model: {e}")
        return

    try:
        result = model.transcribe(audio_path, word_timestamps=True)
        print("Transcription completed")
        return result
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

def cleanup(wav_path, original_path):
    if wav_path != original_path:
        try:
            os.remove(wav_path)
        except Exception as e:
            print(f"Error removing temporary file: {e}")