from utils import check_dependencies
from audio_processing import convert_to_wav
from transcription import transcribe_audio, cleanup
from text_processing import classify_speakers, create_script

def main():
    check_dependencies()

    audio_path = 'audo.m4a'
    wav_path = convert_to_wav(audio_path)
    
    if wav_path:
        result = transcribe_audio(wav_path)
        cleanup(wav_path, audio_path)
        
        if result:
            classified_segments = classify_speakers(result['segments'])
            script = create_script(classified_segments)
            
            print("Transcription Script:")
            print(script)

            # Optionally, save the script to a file
            with open('transcription_script.txt', 'w', encoding='utf-8') as f:
                f.write(script)
            print("Script saved to 'transcription_script.txt'")

if __name__ == "__main__":
    main()