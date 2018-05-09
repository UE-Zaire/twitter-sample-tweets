import pandas as pd
import nltk

nltk.download()

df = pd.read_json('dan-abramov-tweets.json')
print(df.head(100))

tokens = [nltk.word_tokenize(tweet) for tweet in df['body']]
