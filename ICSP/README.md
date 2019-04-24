# ICSP Hardware

## Overview

Use a Raspberry Pi Zero as a host to do In-Circuit Serial Programming of AVR’s. IOFF buffers are used to level convert to the targets voltage. It also allows the serial port to be used for serial bootload and has some switches to control looping of the upload. How to: “git pull” then “make isp” (assuming that is the desired Makefile rule).

## Inputs/Outputs/Functions

```
        Open Drain Voltage level converter for ICSP pins 
        Open Drain Voltage level converter for serial bootload pins
        Swithchs for control of Shutdown, Bootload, and ICSP.
```


## Uses

```
        In-Circuit Serial Programing of AVR target 2V7 to 5V. 
        Bootload programing of target (1.8V to 5V).
        Use your own R-Pi software to detect a switch (BCM13, BCM5) and run the uploader.
```


# Table Of Contents

1. [Status](#status)
2. [Design](#design)
3. [Bill of Materials](#bill-of-materials)
4. [How To Use](#how-to-use)


# Status

[Options](#bill-of-materials)

![Status](./status_icon.png "ICSP Status")

```
        ^2  Done: Design, Layout, 
            WIP: BOM,
            Todo: Review*, Order Boards, Assembly, Testing, Evaluation.
            *during review the Design may change without changing the revision.
            try with an R-Pi zero rather than Uno with ISP sketch.
            set up the serial port for bootloading use.
            set up better for pogo pins.

        ^1  Done: Design, Layout, BOM, Review*, Order Boards, Assembly, Testing,
            WIP: Evaluation.
            Todo:  
            *during review the Design may change without changing the revision.
            fixed the pads so the connector/header works.

        ^0  Done: Design, Layout, BOM, Review*, Order Boards, Assembly, Testing, Evaluation.
            location: 2015-12-15 Bench /w ArduinoISP sketch on an Uno 
            location: 2015-12-25 Shelf /w ArduinoISP sketch on an Uno 
```

Debugging and fixing problems i.e. [Schooling](./Schooling/)

Setup and methods used for [Evaluation](./Evaluation/)


# Design

The board is 0.063 thick, FR4, two layer, 1 oz copper with ENIG (gold) finish.

![Top](./Documents/15321,Top.png "ICSP Top")
![TAssy](./Documents/15321,TAssy.jpg "ICSP Top Assy")
![Bottom](./Documents/15321,Bottom.png "ICSP Bottom")
![BAssy](./Documents/15321,BAssy.jpg "ICSP Bottom Assy")

## Electrical Parameters (Typical)

```
74LVCO7A input are tolerant to 5.5V
74LVCO7A supply on target side can range from 1.65V to 5.5V
When used for in-circuit programming consult the MCU datasheet for valid programming voltages (AVR seems to mostly be 2V7 to 5V).
```

## Mounting

```
        Connectors or pogo pins are to be soldered by user
```

## Electrical Schematic

![Schematic](./Documents/15321,Schematic.png "ICSP Schematic")

## Testing

Check correct assembly and function with [Testing](./Testing/)


# Bill of Materials

The BOM is a CVS file(s), import it into a spreadsheet program like LibreOffice Calc (or Excel), or use a text editor.

Option | BOM's included
----- | ----- 
A. | [BRD] 
M. | [BRD] [SMD] [HDR] 
X. | [BRD] [SMD] [HDR] [POGO]
Z. | [BRD] [SMD] [HDR] [POGO] [POL]

[BRD]: ./Design/15321BRD,BOM.csv
[SMD]: ./Design/15321SMD,BOM.csv
[HDR]: ./Design/15321HDR,BOM.csv
[POGO]: ./Design/15321POGO,BOM.csv
[POL]: ./Design/15321POL,BOM.csv

[Available](https://rpubus.org/Order_Form.html)

# How To Use

Solder connectors or pogo pins (e.g. [ICT-100-T]).

[ICT-100-T]: http://www.mouser.com/Search/Refine.aspx?Keyword=ICT-100-T

The 74LVC07A has IOFF circuitry which disables the output to prevent damaging current backflow when the device is powered down. Since the buffer is powered by the target removing power from the target after programming is both safe and advised.

The next version (^2) will use an R-Pi as the host. The upload tool (avrdude) can run directly on it, avrdude can operate the SPI pins with "avrdude -c linuxspi" or bit-bang then with "avrdude -clinuxgpio." The R-Pi can also do a serial bootload with a verity of methods: optiboot is "avrdude -c arduino," xboot is "avrdude -c avr109". It can operate serial tools like the one I have been using which is an Uno loaded with [ArduinoISP] "avrdude -c stk500v1", [ElTangas/STK2UPDI] with "avrdude -c stk500v2", or even [mraardvark/pyupdi] serial port program.

[ArduinoISP]: https://github.com/arduino/Arduino/blob/master/build/shared/examples/11.ArduinoISP/ArduinoISP/ArduinoISP.ino
[ElTangas/STK2UPDI]: https://github.com/ElTangas/STK2UPDI
[mraardvark/pyupdi]: https://github.com/mraardvark/pyupdi/


The plan with ^2 is to use the switches like the shutdown switch that I have been using on RPUpi.  So that means a python program. I can start it at the command line and it will watch the switch and run the make rule at the working directory when it is pushed. The current working folder will tell the program which makefile to run, so I don't even need to change the makefile for this, but I do need to write a little Python program to loop the build system at each button push, and I guess it can exit when I press the enter key. Everything is done over an SSH connection. Do I need to explain SSH, I think that needs to be a homework exercise.

I use Github for my programs and start with a clone of my project files onto the R-Pi, latter a "git pull" is used for updates before I burn new firmware. Also, I use Makefiles; there is no IDE, just an editor, sometimes a good one like VSCode and other times it is Notepad (Samba can share the files) or gedit. If you need an IDE, then I am sorry, but this is probably not the right tool.


