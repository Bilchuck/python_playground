import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path="tweets.txt"

tweets_data=[]

file=open(file_path, 'r')

for line in file:
  tweet=json.loads(line)
  tweets_data.append(tweet)

file.close()

df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

print(df.head())

[cat, dog] = [0, 0]

import re
def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

for index, row in df.iterrows():
  row1=row['text']
  cat += word_in_text('cat', row1)
  dog += word_in_text('dog', row1)

labels=["cat", "dog"]

sns.set(color_codes=True)

ax=sns.barplot(labels, [cat, dog])
ax.set(ylabel='count')
plt.show()