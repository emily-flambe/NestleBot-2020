from nestlebot_functions import *

import time
import random

def main():
    
    
    print("getting Twitter API")
    api = get_twitter_api()
    
    while True:
        
        print("attempting to Tweet")
        randint = random.randint(1,1000)
        tweet = f"Test tweet #{randint}"
        post_result = api.update_status(status=tweet)
        print("tweet success")
        time.sleep(10)


if __name__ == "__main__":
    main()
    