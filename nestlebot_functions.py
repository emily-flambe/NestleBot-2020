from google_images_search import GoogleImagesSearch
from imutils.object_detection import non_max_suppression
from os import environ
import argparse
import cv2
import glob
import numpy as np
import os
import random
import re
import requests
import sys
import time
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


def google_image_search(search_term, num_images):
    
    '''
    Conducts a google image search using the custom search engine I set up: https://cse.google.com/cse?cx=61bc008d6464ccf10

    Input: search_term (like 'benefiber'), num_images
    Output: downloads num_images number of images to local directory "images/{search_term}"
    '''
    
    
    # get GCS API key and CX id from environment variables
    GCS_DEVELOPER_KEY=os.getenv("GCS_DEVELOPER_KEY")
    GCS_CX=os.getenv("GCS_CX")
    
    # create GoogleImagesSearch object
    gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
        
    # define search params:
    _search_params = {
         'q': 'nestle food '+search_term
        ,'num': num_images
        ,'imgType': 'photo'
        ,'fileType': 'jpg'
        ,'imgSize': 'MEDIUM',
    }
        
    #create or empty target directory (where we will be saving images from Google Image Search)
    if not os.path.exists(f"images/{search_term}"):
        print(f"creating folder images/{search_term}...")
        os.makedirs(f"images/{search_term}")
    
    else:
        print(f"folder images/{search_term} already exists - clearing contents...")
        files = glob.glob(f"images/{search_term}/*")
        for f in files:
            os.remove(f)
            
    # generate path for image download
    download_path=os.getcwd()+'/images/'+search_term
    
    # search, download, and resize:
    gis.search(search_params=_search_params
               , path_to_dir=download_path
               , width=300
               , height=300)
    
    
def detect_text(path_to_image):
    
    '''
    
    Detects whether an image contains text. TODO: Make this into an API using Flask? Why the hell not?
    
    Input: path_to_image (file path to image, e.g. "images/spoopy.jpg")
    Output: boolean ('True' if text was detected in image)

    Sample usage:
    
    path_to_image="images/spoopy.jpg"
    detect_text(path_to_image)
    
    source code for EAST text detection strats: https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/
    '''
    
    
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", type=str, default=path_to_image, help="path to input image")
    ap.add_argument("-east", "--east", type=str, default="east/frozen_east_text_detection.pb", help="path to input EAST text detector")
    ap.add_argument("-c", "--min-confidence", type=float, default=0.5, help="minimum probability required to inspect a region")
    ap.add_argument("-w", "--width", type=int, default=320, help="resized image width (should be multiple of 32)")
    ap.add_argument("-e", "--height", type=int, default=320, help="resized image height (should be multiple of 32)")
    args = vars(ap.parse_args(args=[]))
    
    # load the input image and grab the image dimensions
    image = cv2.imread(args["image"])
    orig = image.copy()
    (H, W) = image.shape[:2]
    
    # set the new width and height and then determine the ratio in change
    # for both the width and height
    (newW, newH) = (args["width"], args["height"])
    rW = W / float(newW)
    rH = H / float(newH)

    # resize the image and grab the new image dimensions
    image = cv2.resize(image, (newW, newH))
    (H, W) = image.shape[:2]
    
    # define the two output layer names for the EAST detector model that
    # we are interested -- the first is the output probabilities and the
    # second can be used to derive the bounding box coordinates of text
    layerNames = ["feature_fusion/Conv_7/Sigmoid","feature_fusion/concat_3"]
    
    # load the pre-trained EAST text detector
    net = cv2.dnn.readNet(args["east"])
    
    # construct a blob from the image and then perform a forward pass of
    # the model to obtain the two output layer sets
    blob = cv2.dnn.blobFromImage(image, 1.0, (W, H), (123.68, 116.78, 103.94), swapRB=True, crop=False)
    net.setInput(blob)
    (scores, geometry) = net.forward(layerNames)
    
    # grab the number of rows and columns from the scores volume, then
    # initialize our set of bounding box rectangles and corresponding
    # confidence scores
    (numRows, numCols) = scores.shape[2:4]
    rects = []
    confidences = []
    
    # loop over the number of rows
    for y in range(0, numRows):
        # extract the scores (probabilities), followed by the geometrical
        # data used to derive potential bounding box coordinates that
        # surround text
        scoresData = scores[0, 0, y]
        xData0 = geometry[0, 0, y]
        xData1 = geometry[0, 1, y]
        xData2 = geometry[0, 2, y]
        xData3 = geometry[0, 3, y]
        anglesData = geometry[0, 4, y]
    
        # loop over the number of columns
        for x in range(0, numCols):
            # if our score does not have sufficient probability, ignore it
            if scoresData[x] < args["min_confidence"]:
                continue
    
            # compute the offset factor as our resulting feature maps will
            # be 4x smaller than the input image
            (offsetX, offsetY) = (x * 4.0, y * 4.0)
    
            # extract the rotation angle for the prediction and then
            # compute the sin and cosine
            angle = anglesData[x]
            cos = np.cos(angle)
            sin = np.sin(angle)
    
            # use the geometry volume to derive the width and height of
            # the bounding box
            h = xData0[x] + xData2[x]
            w = xData1[x] + xData3[x]
    
            # compute both the starting and ending (x, y)-coordinates for
            # the text prediction bounding box
            endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
            endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
            startX = int(endX - w)
            startY = int(endY - h)
    
            # add the bounding box coordinates and probability score to
            # our respective lists
            rects.append((startX, startY, endX, endY))
            confidences.append(scoresData[x])
            
    # apply non-maxima suppression to suppress weak, overlapping bounding
    # boxes
    boxes = non_max_suppression(np.array(rects), probs=confidences)
    
    #return boolean (True if "boxes" contains anything, ie. text was detected in the image)
    return len(boxes)>0




