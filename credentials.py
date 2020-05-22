import json
import tweepy
import requests

def getCredentials(item):
    with open('credentials.json', 'r') as credentials:
        data = credentials.read()
    if item == "twitter":
        consumer_key = ((json.loads(data)['twitter']['consumer_key']))
        consumer_secret = ((json.loads(data)['twitter']['consumer_secret']))
        access_token = ((json.loads(data)['twitter']['access_token']))
        access_token_secret = ((json.loads(data)['twitter']['access_token_secret']))
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return (api)
    
        
