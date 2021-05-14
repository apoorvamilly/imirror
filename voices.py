
from gtts import gTTS
import os
import platform
  

def playAudio(id):

    fileName = 'voices/' + str(id) + '.mp3'
    # Get the current operating sytem
    OS = platform.system()

    # Start command doesn't work on linux

    if OS == 'Linux':
        # Install mpg123 binaries on the system
        # sudo apt-get install mpg123
        os.system('mpg123 ' + fileName)
    else:
        os.system("start " + fileName)



def saveVoice(id):
    fileName = 'speeches/' + str(id) + '.txt'
        
    file = open(fileName, "r").read().replace(os.linesep, " ")
    # Here are converting in English Language  
    language = 'en' 

    speech = gTTS(text = str(file), lang = language, slow = False)
    speech.save("voices/" + str(id) + ".mp3")
    # os.system("start voice.wav")