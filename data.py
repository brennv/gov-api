import yaml
import tweepy
import os


consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# twitter = tweepy.API(auth)

with open('congress-legislators/legislators-current.yaml') as f:
    names = yaml.load(f)

with open('congress-legislators/legislators-social-media.yaml') as f:
    social = yaml.load(f)


def merge_social(names, social):
    data = {}
    for n in names:
        bioguide = n['id']['bioguide']
        data[bioguide] = n
    for s in social:
        bioguide = s['id']['bioguide']
        data[bioguide]['social'] = s['social']
    return data


def get_twitter_handles(data):
    handles = {}
    e = 0
    for k, v in data.items():
        try:
            handles[k] = v['social']['twitter']
        except KeyError:
            e += 1
            if 'social' in v:
                print('no twitter', v['id']['bioguide'])
            else:
                print('no social', v['id']['bioguide'])
            handles[k] = ''
    print('errors', e)
    return handles


def get_tweets(data, handles):
    all_tweets = []
    for k, v in handles.items():
        tweets = []
        if v:
            tweets = []  # twitter.user_timeline(v)
        data[k]['tweets'] = tweets
        all_tweets.append(tweets)
    return data, all_tweets


data = merge_social(names, social)
handles = get_twitter_handles(data)
data, tweets = get_tweets(data, handles)
