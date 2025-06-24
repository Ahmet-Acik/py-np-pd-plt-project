# Numbers: Calculate mean
numbers = [1, 2, 3, 4, 5]
mean = sum(numbers) / len(numbers)
print("Mean:", mean)

# Text: Count words
text = "Hello world! Hello Python."
words = text.split()
print("Word count:", len(words))

import numpy as np
from scipy.io.wavfile import write

samplerate = 44100  # Hz
duration = 2  # seconds
frequency = 440  # Hz (A4 note)
t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
data = 0.5 * np.sin(2 * np.pi * frequency * t)
write('example.wav', samplerate, data.astype(np.float32))

import soundfile as sf
# Sound: Read audio file (WAV)
data, samplerate = sf.read('example.wav')
print("Audio shape:", data.shape)

from PIL import Image
# Image: Open and show image
img = Image.open('example.jpg')
img.show()

import pandas as pd
# CSV: Read and display data
df = pd.read_csv('data.csv')
print(df.head())