from tracemalloc import Snapshot
from unicodedata import name
import cv2
import time
import random
import dropbox

from numpy import number

startTime=time.time()

def take_snapshot():
    number=random.randint(0,100)
    #initialising cv2
    videoCaptureObj=cv2.VideoCapture(0)
    result=True
    while (result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObj.read()
        imageName="image"+str(number)+".png"
        

        #cv2.imwrite() is used to save an image to any storage device
        cv2.imwrite(imageName,frame)
        startTime=time.time
        result=False
    return imageName
    print("SNAPSHOT TAKEN")
        #releases the camera
    videoCaptureObj.release()

        #closes all the windows that might be open while this process
    cv2.destroyAllWindows()

take_snapshot()

def uploadfile(imageName):
    access_token = 'sl.BJ6VCgwf6SMN1LuX1eHaE4By7Ie5VFaKpBWDAl52c5NNM7RdJSPm4StPebMk-g2EflMlUZUeHmqQxpB3L-kA8JFDZJj9UQbxLpSii83X1P_217PdnteGoZTalKkHech0AyB9KGItrbQ'
    file=imageName

    file_from = file

    file_to = "/newfolder1/"+(imageName)

    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
            print("FILE UPLOADED")
    
def main():
    while (True):
        if ((time.time()-startTime)>=300):
            name=take_snapshot()
            uploadfile(name)

main()