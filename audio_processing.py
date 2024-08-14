import os
from pydub import AudioSegment

def convert_to_wav(input_path):
    _, file_extension = os.path.splitext(input_path)
    file_extension = file_extension.lower()[1:]

    if file_extension == 'wav':
        return input_path

    output_path = 'temp_audio.wav'
    try:
        audio = AudioSegment.from_file(input_path, format=file_extension)
        audio.export(output_path, format="wav")
        print(f"Converted {file_extension} to wav")
        return output_path
    except Exception as e:
        print(f"Error converting audio file: {e}")
        return None