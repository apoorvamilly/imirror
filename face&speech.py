import cv2
import numpy as np
import _thread
import speech_recognition as sr
import pyttsx3
from gtts import gTTS  
import os

flag=0

r = sr.Recognizer() 
def recog():
    
    while(1):
        
        
      
        # Exception handling to handle
        # exceptions at the runtime
        try:
            
            file = open("speech.txt","a")
              
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                  
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level 
                r.adjust_for_ambient_noise(source2, duration=0.1)
                  
                #listens for the user's input 
                audio2 = r.listen(source2)
                  
                # Using ggogle to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print(MyText)
                

               
               
                file.write(MyText)
               
               
                  
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
              
        except sr.UnknownValueError:
            print("unknown error occured") 


def txt():
    while(1):
        
            
        file = open("speech.txt", "r").read().replace("\n", " ")
        language = 'en' 

        speech = gTTS(text = str(file), lang = language, slow = False)
        speech.save("voice.wav")
        os.system("start voice.wav")

    

_thread.start_new_thread(recog ,())






recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('train.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    
    ret, im = cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray,1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
        if(conf<50):
            if(Id==1):
                Id="milly"
                if(flag==0):
                    txt()
                    flag=1
                    
                
            elif(Id==2):
                Id="shally "
               
            elif(Id==3):
                Id="aahhh"
                
        else:
            Id="Unkown"
            flag=0
        cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)
        im=cv2.resize(im,(600,400))
        cv2.imshow('im',im)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
cam.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
