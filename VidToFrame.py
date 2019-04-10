# -*- coding: utf-8 -*-
"""
Credit to https://www.life2coding.com/extract-frame-video-file-using-opencv-python/
"""
#import library
import cv2
import os

#Define Function for extracting frames
def extractFrames(pathIn, pathOut):
    os.mkdir(pathOut)
 
    cap = cv2.VideoCapture(pathIn)
    count = 0
 
    while (cap.isOpened()):
 
        # Capture frame-by-frame
        ret, frame = cap.read()
 
        if ret == True:
            print('Read %d frame: ' % count, ret)
            cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  # save frame as JPEG file
            count += 1
        else:
            break
 
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    
def main():
    extractFrames('2019-04-10-101948-TIC-Video.mp4', 'test5')

if __name__=="__main__":
    main()