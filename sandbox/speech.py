"""
In this file I'll be doing some audio processing.

Some things I'd like to find in here are:
- Talking speed
- Variation in pitch
- Variation in speed
- Variation in intensity
- How similar does the speech mimic a story? intro, build up, climax, resolution, outro.
"""

import librosa
from pydub import AudioSegment
import pandas as pd
import matplotlib.pylab as plt
import numpy as np

# def convert_webm_to_wav(input_file, output_file):
#     audio = AudioSegment.from_file(input_file, format="webm")
#     audio.export(output_file, format="wav")

# convert_webm_to_wav("./audio.webm", "./audio.wav")

y, sr = librosa.load("./audio.wav")
# pd.Series(y).plot(figsize=(10, 5), lw=1, title="Raw audio output")
# plt.show()
# print(y.shape)
print(type(y))


# D = librosa.stft(y)
# S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
# print(S_db.shape)

# fig, ax = plt.subplots(figsize=(10, 5))
# img = librosa.display.specshow(S_db, x_axis='time', y_axis='log', ax=ax)
# ax.set_title("Spectogram", fontsize=20)
# fig.colorbar(img, ax=ax)
# plt.show()

# fig, ax = plt.subplots(figsize=(15, 5))
# S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=256)
# S_db_mel = librosa.amplitude_to_db(S, ref=np.max)
# img = librosa.display.specshow(S_db_mel, x_axis='time', y_axis='log', ax=ax)
# ax.set_title("Mel Spectogram", fontsize=20)
# fig.colorbar(img, ax=ax)
# plt.show()