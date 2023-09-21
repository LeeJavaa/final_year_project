import librosa
from pydub import AudioSegment
import pandas as pd
import numpy as np
import re

df = pd.read_csv("../data/dataset/validation/validation.csv")
audio_df = pd.DataFrame(columns=['id', 'speech_rate', 'pitch_range'])

def convert_duration_to_seconds(duration):
    pattern = r'PT(\d+H)?(\d+M)?(\d+S)?'
    hours, minutes, seconds = re.match(pattern, duration).groups()
    
    total_seconds = 0
    if hours:
        total_seconds += int(hours[:-1]) * 3600
    if minutes:
        total_seconds += int(minutes[:-1]) * 60
    if seconds:
        total_seconds += int(seconds[:-1])
    
    return total_seconds

def convert_mp4_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="mp4")
    audio.export(output_file, format="wav")

# for audio_id in df['id']:
#     # Import audio file
#     audio_file = f'../data/audio/validation/{audio_id}.mp4'
#     convert_mp4_to_wav(audio_file, "./audio.wav")
#     y, sr = librosa.load('./audio.wav')

#     # Calculate pitch range
#     pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
#     threshold = 1
#     pitches = pitches[magnitudes > threshold]
#     pitch_range = pitches.max() - pitches.min()
#     print(pitch_range)

#     # Calculate speech rate
#     duration = convert_duration_to_seconds(df[df['id'] == audio_id].iloc[0]['duration'])
#     transcript = df[df['id'] == audio_id].iloc[0]['transcript']
#     words = len(transcript.split())
#     speech_rate = (words / duration)*60
#     print(speech_rate)

#     # Add row to df
#     new_row = {'id': audio_id, 'speech_rate': speech_rate, 'pitch_range': pitch_range}
#     audio_df = pd.concat([audio_df, pd.DataFrame([new_row])], ignore_index=True)

#     # print out df
#     print(audio_df)

# audio_df.to_csv("../data/dataset/validation/validation_audio.csv", header=True, index=False)