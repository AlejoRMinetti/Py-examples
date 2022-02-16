import cv2
import numpy as np

import matplotlib.pyplot as plt

# This function will plot images in the form of a grid with 1 row and 3 columns where images are placed in each column.
def plotImage(image):
    plt.figure()
    plt.imshow(image)
    plt.grid(False)
    plt.show()

def preprocessImage(input_image, height, width):
    plotImage(input_image)
    '''
    Given an input image, height and width:
    - Resize to height and width
    - Transpose the final "channel" dimension to be first
    - Reshape the image to add a "batch" of 1 at the start 
    '''
    # change dimension of each channel (w,h) oposite of reshape
    image = cv2.resize(input_image, (width, height))
    # change channel order from RGB to BGR 
    image = image.transpose((2,0,1))
    # reshape final with the batch dimension [1x3xHxW]
    image = image.reshape(1, 3, height, width)
    plotImage(image)
    return image

def pose_estimation(input_image):
    height=256
    width=456
    preposseced_img = preprocessImage(input_image, height, width)
    return preposseced_img


def text_detection(input_image):
    height=768
    width=1280
    preposseced_img = preprocessImage(input_image, height, width)
    return preposseced_img


def car_meta(input_image):
    height=72
    width=72
    preposseced_img = preprocessImage(input_image, height, width)
    return preposseced_img
