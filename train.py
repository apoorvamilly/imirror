import cv2
import os
import numpy as np
from PIL import Image

def trainDataset():
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

    def getImagesAndLabels(path):
        #get the paths of all the files in the folder
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        #create empth path list
        faceSamples=[]
        #create empty ID list
        Ids=[]
        #now looping through all the image paths and loading the IDs and the images
        for imagePath in imagePaths:
            #Updates in Code
            #ignore if the file does not have jpg extension
            if(os.path.split(imagePath)[-1].split(".")[-1]!='jpg'):
                continue
            #loading the image and converting it to grey scale
            pilImage=Image.open(imagePath).convert('L')
            #now we are converting PIL image to numpy array
            imageNp=np.array(pilImage,'uint8')
            #getting the id from the image
            Id=int(os.path.split(imagePath)[-1].split('.')[1][-1])
            #extraxt image from training image sample
            faces=detector.detectMultiScale(imageNp)
            #if a face is there then append that in the list as well as Id of it
            for (x,y,w,h) in faces:
                faceSamples.append(imageNp[y:y+h,x:x+w])
                Ids.append(Id)
        return faceSamples,Ids
    faces,Ids= getImagesAndLabels('dataset')
    recognizer.train(faces,np.array(Ids))
    recognizer.save('train.yml')