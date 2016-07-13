import requests
import json


class HNClient():
    def __init__(self):
        print 'HN Client initiated!'

    def get_latest_posts():
        print 'latest posts'

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
        return response.content

# h = HNClient()
# ids = h.get_top_story_ids()
# print h.get_item_content(ids[0])
