# import packages
from imutils.object_detection import non_max_suppression
import numpy as np
import argparse
import time
import cv2
import detect_text as dt

def main():
    
    print("it's running wow")
    
    #this is a photo of me with my favorite chicken. Her name is Spoopy. I love her. She is not text.
    spoopy_pic="images/spoopy.jpg"
    spoopy_result = dt.detect_text_from_image(spoopy_pic)
    print(f"Does {spoopy_pic} contain text? {spoopy_result}")
    
    #this is a photo of a can of Carnation - a deity in the pantheon of horrible Nestle products. It has text.
    carnation_pic="images/nestle_carnation.jpg"
    carnation_result = dt.detect_text_from_image(carnation_pic)
    print(f"Does {carnation_pic} contain text? {carnation_result}")

if __name__ == "__main__":
    main()
    