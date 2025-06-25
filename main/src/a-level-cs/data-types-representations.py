import numpy as np
from scipy.io.wavfile import write
import soundfile as sf
from PIL import Image
import pandas as pd

# Numbers: Calculate mean
numbers = [1, 2, 3, 4, 5]
mean = sum(numbers) / len(numbers)
print("Mean:", mean)

# Text: Count words
text = "Hello world! Hello Python."
words = text.split()
print("Word count:", len(words))

# Create a simple audio file (WAV)
samplerate = 44100  # Hz
duration = 2  # seconds
frequency = 440  # Hz (A4 note)
t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
data = 0.5 * np.sin(2 * np.pi * frequency * t)
write('example.wav', samplerate, data.astype(np.float32))
# Sound: Write audio file (WAV)

# Sound: Read audio file (WAV)
data, samplerate = sf.read('example.wav')
print("Audio shape:", data.shape)

# Create a new RGB image (100x100) with a red background
img = Image.new('RGB', (100, 100), color='red')
img.save('example.jpg')
# Image: Create and save image
# Image: Open and show image
img = Image.open('example.jpg')
img.show()

# Create a simple DataFrame and save as data.csv
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35]
})
df.to_csv('data.csv', index=False)

# CSV: Read and display data
df = pd.read_csv('data.csv')
print(df.head())

# Create a simple DataFrame and save as data.xlsx
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35]
})
df.to_excel('data.xlsx', index=False)
# Excel: Read and display data
df = pd.read_excel('data.xlsx')
print(df.head())
# Excel: Read and display data

import pandas as pd

# Create a simple DataFrame and save as data.json (array of objects)
df = pd.DataFrame({
    'name': ['Robert', 'Alice', 'Charlie'],
    'age': [30, 25, 35]
})
df.to_json('data.json', orient='records', lines=False)

# JSON: Read and display data
df = pd.read_json('data.json', orient='records')
print(df.head())

# JSON: Read and display data
import json
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
# Data Types and Representations in Python
