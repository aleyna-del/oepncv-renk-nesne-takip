import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    # Görüntü frame'i al
    _, frame = cap.read()
    # HSV uzayina donustur
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Mavi rengin HSV uzayindaki araligi
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # HSV icindeki mavi rengi tespit edebilmek icin threshold
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND islemi ve mask uygulaniyor
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()