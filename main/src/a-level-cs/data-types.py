# Numbers: Calculate mean
numbers = [1, 2, 3, 4, 5]
mean = sum(numbers) / len(numbers)
print("Mean:", mean)

# Text: Count words
text = "Hello world! Hello Python."
words = text.split()
print("Word count:", len(words))

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