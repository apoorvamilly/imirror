import dataset
import recognisation
import speech
import voiceInput
from train import trainDataset
import voices
import weather
import _thread


# TODO: A menu system
menu = {
    "fail": "Face not identified",
    "tryAgain": "Say retry to try again",
    "register": "Say register to register as a new face",
}


_thread.start_new_thread(weather.showWeather, ())
def run():
    # As a default, let the camera identify the user
    # Check if the user exists
    name, Id = recognisation.faceRecog()

    if(name == 'Unknown'):
        def runMenu():
            speech.SpeakText(menu['fail'])
            speech.SpeakText(menu['tryAgain'])
            speech.SpeakText(menu['register'])

            # Get the voice from the user
            input = voiceInput.getVoice()
            print(input)
            
            # If the user is not identified, ask the user to try again or register as a new user
            if(input == 'retry'):
                run()
            elif(input == 'register'):
                # Ask the user to register as a new face and train the datasets
                print('register option selected')
                dataset.register()
                trainDataset()
                run()
            else:
                speech.SpeakText('Wrong option. Please try again')
                # Call the same function if a wrong option is selected
                runMenu()

        runMenu()

    else:
        # If the user exists, welcome him by speaking his / her name
        # Then ask him if he wants to know his pending tasks or if he wants to add new ones
        speech.SpeakText('welcome ' + ' ' + name)

        def doUserInteractions():
            speech.SpeakText('Say add to add new tasks')
            speech.SpeakText('Say list to know your pending tasks')
            speech.SpeakText('Say exit to quit')

            # Get the voice from the user
            command = voiceInput.getVoice()

            if(command == 'ad' or command == 'add'):
                # TODO: Add new task
                print('Add new task here')
                def addNewTask():
                    speech.SpeakText('State the tasks that you want to add')

                    # Get the voice from the user
                    task = voiceInput.getVoice()

                    speech.writeToFile(Id, task)
                    speech.SpeakText('Do you want to add more tasks?')

                    input = voiceInput.getVoice()

                    if(input == 'yes'):
                        addNewTask()
                    else:
                        # save this text file as mp3
                        voices.saveVoice(Id)
                        doUserInteractions()

                addNewTask()

                    
            
            elif(command == 'list'):
                # TODO: List the user's task
                print('List the user tasks')
                speech.SpeakText('The following are your tasks for the day')
                voices.playAudio(Id)
                doUserInteractions()
            
            elif(command == 'quit' or command == 'exit'):
                return 0

            else:
                # TODO: wrong option
                speech.SpeakText('You chose the wrong option')
                doUserInteractions()

        doUserInteractions()
        
    
run()