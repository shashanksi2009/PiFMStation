# PiFMStation
Turns your Raspberry Pi into mini FM radio station ( No additional HARDWARE required )

This is my small work which will bring you some joy . This is actually my final setup for my own pi for best quality and performance . I used various software for audio transmission over FM frequency , fm_transmitter works best . This repo contains following :-  fm_transmitter ( by MARKONDEJ ) , my python script ( transmitter.py ) and tricky configuration .

## Basics

This uses hardware on the raspberry pi which generate spread spectrum clock signal on GPIO4 pin for FM radio energy . It even works without any antenna ( very powerful ) . Plug 20 cm long copper wire as antenna ( size may vary but range changes ) . It's range increases from  ~ 10 cm without antenna to ~ 100 m with antenna . This requires hardware access , so run this program as SuperUser .

   NOTE:
          The Raspberry Pi’s broadcast frequency can range between 1Mhz and 250Mhz, which may interfere with government bands. I advise that you limit your transmissions to the standard FM band of 87.5MHz–107.9MHz and always choose a frequency that’s not already in use, to avoid interference with licensed broadcasters. Be a good citizen .

## Features

   PiFMStation supports :-
   
         * Easy to use .
         * Playlist play .
         * Various extensions support .
         * Best performance and loud sound .
   
## Setup

       $> cd ~
       $> sudo mkdir pifmstation
       $> cd pifmstation
       $> wget https://github.com/shashanksi2009/PiFMStation/archive/master.zip
       $> sudo unzip master.zip
       $> sudo rm master.zip
       $> sudo apt-get install sox libsox-fmt-all
       $> cd fm_transmitter
       $> sudo make -j4
       $> cd ..
   
   Setup completed successfully .....

##Test

To test all set correctly , run following :-

      $> sudo python transmitter.py

Now turn on your radio , if you are able to listen some sound @ 100.7 Mhz then all set nicely .

##Settings

For setting your mini FM station , execute following on terminal :-

      $> sudo nano transmitter.py

Change the following lines :-

      frequeny = 100.7 (default) // desire value from 87.5 MHz to 107.9 MHz
      
      audio_folder = "playlist/" ( default folder for your songs ) // You may paste songs in playlist folder or change audio_folder value to a folder which contains your audio file(s) but don't forget '/' at the end .

Save and exit file ( Ctrl+O then Ctrl+X ) .

##Run

Pick an unused frequency in the FM range and place your songs in audio folder.
Reboot your device ....

To run , type in terminal :-

      $> cd ~/pifmstation
      $> sudo python transmitter.py

To stop , press,

      Ctrl + Z



ENJOY YOUR COOL DIY FM RADIO STATION ..........................
