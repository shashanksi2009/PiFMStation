# PiFMStation
Turns your Raspberry Pi into mini FM radio station ( No additional HARDWARE required )

This is my small work which will bring you some joy . This is actually my final setup for my own pi for best quality and performance . I used various software for audio transmission over FM frequency , fm_transmitter works best . This repo contains following :-  fm_transmitter ( by MARKONDEJ ) , my python script ( transmitter.py ) and configuration .

## Basics

This uses hardware on the raspberry pi which generate spread spectrum clock signal on GPIO4 pin for FM radio energy . It even works without any antenna . Plug 20 cm long copper wire as antenna ( size may vary but range changes ) . It's range increases from  ~ 10 cm to 100 m with antenna . This required hardware access , so run this program as SuperUser .

# Setup

       $> cd ~
       $> sudo mkdir pifmstation
       $> cd pifmstation
       $> wget 
``make -j4``

# Run

Pick an unused frequiency in the FM range (be a good citizen and play nice).

```
./bin/Release/fm_transmitter starwars.wav 103.5
```
