import tweepy
import os
import time
import random
import sys
from os import environ

def main():
    
    # get twitter auth creds
    CONSUMER_KEY = environ["CONSUMER_KEY"]
    CONSUMER_SECRET = environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = environ["ACCESS_TOKEN_SECRET"]
    
    # set tweeting time interval
    #INTERVAL = 60 * 60 * 1  # tweet every 1 hour (prod)
    INTERVAL = 15  # every 15 seconds, for testing

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    # Create API object
    api = tweepy.API(auth)
    
    while True:
        
        randint=random.randint(1,1000000)
        print(f"time to tweet! beep boop boop {randint} have a great day")
        
        # tweet the tweet
        api.update_status(f"beep boop boop {randint} have a great day")
        
        print("Tweeted, sleeping again...")
        #sleep for 10 seconds
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
    