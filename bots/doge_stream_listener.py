from doge_logging import logger
import json
import tweepy


class DogeStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        self.keywords = ['doge', 'dogecoin', 'to the moon']

    def on_connect(self):
        logger.info("Bot is connected - Let's go to the moon")

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        logger.error(f'Bot Error {status}')

    def on_data(self, tweet):
        tweet = json.loads(tweet)
        text = tweet['text']

        if (self.is_doge_related(tweet['text'])):
            logger.info(f'[DogeTweet] {text}')
        else:
            logger.info(f'[NonDogeTweet] {text}')

    def on_timeout(self):
        logger.error("Timeout")

    def on_disconnect(self, notice):
        notice = json.loads(notice)
        code = notice['code']
        logger.error(f'Disconnected, code: {code}')

    def is_doge_related(self, text:str):
        has_doge_topic = False
        for k in self.keywords:
            if k.lower() in text.lower():
                has_doge_topic = True
                break
        return has_doge_topic
