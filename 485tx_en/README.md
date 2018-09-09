# 485tx_en Hardware

## Overview

Waring: this board is not industry-standard RS485.

RS485 half duplex with fail-safe biasing and automatic push to talk (e.g. tx_en). Truth is industry standard RS485 is notoriously difficult to work with. But now that there are a few chip options with a trustworthy fail-safe bias, it can be a lot easier.

When more than two transceivers are on the media (the differential pair) and more than one unintentionally transmits (e.g. both DE HIGH and, one DI HIGH and another with DI LOW) the results can be a catastrophe (differential lines A/B cross conduct). This problem is designed into the industry standard and it is not easy to fix, at least with long-term survival in mind.

The ISL3172, MAX3085, and THVD150 transceivers have a 50mV built-in fail-safe margin, so they see everything on the pair that is higher than -50mV as a HIGH. Between -50mV and -200mV is undefined and bellow -200mV is a LOW. These devices see 0V on the pair as a HIGH. The old standard is undefined in the range 200mV to -200mV between A/B pair.

If 0V between A/B is guaranteed to be seen as a HIGH, then why do I need to drive it? I do not.

When a UART TX line is at rest it is a digital HIGH. If I use the digital high to disable the transmitter and all the receivers see 0V as HIGH then all is good, plus the possibility of self-destructing cross conduction is eliminated.

The RX line will receive everything placed on the media and it is enabled by default with a pull-up.

IOFF buffers are also added so any MCU voltage can be used.

Why? Well, beginners need something that is resistant to damage. The common MAX485 boards are easy to wreck with programming errors. 


## Inputs/Outputs/Functions

```
        RS485 transceiver
        Easy push to talk control, so easy it can be ignored.
```


## Uses

```
        Half Duplex serial that does not self-destruct with software mistakes.
```


# Table Of Contents

1. [Status](#status)
2. [Design](#design)
3. [Bill of Materials](#bill-of-materials)
4. [How To Use](#how-to-use)


# Status

![Status](./status_icon.png "Status")

```
        ^0  Done: 
            WIP: 
            Todo: Design, Layout, BOM, Review*, Order Boards, Assembly, Testing, Evaluation.
            *during review the Design may change without changing the revision.
```

Debugging and fixing problems i.e. [Schooling](./Schooling/)

Setup and methods used for [Evaluation](./Evaluation/)


# Design

The board is 0.063 thick, FR4, two layer, 1 oz copper with ENIG (gold) finish.

![Top](./Documents/18250,Top.png "Top")
![TAssy](./Documents/18250,TAssy.jpg "Top Assy")
![Bottom](./Documents/18250,Bottom.png "Bottom")
![BAssy](./Documents/18250,BAssy.jpg "Bottom Assy")


## Electrical Schematic

![Schematic](./Documents/18250,Schematic.png "Schematic")

## Testing

Check correct assembly and function with [Testing](./Testing/)


# Bill of Materials

The BOM is a CVS file(s), import it into a spreadsheet program like LibreOffice Calc (or Excel), or use a text editor.

Option | BOM's included
----- | ----- 
A. | [BRD] 
M. | [BRD] [SMD] [HDR] 
W. | [BRD] [SMD] [HDR] [PLUG]

[BRD]: ./Design/18250BRD,BOM.csv
[SMD]: ./Design/18250SMD,BOM.csv
[HDR]: ./Design/18250HDR,BOM.csv
[PLUG]: ./Design/18250PLUG,BOM.csv


# How To Use

Connect UART RX to RO and UART TX to DI. The Receiver enable is logic low (with a bar over RE, or nRE), it has a 3k Ohm pull-down resistor. The Transmitter enable (DE) has a 3k Ohm pull-up, but is also pulled low with an N-CH MOSFET whose gate is controlled with the UART TX. In general, the push to talk lines (DE and nRE) is ignored but it is possible to control them (e.g. when a point to point communication is needed, perhaps all the devices can go into a lockout mode for a time). 



