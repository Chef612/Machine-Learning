import cv2
import time
import numpy as np
v=cv2.VideoCapture(0)
time.sleep(2)
c=cv2.imread(r'cat.png')
sh=c.shape
r,j=v.read()
while(1):
    r,i=v.read()
    l=i[::,::-1,::]
    '''g=cv2.cvtColor(l,cv2.COLOR_BGR2GRAY)
    u,bw=cv2.threshold(g,80,255,1)'''
    l[10:10+sh[0],10:10+sh[1]]=c
    cv2.imshow('my image',l)
    #cv2.imshow('new',k)
    k1=cv2.waitKey(1)
    if(k1==99):
        break
cv2.destroyAllWindows()
v.release()

