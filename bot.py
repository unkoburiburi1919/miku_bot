import os
import tweepy

auth = tweepy.OAuth1UserHandler(
    os.environ["API_KEY"],
    os.environ["API_SECRET"],
    os.environ["ACCESS_TOKEN"],
    os.environ["ACCESS_TOKEN_SECRET"]
)

api = tweepy.API(auth)

user = api.verify_credentials()

print("認証成功:", user.screen_name)
