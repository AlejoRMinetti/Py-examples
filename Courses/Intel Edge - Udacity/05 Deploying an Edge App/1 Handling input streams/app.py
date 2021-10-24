import argparse
import cv2
import numpy as np

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Handle an input stream")
    # -- Create the descriptions for the commands
    i_desc = "The location of the input file"

    # -- Create the arguments
    parser.add_argument("-i", help=i_desc, default = "blue-card.jpg")
    args = parser.parse_args()

    return args


def capture_stream(args):
    ### TODO: Handle image, video or webcam
    isSingleImg = False
    if args.input.find(".jpg") != -1 or args.input.find(".png") != -1:
        input_stream = args.input
        isSingleImg = True
    if args.input.find(".mp4") != -1:
        input_stream = args.input
    else:
        input_stream = 0 # for system camera

    capture = cv2.VideoCapture(input_stream)
    
    ### Get and open video capture
    capture.open(args.input)

    while capture.isOpened():
        flag, frame = cap.read()
        if not flag:
            break
        
        # check for Escape for exit
        key_pressed = cv2.waitKey(60) 
        if key_pressed == 27: 
            break

        ### Re-size the frame to 100x100
        image = cv2.resize(frame, (100,100))


        ### Add Canny Edge Detection to the frame, 
        ###       with min & max values of 100 and 200
        ###       Make sure to use np.dstack after to make a 3-channel image
        edges = cv2.Canny(image,100,200)


        ### Write out the frame, depending on image or video
        if isSingleImg == True:
            cv2.imwrite('output.jpg', edges) # for single image
        else:
            cv2.imshow('display', edges) # for video

    ### Close the stream and any windows at the end of the application
    capture.release()
    cv2.destroyAllWindows()

def main():
    args = get_args()
    capture_stream(args)


if __name__ == "__main__":
    main()

# TEST:
# python app.py -i blue-car.jpg
# python app.py -i test_video.mp4