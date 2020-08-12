import cv2
import time
v=cv2.VideoCapture(0)
plates_cascade=cv2.CascadeClassifier(r'C:\Users\KIIT\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\cv2\data\haarcascade_russian_plate_number.xml')
#cv2.imshow('bg',bg)
while(1):
    r,i=v.read()
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=plates_cascade.detectMultiScale(gray,1.2,4)
    print(len(f))
    for x,y,w,h in f:

        #i[y:y+h,x:x+w]=bg[y:y+h,x:x+w]
       cv2.rectangle(i,(x-20,y-20),(x+w+30,y+h+30),(255,0,0), 2)
       cv2.imshow('plates',i[y-20:y+h+30,x-20:x+w+30])
       
    
    cv2.imshow('face',i)
    #cv2.imshow('a',gray)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break

cv2.destroyAllWindows()
v.release()
