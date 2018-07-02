import tweepy, json, codecs

api_key="1Pt47VlVcVui9AFV3RnJJ3udg"
api_secret="mgTnmQIiT4RZINwVj9KG72jfz00J3KO8ek3o5wNmcTVQU88MLR"
token_key="349607054-z8YdkS4zwjDf8tqOjKN8EdKwiMjB4zcoOLulRmtg"
token_secret="cl6vfcqQKr9oRtO1BV3VT3PIV5PZRwwLjvKxuySPpA4cR"

auth=tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(token_key, token_secret)

class MyStreamListener(tweepy.StreamListener):
  def __init__(self, api=None):
    super(MyStreamListener, self).__init__()
    self.num_tweets=0
    self.file=open('tweets.txt', 'w')

  def on_status(self, status):
    print('here')
    tweet=status._json
    self.file.write(json.dumps(tweet) + '\n')
    self.num_tweets=self.num_tweets+1
    # self.file.close()
    if self.num_tweets<100:
      return True
    else:
      return True

  def on_error(self, error):
    print(error)

l = MyStreamListener()
stream = tweepy.Stream(auth, l)

stream.filter(track=['cat', 'dog'])
