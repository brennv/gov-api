import tweepy
import os

CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
OAUTH_TOKEN = os.getenv('TWITTER_OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.getenv('TWITTER_OAUTH_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter = tweepy.API(auth)
