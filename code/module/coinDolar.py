import cv2
import numpy as np
import os


def CoinDolar():

    local = os.path.join(os.getcwd(),"image","dolar_original.png")
    
    img1 = cv2.imread(f"{local}",cv2.COLOR_BAYER_BG2GRAY)

    img = cv2.cvtColor(img1, cv2.COLOR_BGRA2GRAY)

    cv2.imshow("o1",img1)
    cv2.imshow("o",img)

    te = cv2.GaussianBlur(img, (3, 3), 0) # aplica blur 

    retval,nova = cv2.threshold(te,65,255, cv2.THRESH_BINARY_INV)
    cv2.imshow("nova",nova)

    kenel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))

    erode1 = cv2.morphologyEx(nova,cv2.MORPH_CLOSE,kenel)


    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 1000
    params.maxArea = 12000
    params.filterByCircularity = True
    params.minCircularity = 0.5
    params.filterByConvexity = True
    params.minConvexity = 0.9
    params.filterByInertia = True
    params.minInertiaRatio = 0.7
    params.minDistBetweenBlobs = 10
    params.filterByColor = False

    detector = cv2.SimpleBlobDetector_create(params)

    keipoint = detector.detect(erode1)

    cv2.imshow("ok",erode1)

    im_with_keypoints = cv2.drawKeypoints(img1, keipoint, np.array([]), (0, 255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Display result
    cv2.imshow("Keypoints", im_with_keypoints)

    print(len(keipoint))

    cv2.waitKey(0)

    real_result_local = os.path.join(os.getcwd(),"image_result"," dolar_result.png")

    cv2.imwrite(f"{real_result_local}", im_with_keypoints)

    cv2.destroyAllWindows()