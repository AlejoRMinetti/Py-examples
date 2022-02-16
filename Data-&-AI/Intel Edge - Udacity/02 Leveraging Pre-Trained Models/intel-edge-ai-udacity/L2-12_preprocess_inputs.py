import cv2
import numpy as np

def reshape_img(image, height, width):
    '''
    Given an input image of shape WxHxC, this function will reshape it to
    the shape BxCxHxW, where:
    
    B - batch size
    C - number of channels
    H - image height
    W - image width
    
    Expected image shape: WxHxC; e.g. [750, 1000, 3]
    Expected colour order: BGR
    
    Output shape: BxCxHxW; e.g. [1, 3, 256, 456]
                  --> if H = 256, W = 456
    '''
    
    # resize image to desired width and height
    # get width before height because OpenCV messes things up...sadly
    image = cv2.resize(image, (width, height) )
    
    # transpose image to make channel the first dimension
    image = image.transpose((2,0,1))
    
    # reshape image as BxCxHxW
    # batch size is 1 because we are dealing with a single image
    image = image.reshape(1, image.shape[0], height, width)
    
    return image
    

def pose_estimation(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related pose estimation model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    #preprocessed_image = np.copy(input_image)

    # TODO: Preprocess the image for the pose estimation model
    preprocessed_image = reshape_img(input_image, 256, 456)

    return preprocessed_image


def text_detection(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related text detection model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    #preprocessed_image = np.copy(input_image)

    # TODO: Preprocess the image for the text detection model
    preprocessed_image = reshape_img(input_image, 768, 1280)
    
    
    return preprocessed_image


def car_meta(input_image):
    '''
    Given some input image, preprocess the image so that
    it can be used with the related car metadata model
    you downloaded previously. You can use cv2.resize()
    to resize the image.
    '''
    #preprocessed_image = np.copy(input_image)

    # TODO: Preprocess the image for the car metadata model
    preprocessed_image = reshape_img(input_image, 72, 72)
    
    return preprocessed_image
