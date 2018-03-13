# Description

This is a list of Test preformed on each board after assembly.

# Table of References


# Table Of Contents:

1. Basics
2. Assembly check
3. IC Solder Test
4. Bias 5V
5. TBD


## Basics

These tests are for an assembled USBart board 180666^0 which may be referred to as a Unit Under Test (UUT). If the UUT fails and can be reworked then do so, otherwise it needs to be scraped. 

__Warning__: never use a soldering iron to rework ceramic capacitors due to the thermal shock.

![ItemsForTest](./180666_ItemsUsedForTest.jpg "Items used for test")

## Assembly check

After assembly check the circuit carefully to make sure all parts are soldered and correct. The device marking is used as the part name on the schematic and assembly drawings.  In other words, the name K3N (Q1) is actually the device marking. Check the bill of materials to figure out what the device is (e.g. it is a Diodes MMBT3906).


## IC Solder Test

Check continuity between pin and pad by measuring the reverse body diode drop from 0V (aka ground) and all other IC pads not connected to 0V. This value will vary somewhat depending on what the pin does, but there is typically an ESD diode to ground or sometimes a body diode (e.g. open drain MOSFET), thus a value of .4V to .7V is valid to indicate a solder connection. 


## Bias 5V

Setup a current limited supply with 5V and about 30mA limit. Connect TBD to the supply return. Connect TBD to the supply. Measure the input current while disabled.

``` 
{ "CURR_SOURCE_mA":[TBD,] }
``` 
