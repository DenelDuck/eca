from eca import *
from eca.generators import start_offline_tweets

import datetime
import textwrap

root_content_path = 'dashboard_static'

@event('init')
def setup(ctx, e):
    # start the offline tweet stream
    start_offline_tweets('worldcupfinal_2014.txt', 'tweet', time_factor=10000)



@event('tweet')
def tweet(ctx, e):
    tweet = e.data
    text = tweet["text"]
    keywords = ["award", "golden ball", "goldenball", "golden glove", "goldenglove", "golden boot",
                "goldenboot", "best young player", "fifa fair play trophy"]
    for i in keywords:
        if "retweeted_status" not in tweet:
            if i.lower() in text.lower():
                emit('tweet', tweet)
#        elif "retweeted_status" in tweet:
#            retweettext = tweet["retweeted_status"]["text"]
#            if i.lower() in retweettext.lower():
#               emit('tweet', tweet)
