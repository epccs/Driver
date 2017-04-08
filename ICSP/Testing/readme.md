# Description

This is a list of Test preformed on each board after assembly.

# Table of References


# Table Of Contents:

1. [Basics](#basics)
2. [Assembly check](#assembly-check)
3. [IC Solder Test](#ic-solder-test)
4. [Bias 5V](#bias-5v)


## Basics

These tests are for an assembled ICSP board 15321^1 which may be referred to as a Unit Under Test (UUT). If the UUT fails and can be reworked then do so, otherwise it needs to be scraped. 

__Warning__: never use a soldering iron to rework ceramic capacitors due to the thermal shock.

![ItemsForTest](./15321_ItemsUsedForTest.jpg "Items used for test")

## Assembly check

After assembly check the circuit carefully to make sure all parts are soldered and correct. The device marking is used as the part name on the schematic and assembly drawings.  In other words, the name K38 (Q16) is actually the device marking. Check the bill of materials to figure out what the device is (e.g. it is a Diodes BSS138).


## IC Solder Test

Check continuity between pin and pad by measuring the reverse body diode drop from 0V (aka ground) and all other IC pads not connected to 0V. This value will vary somewhat depending on what the pin does, but there is typically an ESD diode to ground or sometimes a body diode (e.g. open drain MOSFET), thus a value of .4V to .7V is valid to indicate a solder connection. 


## Bias 5V

Setup a current limited supply with 5V and about 30mA limit. Connect the SPI input 0V (J1 pin 6) to the supply return. Connect +5V (J1 pin 2), MOSI (J1 pin 4) and SCK (J1 pin 3) to the supply. 

``` 
{"DISABLED_mA":[] }
``` 

Connect the target voltage to the supply (J2 pin 2). Note the 0V is connected between to J1 and J2. 

``` 
{"ENABLED_mA":[] }
``` 

Pull down SCK (J1 pin 3) with a connection to the supply return.

``` 
{ "SCK_mA":[] }
``` 

Pull down MOSI (J1 pin 4) with a connection to the supply return, pull up SCK (J1 pin 3) to the supply.

``` 
{ "MOSI_mA":[] }
``` 

Pull down nSS (J1 pin 5) with a connection to the supply return, pull up MOSI (J1 pin 4) to the supply.

``` 
{ "nSS_mA":[] }
``` 

Pull down MISO (J2 pin 1) with a connection to the supply return, open nSS.

``` 
{ "MISO_mA":[] }
``` 
