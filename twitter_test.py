from nestlebot_functions import *

import time
import random

def main():
    
    print("getting Twitter API")
    api = get_twitter_api()
    
    randint = random.randint(1,1000)
    tweet = f"Test tweet #{randint}"
    post_result = api.update_status(status=tweet)


if __name__ == "__main__":
    main()
    