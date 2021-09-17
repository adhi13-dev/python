import cv2
import dropbox
import time
import random

from dropbox.base import DropboxBase

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True 
    while (result) :
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
def uploadfile(img_name):
    access_token = "sl.A4rd72TyFPZTBDzRj02U9O9MlsmtoAfDTQ81fFTJ829TYLeunIt3a7gRq1Q95vkSrF4zpQtdATGHCsMUZmtJdBt-KjPttNmKYPdfng1rrWIsUWQ_iYgMjOdaSB24PDn1mkO_1Fw"
    file = img_counter
    file_from = file
    file_to = "/newfolder1/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file has been moved !")

def main():
    while (True):
        if((time.time()-start_time)>300):
            name = take_snapshot()
            uploadfile(name)
main()
