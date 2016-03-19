
import time
import os
import threading

notDone=True
files=os.listdir("/media/radio")
if os.path.isfile("~tmp1.wav"):
        os.system("rm ~tmp1.wav")
if os.path.isfile("~tmp2.wav"):
        os.system("rm ~tmp2.wav")

firstTime=True
saved=""
playing=""
def play():
        global firstTime
        global playing
        time.sleep(10)
        print "Broadcast started ..."
        while True :
                        if os.path.isfile("~tmp1.wav"):
                                playing=saved
                                os.system("mv ~tmp1.wav ~tmp2.wav")
                                time.sleep(2)
                                print "Now playing , " + playing + " ..."
                                firstTime=False
                                os.system("fm_transmitter-master/bin/Release/fm_transmitter ~tmp2.wav 90.6")

def convert():
        global saved
        while True:
                for file in files :
                        notDone=True
                        while notDone:
                                if os.path.isfile("~tmp1.wav")==False:
                                        saved=file
                                        os.system('sox -c 1 -v 1.0 -r 96k  "/media/radio/'+file+'" ~tmp1.wav')
                                        if firstTime==False:
                                                print "Next playing , "+saved+" ..."
                                        notDone=False
                                time.sleep(1)


print "Starting, please wait ..."
t1=threading.Thread(target=convert)
t2=threading.Thread(target=play)
t1.start()
t2.start()
