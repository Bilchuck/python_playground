import tweepy, json, codecs, sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

TWITTER_USER = sys.argv[1]
WORDS = sys.argv[2:]

api_key="1Pt47VlVcVui9AFV3RnJJ3udg"
api_secret="mgTnmQIiT4RZINwVj9KG72jfz00J3KO8ek3o5wNmcTVQU88MLR"
token_key="349607054-z8YdkS4zwjDf8tqOjKN8EdKwiMjB4zcoOLulRmtg"
token_secret="cl6vfcqQKr9oRtO1BV3VT3PIV5PZRwwLjvKxuySPpA4cR"

auth=tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token_key, token_secret)

api = tweepy.API(auth)
stuff = api.user_timeline(screen_name = TWITTER_USER, count = 1000, include_rts = True)
tweets = []

for status in stuff:
    tweets.append(status._json)

df = pd.DataFrame(tweets, columns=['text'])

def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
  
words_count = {}

for word in WORDS:
  words_count[word] = 0

for index, row in df.iterrows():
  row1=row['text']
  for word in WORDS:
    found_words = word_in_text(word, row1)
    words_count[word] = words_count[word] + found_words

list_statistic=[]
for word in WORDS:
  list_statistic.append(words_count[word])

labels=WORDS

# sns.set(color_codes=True)

plt.pie(list_statistic, labels=WORDS, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
ax=sns.barplot(labels, list_statistic)
ax.set(ylabel='count')
plt.show()