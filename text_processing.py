from typing import List, Dict

def classify_speakers(segments: List[Dict], time_threshold: float = 1.0) -> List[Dict]:
    classified_segments = []
    current_speaker = 1
    last_end_time = 0

    for segment in segments:
        start_time = segment['start']
        if start_time - last_end_time > time_threshold:
            current_speaker = 3 - current_speaker  # Switch between 1 and 2

        classified_segments.append({
            'speaker': current_speaker,
            'start': segment['start'],
            'end': segment['end'],
            'text': segment['text']
        })
        last_end_time = segment['end']

    return classified_segments

def create_script(classified_segments: List[Dict]) -> str:
    script = ""
    for segment in classified_segments:
        timestamp = f"{segment['start']:.2f} - {segment['end']:.2f}"
        script += f"Speaker {segment['speaker']} [{timestamp}]: {segment['text']}\n\n"
    return script