import yaml
import tweepy
import os

# os.path.abspath(os.path.dirname(__file__))
root = os.path.abspath(os.path.dirname(__file__))
print(os.listdir())

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# twitter = tweepy.API(auth)

filepath = os.path.join(root, 'congress-legislators', 'legislators-current.yaml')
with open(filepath) as f:
    congress_names = yaml.load(f)

filepath = os.path.join(root, 'congress-legislators', 'legislators-social-media.yaml')
with open(filepath) as f:
    congress_social = yaml.load(f)

filepath = os.path.join(root, 'more-data', 'governors.yaml')
with open(filepath) as f:
    governors = yaml.load(f)

filepath = os.path.join(root, 'more-data', 'international.yaml')
with open(filepath) as f:
    international = yaml.load(f)

filepath = os.path.join(root, 'more-data', 'whitehouse.yaml')
with open(filepath) as f:
    whitehouse = yaml.load(f)


def merge_congress(names, social):
    data = {}
    for n in names:
        bioguide = n['id']['bioguide']
        data[bioguide] = n
    for s in social:
        bioguide = s['id']['bioguide']
        data[bioguide]['social'] = s['social']
    return data


def merge_data(data, more_data):
    for m in more_data:
        bioguide = m['id']['bioguide']
        data[bioguide] = m
    return data


def get_twitter_handles(data):
    handles = {}
    warnings = []
    for k, v in data.items():
        try:
            handles[k] = v['social']['twitter']
        except KeyError:
            if 'social' in v:
                warnings.append(' * No twitter data for ' + v['id']['bioguide'])
            else:
                warnings.append(' * No social data for ' + v['id']['bioguide'])
            handles[k] = ''
    if warnings:
        print(' * Data warnings:', len(warnings))
        for w in warnings:
            print(w)
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


congress = merge_congress(congress_names, congress_social)

data = congress.copy()
data = merge_data(data, governors)
data = merge_data(data, international)
data = merge_data(data, whitehouse)

twitter_ids = get_twitter_handles(data)
data, tweets = get_tweets(data, twitter_ids)

twitter_ids = [v for k, v in twitter_ids.items()]
data = [v for k, v in data.items()]
