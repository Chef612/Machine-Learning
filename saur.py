import cv2
import numpy as np
v=cv2.VideoCapture(0)
X=[]
Y=[]
while(1):
    r,i=v.read()
    hsv=cv2.cvtColor(i,cv2.COLOR_BGR2HSV)
    gl=np.array([60,60,55])
    gu=np.array([90,255,255])
    k=np.ones([8,8],'int')
    m=cv2.inRange(hsv,gl,gu)
    dil=cv2.dilate(m,k)
    res=cv2.bitwise_and(i,i,mask=m)
    gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
    t,ti=cv2.threshold(gray,30,255,0)
    contours,h = cv2.findContours(ti,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    font=cv2.FONT_HERSHEY_SIMPLEX
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if(area>1000):
            m=cv2.moments(cnt)
            if(m['m00']!=0):
                x=int(m['m10']/m['m00'])
                y=int(m['m01']/m['m00'])
                cv2.circle(i,(x,y),5,(255,255,255),5)
                cv2.putText(i,'object',(x,y),font,1,(0))
                print(x,y)
                X.append(x)
                Y.append(y)
            
                



    cv2.imshow('frame',i)
    
    
    #cv2.imshow('hsv frame',hsv)
    #cv2.imshow('mask frame',m)
    #cv2.imshow('res frame',res)
    #cv2.imshow('gray frame',gray)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break

cv2.destroyAllWindows()
v.release()
