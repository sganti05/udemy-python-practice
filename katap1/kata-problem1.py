import numpy as np
import pandas as pd
import string # imported to help remove punctuations from the csv

df =  pd.read_csv('lyrics.csv') # reads the csv file using pandas

def clean_lyrics(text):
    text = text.lower() # converts lyrics to lowercase
    return text.translate(str.maketrans('', '', string.punctuation)) # removes punctuation

cleaned_lyrics = [clean_lyrics(lyric) for lyric in df['Lyrics'].dropna()]

# performs random sampling of 10 lyrics
sample_indices = np.random.choice(len(cleaned_lyrics), size=10, replace=False) 
sampled_lyrics = np.array(cleaned_lyrics)[sample_indices]

for i, line in enumerate(sampled_lyrics, 1): # enumerate helps loop through the list of sampled lyrics and starts counting from 1 instead of 0
    print(f"{i}. {line}")
