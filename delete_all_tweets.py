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

import tweepy
from get_twitter_api import get_twitter_api

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