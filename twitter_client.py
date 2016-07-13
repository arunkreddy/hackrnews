import tweepy
from config import *

# api = tweepy.API(auth)
# api.update_status('hello world!')


class Tweet():
    def __init__(self):
        auth = tweepy.OAuthHandler(
            TWITTER_CONSUMER_KEY,
            TWITTER_CONSUMER_SECRET)
        auth.set_access_token(
            TWITTER_ACCESS_TOKEN,
            TWITTER_ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)
        print 'Twitter client initiated'

    def send_tweet(self, tweet):
        self.api.update_status(tweet)
