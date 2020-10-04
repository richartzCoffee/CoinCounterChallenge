import cv2
import numpy as np
import os

class CoinOpenCV():


    def __init__(self,folder:str,name_image:str ):
        """
        opens the image in the program, specifying
        the broken in the system until it
        """
        self.route = os.path.join(os.getcwd(),folder,name_image)
        self.image = cv2.imread(f"{self.route}",cv2.COLOR_BAYER_BG2GRAY)
        pass


    def turnToGray(self):
        """
        converts the image to gray scale
        """
        self.gray_image = cv2.cvtColor(self.image,cv2.COLOR_BGRA2GRAY)
        pass


    def blurryImage(self,blurry_type:bool = False):
        """
        blurry_type:bool = False
        
        filter to blur the image
        
        blurry_type chooses the mode, False,
        using the medium mode, and in True, used by the Gaussian

        """

        self.blurry_type = blurry_type
        if(blurry_type):
            self.blurry_image = cv2.GaussianBlur(self.gray_image, (3, 3), 0)
        else:
            self.blurry_image = cv2.blur(self.gray_image,(7,7))
        pass
    

    def imageThreshold(self,limit:int = 255,min:int = 10):
        """
        binarizes the image, leaving it in
        black and white

        """
        self.retval,self.image_threshold = cv2.threshold(self.blurry_image,min,limit, cv2.THRESH_BINARY_INV)

        pass

    def morphologicalTreatment(self):
        """
        applies morphological treatments to
        eliminate unwanted aspects

        """
        kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9))
        self.morphological_treatment_image = cv2.morphologyEx(self.image_threshold,cv2.MORPH_CLOSE,kernel_ellipse)
        pass


    def SimpleBlobDetector(self):
        """
        detect the circles left after the
        morphological treatments
        """

        self.params = cv2.SimpleBlobDetector_Params()
        self.params.filterByArea = True
        self.params.minArea = 1000
        self.params.maxArea = 12000
        self.params.filterByCircularity = True
        self.params.minCircularity = 0.5
        self.params.filterByConvexity = True
        self.params.minConvexity = 0.9
        self.params.filterByInertia = True
        self.params.minInertiaRatio = 0.7
        self.params.minDistBetweenBlobs = 10
        self.params.filterByColor = False

        detector = cv2.SimpleBlobDetector_create(self.params)
        self.keipoint = detector.detect(self.morphological_treatment_image)

        pass


    def saveImage(self, folder:str, name_image:str):
        """
        folfer: destination folder name
        name_image: final image name

        save the image in the destination folder
        """
        real_result_local = os.path.join(os.getcwd(),folder,name_image)
        cv2.imwrite(f"{real_result_local}", self.image_draw)
        pass


    def detectCircle(self):
        """
        detects circles using the
        HoughCircles function
        """

        self.keipoint = cv2.HoughCircles(self.blurry_image,
                        cv2.HOUGH_GRADIENT,1,param1=100,param2=60,
                        minRadius=0,maxRadius=0,minDist=80)
        
        pass

    def drawDetectedCircle(self,type_keitpont:bool = False):
        """
        type_keitpont: if you have used the
        SimpleBlobDetector mode, you must enter
        the True value as input, due to the use
        of the detect function

        desenha os círculos detectados anteriormente
        """

        self.image_draw = self.image

        if(type_keitpont):

            for keyPoint in self.keipoint:
                #draw the circle
                cv2.circle(self.image_draw, (np.uint16(keyPoint.pt[0]), np.uint16(keyPoint.pt[1])),np.uint16(keyPoint.size/2),(0, 255 ,0),2)
                #mark the center
                cv2.circle(self.image_draw, (np.uint16(keyPoint.pt[0]), np.uint16(keyPoint.pt[1])),2,(0,0,255),3)

        else:

            self.circles = np.uint16(np.around(self.keipoint))

            for i in self.circles[0, :]:
                #draw the circle
                cv2.circle(self.image_draw, (i[0],i[1]),i[2],(0, 255 ,0),2)

                #mark the center
                cv2.circle(self.image_draw, (i[0],i[1]),2,(0,0,255),3)
        pass


    def presentImages(self,version:bool = False):
        """
        represent the images. if you used the
        binarization method, to show the images
        related to that part, the version parameter
        must be set to True
        """
        cv2.imshow('original_Image',cv2.imread(f"{self.route}"))
        cv2.imshow('Gray_Image',self.gray_image)
        cv2.imshow('blurrt_Image',self.blurry_image)

        if(version):
            cv2.imshow('Threshold_Image',self.image_threshold)
            cv2.imshow('morphological_treatment_Image',self.morphological_treatment_image)
        
        cv2.imshow("final image",self.image_draw)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        pass


    def numberOfCoins(self,dolar:bool = False):
        """
        
        Inform the number of coins we have in the image
        """
        if(dolar):
            return len(self.keipoint)
        else:
            return len(self.circles[0,:])
        pass