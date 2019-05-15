# Description

This is a list of Test preformed on each board after assembly.

# Table of References


# Table Of Contents:

1. [Basics](#basics)
2. [Assembly check](#assembly-check)
3. [IC Solder Test](#ic-solder-test)
4. [Bias 5V](#bias-5v)


## Basics

These tests are for an assembled ICSP board 15321^2 which may be referred to as a Unit Under Test (UUT). If the UUT fails and can be reworked then do so, otherwise it needs to be scraped. 

__Warning__: never use a soldering iron to rework ceramic capacitors due to the thermal shock.

![ItemsForTest](./15321_ItemsUsedForTest.jpg "Items used for test")

## Assembly check

After assembly check the circuit carefully to make sure all parts are soldered and correct. The device marking is used as the part name on the schematic and assembly drawings.  In other words, the name K38 (Q16) is actually the device marking. Check the bill of materials to figure out what the device is (e.g. it is a Diodes BSS138).


## IC Solder Test

Check continuity between pin and pad by measuring the reverse body diode drop from 0V (aka ground) and all other IC pads not connected to 0V. This value will vary somewhat depending on what the pin does, but there is typically an ESD diode to ground or sometimes a body diode (e.g. open drain MOSFET), thus a value of .4V to .7V is valid to indicate a solder connection. 


## TBD

Buffer U1 and U2 are powered by the target side. The probes are difficult to line up, and solder bridges are a problem, which can damage the target, check the ESD diode after soldering probes or headers to interface with the ICSP target.
