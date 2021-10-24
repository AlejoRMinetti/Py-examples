from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test")
    imshow("cam-test",img)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("PicExample.jpg",img) #save image