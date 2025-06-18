import numpy as np
import pandas as pd
import string
import matplotlib.pyplot as plt

df = pd.read_csv('customer_review.csv')

df = df[df['Sentiment'].isin(['positive', 'negative'])]

def clean_text(text):
    text = text.lower()
    return text.translate(str.maketrans('','',string.punctuation))

df['Cleaned Review'] = df['Review'].astype(str).apply(clean_text)

df['Word Count'] = df['Cleaned Review'].apply(lambda x: len(x.split()))

avg_word_count = df.groupby('Sentiment')['Word Count'].mean()
print("Average Word Count:")
print(avg_word_count)

positive_wc = df[df['Sentiment'] == 'positive']['Word Count']
negative_wc = df[df['Sentiment'] == 'negative']['Word Count']

plt.figure(figsize=(10,6))
plt.hist(positive_wc, bins=15, alpha=0.7, label='Positive', color='green')
plt.hist(negative_wc, bins=15, alpha=0.7, label='Negative', color='red')
plt.title("Word Count Distribution by Sentiment")
plt.xlabel('Word Count')
plt.ylabel("Number of Reviews")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()