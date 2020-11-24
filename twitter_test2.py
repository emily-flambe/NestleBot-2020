import tweepy
import os
from os import environ

def main():
    
    # get twitter auth creds
    CONSUMER_KEY = environ["TWITTER_CONSUMER_KEY"]
    CONSUMER_SECRET = environ["TWITTER_CONSUMER_SECRET"]
    ACCESS_TOKEN = environ["TWITTER_ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = environ["TWITTER_ACCESS_TOKEN_SECRET"]
    
    print(CONSUMER_KEY)
    print(CONSUMER_SECRET)
    print(ACCESS_TOKEN)
    print(ACCESS_TOKEN_SECRET)
    
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
        time.sleep(10)

if __name__ == "__main__":
    main()