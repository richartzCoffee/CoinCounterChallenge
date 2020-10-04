import cv2
import numpy as np
import os


def CoinReal():
    """

    """

    local = os.path.join(os.getcwd(),"image","real_original.jpg")
    image_original = cv2.imread(f"{local}")

    image_gray = cv2.imread(f"{local}",cv2.IMREAD_GRAYSCALE)

    image_blurry = cv2.blur(image_gray,(7,7))

    cv2.imshow('image_b',image_blurry)

    circles = cv2.HoughCircles(image_blurry, cv2.HOUGH_GRADIENT,1,param1=100,param2=60,minRadius=0,maxRadius=0,minDist=80)
    circle = np.uint16(np.around(circles))


    for i in circle[0, :]:
        img = cv2.circle(image_original, (i[0],i[1]),i[2],(0, 255 ,0),2)


    cv2.imshow('imag',img)
       

    cv2.waitKey(0)
    
    real_result_local = os.path.join(os.getcwd(),"image_result"," real_result.jpg")

    cv2.imwrite(f"{real_result_local}", img)

    cv2.destroyAllWindows()