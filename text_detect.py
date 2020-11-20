# import packages
from imutils.object_detection import non_max_suppression
import numpy as np
import argparse
import time
import cv


'''


def detect_text(path_to_image):
    
    
    #Input: path_to_image (file path to image, e.g. "images/spoopy.jpg")
    #Output: boolean ('True' if text was detected in image)
    #Sample usage:
    #
    #path_to_image="images/spoopy.jpg"
    #detect_text(path_to_image)
    #
    #source code for EAST text detection strats: https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/
    
    
    
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
    
    #return boolean True if "boxes" contains anything (ie. text was detected in the image)
    return len(boxes)>0
'''
    
    
def main():
    
    print("it's running wow")
    
    '''
    #this is a photo of me with my favorite chicken. Her name is Spoopy. I love her. She is not text.
    path_to_image="images/spoopy.jpg"
    result = detect_text(path_to_image)
    print(f"Does {path_to_image} contain text? {result}")
    '''
if __name__ == "__main__":
    main()
    