# %%
import tweepy
from config import twitter_id
from doge_api import create_api
from doge_logging import logger
from doge_stream_listener import DogeStreamListener

# %%
if __name__ == '__main__':
    api = create_api()
    tweets_listener = DogeStreamListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(follow=[twitter_id])