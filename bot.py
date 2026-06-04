import os
import random
import tweepy

words = ["ミク", "胸", "パッド"]

tweet = f"{random.choice(words)}の{random.choice(words)}は{random.choice(words)}入り"

client = tweepy.Client(
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
)

client.create_tweet(text=tweet)
