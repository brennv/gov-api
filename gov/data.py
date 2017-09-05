from .twitter import twitter
import yaml
import os


base_path = os.path.dirname(__file__)

base_path = '/'.join(base_path.split('/')[:-1])

filepath = os.path.join(base_path, 'congress-legislators/legislators-current.yaml')
with open(filepath) as f:
    congress_names = yaml.load(f)

filepath = os.path.join(base_path, 'congress-legislators/legislators-social-media.yaml')
with open(filepath) as f:
    congress_social = yaml.load(f)


def merge_congress(names, social):
    congress_by_id = {}
    ids = []
    for n in names:
        bioguide = n['id']['bioguide']
        congress_by_id[bioguide] = n
        ids.append(bioguide)
    for s in social:
        bioguide = s['id']['bioguide']
        congress_by_id[bioguide]['social'] = s['social']
    return congress_by_id, ids


def get_legislator(bid, attr=None, subattr=None):
    bid = bid.upper()
    try:
        if subattr:
            result = congress_by_id[bid][attr][subattr]
        elif attr:
            result = congress_by_id[bid][attr]
        else:
            result = congress_by_id[bid]
    except KeyError:
        result = {"message": "Invalid request"}
    return result


def get_tweets(id):
    results = []
    twitter_id = str(get_legislator(id, 'social', 'twitter_id'))
    if twitter_id:
        results = twitter.user_timeline(id=twitter_id)  # , count=count)
        results = [x._json for x in results]
    return resultsn


congress_by_id, congress_ids = merge_congress(congress_names, congress_social)
congress = [v for k, v in congress_by_id.items()]
