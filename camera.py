import cv2
import time
import numpy as np
v=cv2.VideoCapture(0)
time.sleep(2)
r,j=v.read()
while(1):
    r,i=v.read()
    k=j-i
    l=k[::,::-1,::]
    g=cv2.cvtColor(l,cv2.COLOR_BGR2GRAY)
    u,bw=cv2.threshold(g,80,255,1)
    '''p=np.count_nonzero(bw)
    print(p)'''
    '''j=i.copy()
    k=j[100:200,100:200]
    i[300:400,300:400]=k
    cv2.circle(i,(100,200),20,(0,0,255),5)
    cv2.rectangle(i,(100,100),(200,200),(0,255,0),5)'''
    #cv2.imshow('my image',i)
    #cv2.imshow('hello',k)
    cv2.imshow('my image',l)
    #cv2.imshow('new',k)
    k1=cv2.waitKey(1)
    if(k1==99):
        break
cv2.destroyAllWindows()
v.release()