def get_brands():
    '''
    get_brands()
    
    purpose: get the freshest data from Charles Stover's github repo (peoplecott)
    input: none
    output: list of brand/product names
    '''
    
    url='https://raw.githubusercontent.com/CharlesStover/peoplecott/master/src/constants/children/children.ts'
    brands_raw_file = requests.get(url).text

    # idk how .ts files work but we can use regex to extract the brand names from it

    #get horrible nasty raw list of all rows in the file that match any of the patterns
    re1 = re.compile(r'([A-Z]+)+:', re.IGNORECASE) #text before a semicolon
    re2 = re.compile(r'"([^"]*)"', re.IGNORECASE)  #text between double quotes
    re3 = re.compile(r"'([^']*)'", re.IGNORECASE)  #text between single quotes
    raw_list = re.findall(re1, brands_raw_file)+re.findall(re2, brands_raw_file)+re.findall(re3, brands_raw_file)
    
    #clean up the riff-raff
    exclude_list = ["http","nestle","\"",",",".","parent","source","child","carpathia"] #exclude carpathia because it keeps returning pictures of a damn ship
    clean_list=[]
    for mystr in raw_list:
        if all(x.upper() not in mystr.upper() for x in exclude_list):
            clean_list.append(mystr)
    
    return clean_list


def get_image(clean_list):

    '''    
    purpose: select an item name and an image to tweet about
    input: clean_list (output from get_brands())
    output: item name (e.g., Nesquik) and path to image file to tweet
    '''
    
    tweet_valid=False
    
    while tweet_valid==False:
        # Choose a random item from the list
        index_to_use = random.randint(0,len(clean_list))
        item = clean_list[index_to_use]
        
        # Retrieve N google image results of that item
        num_images = 5
        print(f"getting {num_images} images of {item}")
        google_image_search(item, num_images)
        
        # Randomly select one of the remaining images
        # Check to make sure the image contains text. If it does not, delete the file and try again
        
        image_dir=f"images/{item}"
        image_files = glob.glob(f"{image_dir}/*")
        
        image_valid = False
        
        while image_valid == False:
            
            image_file_index_to_use = random.randint(0,len(image_files))
            tweet_image_path=image_files[image_file_index_to_use]
            
            print(f"Selected image {tweet_image_path} - checking to make sure it includes text...")
            
            try:
                image_has_text=detect_text(tweet_image_path) #sometimes the google image search function downloads a null image
                if image_has_text:
                    print(f"Image contains text, good for the tweetening.")
                    image_valid = True
                else:   
                    os.remove(tweet_image_path)
            except:
                os.remove(tweet_image_path)
        
        tweet_valid = True
        
        return tweet_image_path, item

def generate_tweet(tweet_image_path, item, api):
        
    '''    
    purpose: craft and send a new tweet
    input: item name (e.g., Nesquik) and path to image file to tweet (output from get_image) and twitter api object
    output: posts the tweet; nothing returned
    '''
    
    # Upload image to Twitter
    print(f"uploading {tweet_image_path} to Twitterspace")
    media = api.media_upload(tweet_image_path)
    
    # Post tweet with image
    print("Tweeting!")
    randint = random.randint(1,1000)
    tweet = f"Have you heard about {item}? It's a bullshit product by the bullshit company Nestle. Reminder #{randint} not to purchase this. Thanksx"
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])

    