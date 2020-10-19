**Make your face invisible**


import cv2
import time
v=cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(r'C:\Users\KIIT\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
time.sleep(3)
for r in range(60):
    r,bg=v.read()
#cv2.imshow('bg',bg)
while(1):
    r,i=v.read()
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(gray,1.1,7)
    for x,y,w,h in f:

        i[y-30:y+h+30,x-30:x+w+30]=bg[y-30:y+h+30,x-30:x+w+30]
        #cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0), 2)
        
    
    cv2.imshow('face',i)
    #cv2.imshow('a',gray)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break

cv2.destroyAllWindows()
v.release()
