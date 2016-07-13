import requests
import json
from twitter_client import Tweet
import time
from config import *


class HNTweetService():
    def __init__(self):
        self.tweeted_ids = []
        self.twitter = Tweet()
        print 'HN Service initiated!'

    @staticmethod
    def get_top_story_ids():
        response = requests.get(
            'https://hacker-news.firebaseio.com/v0/topstories.json'
        )
        return json.loads(response.content)[:5]

    @staticmethod
    def get_item_content(id):
        response = requests.get(
            'https://hacker-news.firebaseio.com/v0/item/' + str(id) + '.json'
        )
        return json.loads(response.content)

    def construct_tweet(self, content):
        hash_tag = '#hacker_news '
        title = content['title'] + ' '
        if len(title) > 50:
            title = title[:50] + '... '
        url = content['url']
        tweet = hash_tag + title + url
        return tweet

    def tweet_posts(self):
        ids = self.get_top_story_ids()
        for id in ids:
            if id not in self.tweeted_ids:
                content = self.get_item_content(id)
                tweet_msg = self.construct_tweet(content)
                self.twitter.send_tweet(tweet_msg)
                self.tweeted_ids.append(id)
                print 'tweeted' + tweet_msg
                time.sleep(60)
            else:
                print 'already tweeted'

hts = HNTweetService()
while True:
    hts.tweet_posts()
    print 'waiting for ' + UPDATE_INTERVAL + ' seconds'
    time.sleep(UPDATE_INTERVAL)
