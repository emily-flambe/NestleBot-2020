import tweepy
import os
from os import environ
import time
import random
import sys
from google_images_search import GoogleImagesSearch
from imutils.object_detection import non_max_suppression
#import cv2
#import detect_text_function as dtf #lol

def main():
    
    # get twitter auth creds
    CONSUMER_KEY = environ["CONSUMER_KEY"]
    CONSUMER_SECRET = environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = environ["ACCESS_TOKEN_SECRET"]
    
    # set tweeting time interval
    #INTERVAL = 60 * 60 * 1  # tweet every 1 hour (prod)
    INTERVAL = 30  # every 15 seconds, for testing

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
    