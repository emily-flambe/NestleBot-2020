from nestlebot_functions import *

import time

def main():
    
    print("getting Twitter API")
    
    # get twitter auth creds
    CONSUMER_KEY = environ["TWITTER_CONSUMER_KEY"]
    CONSUMER_SECRET = environ["TWITTER_CONSUMER_SECRET"]
    ACCESS_TOKEN = environ["TWITTER_ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = environ["TWITTER_ACCESS_TOKEN_SECRET"]
    
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    
    # Create API object
    api = tweepy.API(auth)
    
    # set tweeting time interval
    #INTERVAL = 60 * 60 * 1  # tweet every 1 hour (prod)
    INTERVAL = 30  # every 30 seconds, for testing
    
    while True:
        
        print("Time to tweet - LFG")
        
        #get the freshest list of brands
        brand_list = get_brands()
        
        try:
            #get the image we're gonna tweet
            tweet_image_path, item = get_image(brand_list)
            
            #create and post the tweet
            generate_tweet(tweet_image_path, item, api)
            
            print("Tweeted!!! Back to sleep...")
        
        except:
            print("Tweet failed, RIP. Back to sleep...")
            raise
            pass
        
        #back to sleep zzzzzz
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
    