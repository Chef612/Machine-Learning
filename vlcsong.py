import time
import cv2,vlc
v=cv2.VideoCapture(0)
m=vlc.MediaPlayer(r'C:\Users\KIIT\Dropbox\Dropbox\My PC (SOUVIK)\Desktop\songs\Alan Walker ‒ Darkside ft. Au Ra & Tomine Harket.mp3')
fd=cv2.CascadeClassifier(r'C:\Users\KIIT\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_eye.xml')
time.sleep(3)
m.play()
flag=1
while(1):
    r,i=v.read()
    l=i[::,::-1,::]
    gray=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(gray,1.3,5)
    for x,y,w,h in f:
        print(x,y)
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,255,0),2)
        
    if(len(f)>0):
        m.play()
        flag=0
    elif(flag==0):
        m.pause()
        flag=1
    cv2.imshow('face',i)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        m.stop()
        break
cv2.destroyAllWindows()
v.release
