# Description

This is a list of Test preformed on each board after assembly.

# Table of References


# Table Of Contents:

1. [Basics](#basics)
2. [Assembly check](#assembly-check)
3. [IC Solder Test](#ic-solder-test)
4. [Bias 5V](#bias-5v)
5. [Charge To 9V](#charge-to-9v)
6. [Charge To 12V](#charge-to-12v)
7. [Charge To 24V](#charge-to-24v)
8. [K[1..3] Set and Reset](#k13-set-and-reset)


## Basics

These tests are for an assembled K3 board 16276^0 which may be referred to as a Unit Under Test (UUT). If the UUT fails and can be reworked then do so, otherwise it needs to be scraped. 

__Warning__: never use a soldering iron to rework ceramic capacitors due to the thermal shock.

![Items used for test](./16276_ItemsUsedForTest.jpg "K3 With RPUno" "Items used for test")


## Assembly check

After assembly check the circuit carefully to make sure all parts are soldered and correct. The device marking is used as the part name on the schematic and assembly drawings.  In other words, the name K38 (Q16) is actually the device marking. Check the bill of materials to figure out what the device is (e.g. it is a Diodes BSS138).


## IC Solder Test

Check continuity between pin and pad by measuring the reverse body diode drop from 0V (aka ground) and all other IC pads not connected to 0V. This value will vary somewhat depending on what the pin does, but there is typically an ESD diode to ground or sometimes a body diode (e.g. open drain MOSFET), thus a value of .4V to .7V is valid to indicate a solder connection. 


## Bias 5V

Setup current limited supply with 5V and about 20mA limit. Connect A0, A1, A2 (J2 pin 1, 2, 3),  EN (J2 pin 4), and 0V (J2 pin 8) to the supply return. Connect nEN (J2 pin 5) and +5V (J2 pin 6) to supply. Turn on the supply and Check that the current drawn is about 3 mA.

``` 
 TODO:  some data from unit(s)
{"DISABLED_mA":[2.7,] }
``` 

Add 100 Ohm load between BOOST (C4 plus pin) and 0V (J2 pin 8). Check current draw.

``` 
{ "DISABLED_mA":[16.4,] }
``` 

## Charge To 9V

Setup current limited supply with 5V and about 400mA limit. Connect A1, A2 (J2 pin 2, 3),  nEN (J2 pin 5), and 0V (J2 pin 8) to the supply return. Connect A0 (J2 pin 1), EN (J2 pin 4) and +5V (J2 pin 6) to supply. Connect 100 Ohm load between BOOST (C4 plus pin) and 0V (J2 pin 8). Turn on the supply and Check that boot supply is off (e.g. 1.7V)
    
```
{ "9VBOOSTOFF_V":[1.64,]}
```

Open the 100 Ohm load and Check that the boost voltage is 9V.

```
{ "9VBOOST_V":[9.2,]}
```

Connect the 100 Ohm load between BOOST (C4 plus pin) and 0V (J2 pin 8). Check BOOST voltage and current draw.

```
{ "9VBOOSTLD_V":[9.12,],
"9VBOOSTLD_mA":[224,]}
```

NOTE: A 17mA current source is used to test for a short, if the voltage it causes is not high enough then the PMOS (Q18) that feeds the boost SMPS does not enable. This is a safty feature that should prevent a shorted bridge from connecting to the 5V supply.


## Charge To 12V

Setup current limited supply with 5V and about 400mA limit. Connect A1, A2 (J2 pin 2, 3),  nEN (J2 pin 5), and 0V (J2 pin 8) to the supply return. Connect A0 (J2 pin 1), EN (J2 pin 4) and +5V (J2 pin 6) to supply. Connect 100 Ohm load between BOOST (C4 plus pin) and 0V (J2 pin 8). Jumper for 12V boots (J3 pin 2 to pin 3). Turn on the supply and Check that boot supply is off (e.g. 1.7V)
    
```
{ "12VBOOSTOFF_V":[1.64,]}
```

Open the 100 Ohm load and Check that the boost voltage is 12V. 

```
{ "12VBOOST_V":[12.2,]}
```

Connect the 100 Ohm load between BOOST (C4 plus pin) and 0V (J2 pin 8). Check BOOST voltage and current draw.

```
{ "12VBOOSTLD_V":[9.8,],
"12VBOOSTLD_mA":[260,]}
```

NOTE: The boost supply is now in current limit with the 100 Ohm load.


## Charge To 24V

Setup current limited supply with 5V and about 400mA limit. Connect A1, A2 (J2 pin 2, 3),  nEN (J2 pin 5), and 0V (J2 pin 8) to the supply return. Connect A0 (J2 pin 1), EN (J2 pin 4) and +5V (J2 pin 6) to supply. Connect 100 Ohm load between BOOST (C4 plus pin) and 0V (J2 pin 8). Jumper for 24V boots (J3 pin 2 to pin 1). Turn on the supply and Check that boot supply is off (e.g. 1.7V)
    
```
{ "24VBOOSTOFF_V":[1.64,]}
```

Open the 100 Ohm load and Check that the boost voltage is 24V. 

```
{ "24VBOOST_V":[24.3,]}
```

Connect the 100 Ohm load between BOOST (C4 plus pin) and 0V (J2 pin 8). Check BOOST voltage and current draw.

```
{ "24VBOOSTLD_V":[9.8,],
"24VBOOSTLD_mA":[261,]}
```

## K[1..3] Set and Reset

Setup a current limited supply with 5V and about 400mA limit. Connect A1, A2 (J2 pin 2, 3),  nEN (J2 pin 5), and 0V (J2 pin 8) to the supply return. Connect A0 (J2 pin 1) and +5V (J2 pin 6) to supply. Jumper for 24V boots (J3 pin 2 to pin 1). Connect a terminal of a normally open momentary switch to a 1k Ohm pull-down (0V) and EN (J2 pin 4) with the other terminal of the switch connected to supply. Connect LED load fixture to K1 through K3 and the common.  

* NOTE: the LED's light up one string for each selection, e.g. Set is a different LED string than Reset for each K1 through K3. To do this the LED's in the Set string are polarized in the oppisit direction as the ones in Reset. The LED's can't withstand the reverse polarity of the applied voltage so a 1N4148 is also added to the string to block the reverse polarity.

Turn on the supply and press the switch to charge the boost. Release the switch and move A0 to supply return and A1 to supply to drive SET-K1. Press the switch and verify the LED string for K1 Set is glowing. Release the switch to turn off the bridge and move A0 back to the supply and A1 to its return and press the switch to charge boost again. Repeat for each RESET-K1, SET-K2, RESET-K2, SET-K3, and RESET-K3. Use the chart on the schematic as a reference of how to connect A0, A1, and A2. Make sure to release before moving any wires. 

* NOTE: The reason to disable before removing wires is because debounce during (e.g. SET-K2 and RESET-K2) bridge selection can be faster than the transistors can clear (e.g. transistor switching time) and thus cross conduct, which results in instant destruction of the bridge. 


