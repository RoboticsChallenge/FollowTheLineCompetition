from GUI import GUI
from HAL import HAL
from datetime import datetime
import cv2
import numpy as np

# lower boundary RED color range values; Hue (0 - 10)
start_time = datetime.now()
lower1 = np.array([0, 100, 20])
upper1 = np.array([10, 255, 255])

# upper boundary RED color range values; Hue (160 - 180)
lower2 = np.array([160,100,20])
upper2 = np.array([179,255,255])

def imageProccessing():
    image = HAL.getImage() 
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    result = hsv.copy()

    lower_mask = cv2.inRange(hsv, lower1, upper1)
    upper_mask = cv2.inRange(hsv, lower2, upper2)
    full_mask = lower_mask + upper_mask
    result = cv2.bitwise_and(result, result, mask=full_mask) #removes everything except our wanted colours 
    #GUI.showImage(result) #used for debugging

    h, s, gray = cv2.split(result) #to make HSV gray, use only last channel
    contours,hierarchy = cv2.findContours(gray, 1, cv2.CHAIN_APPROX_SIMPLE) #detects all shapes
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)  #magic conversion of image to mystical beeing
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00']) #finds center of mystical beeing
            cy = int(M['m01']/M['m00']) #finds center of mystical beeing
            #cv2.line(image,(cx,0),(cx,200),(255,0,0),1)
            #cv2.line(image,(0,cy),(1280,cy),(255,0,0),1)
            cv2.circle(image, (cx, cy), 7, (255, 255, 255), -1)
            cv2.drawContours(image, c, -1, (0,255,0), 1)
        else:
            cx = 0
            cy = 0
    else:
        cx = 0
        cy = 0

    GUI.showImage(image)
    return cx,cy

while True:
    #write program for steering car. imageProccessing will return x and y value for circle that tracks center line on image
    x, y = imageProccessing()
    HAL.setV(2) # to set the linear speed of car
    #HAL.setW(1) # to set the angular velocity of car

    print(datetime.now() - start_time) #adds timer to Console
