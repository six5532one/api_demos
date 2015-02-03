import tweepy
import json

from flask import render_template
from app import app, twitter_api

@app.route('/trend/<query>')
def trend(query, num_tweets_per_trend = 10):
    results = []
    try:
        for status in tweepy.Cursor(twitter_api.search, q=query).items(num_tweets_per_trend):
            results.append({'handle': status.author.screen_name, 'username': status.author.name, 'text': status.text})
    except:
        #TODO handle
        raise
    return render_template("trend_details.html", title="Twitter Trend - Most Recent Tweets", details=results) 

@app.route('/trends')
def trends(WOEID = 23424977):
    try:
        results = twitter_api.trends_place(WOEID)[0]['trends']
    except:
        #TODO handle
        results = []
        raise
    return render_template("trends.html", title="Twitter Trends", trends=results)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Menu")
