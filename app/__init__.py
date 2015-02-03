import tweepy
import json

from flask import Flask

app = Flask(__name__)

def _parse_credentials(infile):
    with open(infile, 'rb') as f:
        credentials = json.loads(f.read())
    return credentials

twitter_infile = 'tweepy_demo_credentials.json'
twitter_cred = _parse_credentials(twitter_infile)
app.config.setdefault('TWEEPY_CONSUMER_KEY', twitter_cred['consumer_key'])
app.config.setdefault('TWEEPY_CONSUMER_SECRET', twitter_cred['consumer_secret'])
app.config.setdefault('TWEEPY_ACCESS_TOKEN_KEY', twitter_cred['access_token'])
app.config.setdefault('TWEEPY_ACCESS_TOKEN_SECRET', twitter_cred['access_token_secret'])

auth = tweepy.OAuthHandler(app.config['TWEEPY_CONSUMER_KEY'], app.config['TWEEPY_CONSUMER_SECRET'])
auth.set_access_token(app.config['TWEEPY_ACCESS_TOKEN_KEY'], app.config['TWEEPY_ACCESS_TOKEN_SECRET'])
twitter_api = tweepy.API(auth)

from app import views
