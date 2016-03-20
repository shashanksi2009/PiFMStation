# PiFMStation
Turns your Raspberry Pi into mini FM radio station ( No additional HARDWARE required )

This is my small work which will bring you some joy . This is actually my final setup for my own pi for best quality and performance . I used various software for audio transmission over FM frequency , fm_transmitter works best . This repo contains following :-  fm_transmitter ( by MARKONDEJ ) , my python script ( transmitter.py ) and tricky configuration .

## Basics

This uses hardware on the raspberry pi which generate spread spectrum clock signal on GPIO4 pin for FM radio energy . It even works without any antenna ( very powerful ) . Plug 20 cm long copper wire as antenna ( size may vary but range changes ) . It's range increases from  ~ 10 cm to 100 m with antenna . This requires hardware access , so run this program as SuperUser .

   ###NOTE:
          The Raspberry Pi’s broadcast frequency can range between 1Mhz and 250Mhz, which may interfere with government bands. We advise that you limit your transmissions to the standard FM band of 87.5MHz–107.9MHz (see Step 3) and always choose a frequency that’s not already in use, to avoid interference with licensed broadcasters. Be a good citizen .


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
   
   ###Setup completed successfully .....

# Run

Pick an unused frequiency in the FM range (be a good citizen and play nice).

```
./bin/Release/fm_transmitter starwars.wav 103.5
```
