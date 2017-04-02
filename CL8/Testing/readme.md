# Description

This is a list of Test preformed on each board after assembly.

# Table of References


# Table Of Contents:

1. [Basics](#basics)
2. [Assembly check](#assembly-check)
3. [IC Solder Test](#ic-solder-test)
4. [Bias 5V](#bias-5v)
5. [TBD](#tbd)


## Basics

These tests are for an assembled K3 board 16276^2 which may be referred to as a Unit Under Test (UUT). If the UUT fails and can be reworked then do so, otherwise it needs to be scraped. 

__Warning__: never use a soldering iron to rework ceramic capacitors due to the thermal shock.

![ItemsForTest1to7](./16276_ItemsUsedForTest[1-7].jpg "Items used for test 1to7")

![ItemsForTest8](./16276_ItemsUsedForTest[8].jpg "Items used for test 8")

## Assembly check

After assembly check the circuit carefully to make sure all parts are soldered and correct. The device marking is used as the part name on the schematic and assembly drawings.  In other words, the name K38 (Q16) is actually the device marking. Check the bill of materials to figure out what the device is (e.g. it is a Diodes BSS138).


## IC Solder Test

Check continuity between pin and pad by measuring the reverse body diode drop from 0V (aka ground) and all other IC pads not connected to 0V. This value will vary somewhat depending on what the pin does, but there is typically an ESD diode to ground or sometimes a body diode (e.g. open drain MOSFET), thus a value of .4V to .7V is valid to indicate a solder connection. 


## Bias 5V

Setup a current limited supply with 5V and about 30mA limit. Connect A0 (J3 pin 1), A1 (J3 pin 3), A2 (J3 pin 5), and all 0V (J3 pin 2,4,6, J2 pin 3) to the supply return. Connect SUPPLY (J2 pin 2) and VCC (J3 pin 8) to the supply. Connect E3 (which has a pull down) to a switch that connects to supply when closed. Verify that nE1 (J3 pin 10) and nE2 (J3 pin 9) are each pulled down by 10k Ohm resistor. Measure the input current while disabled.

``` 
 {"DISABLED_mA":[] }
``` 

Close the switch that connects E3 to the 5V supply to turn on the current source that is used to test for a shorted bridge, wait for it to settle (about one second) and measure that the current drawn is less than 5 mA.

``` 
{"ENABLED_mA":[] }
``` 


## TBD

To be determined
