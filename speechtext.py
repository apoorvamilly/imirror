import speech_recognition as sr
import pyttsx3
import tkinter as tk
import time
  
# Initialize the recognizer 
r = sr.Recognizer() 

      
# Loop infinitely for user to

def SpeakText(command):
    
      
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()





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
            r.adjust_for_ambient_noise(source2, duration=0.2)
              
            #listens for the user's input 
            audio2 = r.listen(source2)
              
            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print(MyText)
            
  
           
           
            file.write(MyText)
            SpeakText(MyText)
           
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")


