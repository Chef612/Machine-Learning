import cv2
import numpy as np
v=cv2.VideoCapture(0)
ta=0
count=0
while(1):
    r,i=v.read()
    hsv=cv2.cvtColor(i,cv2.COLOR_BGR2HSV)
    gl=np.array([65,50,55])
    gu=np.array([90,255,255])
    k=np.ones([8,8],'int')
    
    m=cv2.inRange(hsv,gl,gu)
    dil=cv2.dilate(m,k)
    res=cv2.bitwise_and(i,i,mask=m)
    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    gb=cv2.GaussianBlur(gray, (7,7), 0)
    mb=cv2.medianBlur(gb,3)
    t,ti=cv2.threshold(mb,32,255,0)
    
    cv2.imshow('bw',ti)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break
    
cv2.destroyAllWindows()
v.release() 
