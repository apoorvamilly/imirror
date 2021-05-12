import cv2
import os
cam=cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
num=input('enter our ID : ') 
sampleNum=0
while True:
    pwd=os.getcwd()
    ret,im=cam.read()
    if not ret:
        print(ret)
        break
    imgray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    cv2.imshow('FACE',im)
    faces=detector.detectMultiScale(imgray,1.3,5)
    for (x,y,w,h) in faces:
        sampleNum+=1
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        patch=imgray[y:y+h,x:x+w]
        os.chdir(pwd+'/dataset')
        cv2.imwrite('user.' +num+'.' +str(sampleNum)+ '.jpg',patch)
        os.chdir(pwd)
        cv2.imshow('FACES',im)
        
    if cv2.waitKey(100)&0xFF==ord('q') or sampleNum>=300:
        break
cam.release()
cv2.destroyAllWindows()