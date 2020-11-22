import tweepy
import os
from os import environ
import time
import random
import sys
from google_images_search import GoogleImagesSearch
from imutils.object_detection import non_max_suppression
import cv2
from detect_text import detect_text
from get_twitter_api import get_twitter_api

def main():
    
    print("getting Twitter API")
    api = get_twitter_api()
    
    # set tweeting time interval
    #INTERVAL = 60 * 60 * 1  # tweet every 1 hour (prod)
    INTERVAL = 30  # every 30 seconds, for testing
    
    while True:
        
        randint=random.randint(1,1000000)
        print(f"time to tweet! beep boop boop {randint} have a great day")
        
        #this is a photo of me with my favorite chicken. Her name is Spoopy. I love her. She is not text.
        spoopy_pic="images/spoopy.jpg"
        spoopy_result = detect_text(spoopy_pic)
        print(f"Does {spoopy_pic} contain text? {spoopy_result}")
    
        # tweet the tweet
        api.update_status(f"beep boop boop {randint} have a great day oh and by the way {spoopy_result}")
        
        print("Tweeted, sleeping again...")
        #sleep for 10 seconds
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
    