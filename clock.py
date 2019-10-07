#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:43:45 2019

@author: pengzijun
"""

import cv2
import numpy as np
import time
import math
def getEndPosition(i,length):
    x=(int)(length*r*math.sin(alpha*i))
    y=(int)(length*r*math.cos(alpha*i+math.pi))
    return x,y
def getClockPannel():
    img=np.zeros([size,size,3])
    for i in range(0,60):
        x,y=getEndPosition(i,0.9)
        
        if(i%5==0):
             x1,y1=getEndPosition(i,0.8)
             cv2.line(img, (r+x1, r+y1), (r+x,r+y), white, 8)
        else:
             x1,y1=getEndPosition(i,0.85)
             cv2.line(img, (r+x1, r+y1), (r+x,r+y), white, 4)
            
            
    return img
white=(255,255,255)
size=1024
r=(int)(size/2)
alpha=2*math.pi/60
i=0

while(True):
    img=getClockPannel()
    currentTime=time.strftime('%H:%M:%S',time.localtime(time.time()))
    print(currentTime)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, currentTime, (r-100, r-100), font, 2, white, 2, lineType=cv2.LINE_AA)

    current_split=currentTime.split(":")
    hour=int(current_split[0])%12
    mintue=int(current_split[1])
    second=int(current_split[2])
    cv2.circle(img, (r, r), r, white, 1)
    x,y=getEndPosition(second,0.7)
    cv2.line(img, (r, r), (r+x,r+y), white, 2)
    x,y=getEndPosition(mintue,0.6)
    cv2.line(img, (r, r), (r+x,r+y), white, 4)
    x,y=getEndPosition(5*hour,0.5)
    cv2.line(img, (r, r), (r+x,r+y), white, 8)
    cv2.imshow("test",img)
    if(cv2.waitKey(30)==ord('q')):
        cv2.destroyAllWindows()
        break
    
    

