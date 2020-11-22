import tweepy
from os import environ

def get_twitter_api():
    
    # get twitter auth creds
    CONSUMER_KEY = environ["TWITTER_CONSUMER_KEY"]
    CONSUMER_SECRET = environ["TWITTER_CONSUMER_SECRET"]
    ACCESS_TOKEN = environ["TWITTER_ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = environ["TWITTER_ACCESS_TOKEN_SECRET"]
    
    # set tweeting time interval
    #INTERVAL = 60 * 60 * 1  # tweet every 1 hour (prod)
    INTERVAL = 30  # every 15 seconds, for testing

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    # Create API object
    api = tweepy.API(auth)
    
    return api