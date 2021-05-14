import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

def getVoice():
    while(1):

        # Exception handling to handle
        # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source, duration=0.5)

                # listens for the user's input
                audio2 = r.listen(source)

                # Using ggogle to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                
                print(MyText)
                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")
