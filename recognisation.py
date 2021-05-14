import cv2
import numpy as np
import time


def faceRecog():
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('train.yml')

    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    cam = cv2.VideoCapture(0)

    font = cv2.FONT_HERSHEY_SIMPLEX

    isFaceRecognized = False

    # Set a delay of 2 seconds so that the camera gets enough time to get ready
    time.sleep(2)

    timeout = time.time() + 5

    # Loop till face is recognized
    while not isFaceRecognized:
        ret, im = cam.read()

        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray,1.2,5)

        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            name = 'Unknown'
            if(conf<50):
                # Set the faceRecognized as true
                # isFaceRecognized = True
                if(Id==1):
                    name="King"
                elif(Id==2):
                    name="shally "
                elif(Id==3):
                    name="aahhh"         
                cam.release()
                cv2.destroyAllWindows()
                return name, Id
            else:
                name="Unknown"

            # The timeout window
            if(time.time() > timeout):
                cam.release()
                cv2.destroyAllWindows()
                return name, Id


            cv2.putText(im, str(name), (x,y-40), font, 1, (255,255,255), 3)
            im=cv2.resize(im,(600,400))
            cv2.imshow('im',im)
            
            if cv2.waitKey(10) & 0xFF==ord('q'):
                break
    cam.release()
    # cv2.waitKey(0)
    cv2.destroyAllWindows()