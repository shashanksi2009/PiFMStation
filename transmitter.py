import time
import os
import threading

audio_folder = "playlist/"      // Set folder where audio file exists, Default : playlist/
frequency = "100.7"           // Set frequency for broadcasting, Default : 100.7 MHz
fm_transmitter_folder = "fm_transmitter/bin/Release/fm_transmitter"  //fm_transmitter folder
""" WARNING :-
> Don't change value of fm_transmitter_folder
"""


notDone=True
files=os.listdir( audio_folder )
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
                                os.system( fm_transmitter_folder + " ~tmp2.wav " + frequency)

def convert():
        global saved
        while True:
                for file in files :
                        notDone=True
                        while notDone:
                                if os.path.isfile("~tmp1.wav")==False:
                                        saved=file
                                        os.system('sox -c 1 -v 1.0 -r 96k  "' + audio_folder + file+'" ~tmp1.wav')
                                        if firstTime==False:
                                                print "Next playing , "+saved+" ..."
                                        notDone=False
                                time.sleep(1)


print "Starting, please wait ..."
t1=threading.Thread(target=convert)
t2=threading.Thread(target=play)
t1.start()
t2.start()
