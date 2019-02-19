# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:23:20 2018

@author: Reaper124
"""
#Import OpenCV library
import cv2, time

#Sets cam variable as initial camera, change if you have multiple webcams
cam = cv2.VideoCapture(0)
#Names the window for the camera feed
cv2.namedWindow("Camera Feed")

#set img_counter variable to start at 0
img_counter = 0
#modify total_count variable to max amount of pics to capture
total_count = 5

#key value
cam.set(3 , 640  ) # width        
cam.set(4 , 480  ) # height       
cam.set(10, 120  ) # brightness     min: 0   , max: 255 , increment:1  
cam.set(11, 50   ) # contrast       min: 0   , max: 255 , increment:1     
cam.set(12, 70   ) # saturation     min: 0   , max: 255 , increment:1
cam.set(13, 13   ) # hue         
cam.set(14, 50   ) # gain           min: 0   , max: 127 , increment:1
cam.set(15, -3   ) # exposure       min: -7  , max: -1  , increment:1
cam.set(17, 5000 ) # white_balance  min: 4000, max: 7000, increment:1
cam.set(28, 0    ) # focus          min: 0   , max: 255 , increment:5

while True:
    ret, frame = cam.read()
    cv2.imshow("Cam Frame",frame)
    if not ret:
        break
    k =cv2.waitKey(1)
    
    if k%256 == 27:
        print("Escape")
        break
    elif k%256 == 32:
        #space key pressed
        while img_counter < total_count:
            ret, frame = cam.read()
            cv2.imshow("Cam Frame",frame)
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            time.sleep(5) #modify for time between image capture
            
cam.release()
cv2.destroyAllWindows()

    
