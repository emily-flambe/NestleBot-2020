# -*- coding: utf-8 -*-
"""
SOURCE: https://gist.github.com/davej/113241

This script will delete all of the tweets in the specified account.
You may need to hit the "more" button on the bottom of your twitter profile
page every now and then as the script runs, this is due to a bug in twitter.
You will need to get a consumer key and consumer secret token to use this
script, you can do so by registering a twitter application at https://dev.twitter.com/apps
@requirements: Python 3+, Tweepy (http://pypi.python.org/pypi/tweepy/1.7.1)
@author: Dave Jeffery
"""

from os import environ
import tweepy

def get_twitter_api():
    
    '''
    Returns an API object to do Twittering
    
    Input: none BAYBEE
    Output: returns API object
    '''
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

def batch_delete(api):
    print("You are about to Delete all tweets from the account @%s." % api.verify_credentials().screen_name)
    print("Does this sound ok? There is no undo! Type yes to carry out this action.")
    do_delete = input("> ")
    if do_delete.lower() == 'yes':
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
                print("Deleted:", status.id)
            except:
                print("Failed to delete:", status.id)

if __name__ == "__main__":
    api = get_twitter_api()
    print("Authenticated as: %s" % api.me().screen_name)
    
    batch_delete(api)