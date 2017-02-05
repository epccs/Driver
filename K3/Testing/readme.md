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

These tests are for an assembled K3 board 16276^1 which may be referred to as a Unit Under Test (UUT). If the UUT fails and can be reworked then do so, otherwise it needs to be scraped. 

__Warning__: never use a soldering iron to rework ceramic capacitors due to the thermal shock.

![Items used for test](./16276_ItemsUsedForTest.jpg "K3 With RPUno" "Items used for test")


## Assembly check

After assembly check the circuit carefully to make sure all parts are soldered and correct. The device marking is used as the part name on the schematic and assembly drawings.  In other words, the name K38 (Q16) is actually the device marking. Check the bill of materials to figure out what the device is (e.g. it is a Diodes BSS138).


## IC Solder Test

Check continuity between pin and pad by measuring the reverse body diode drop from 0V (aka ground) and all other IC pads not connected to 0V. This value will vary somewhat depending on what the pin does, but there is typically an ESD diode to ground or sometimes a body diode (e.g. open drain MOSFET), thus a value of .4V to .7V is valid to indicate a solder connection. 


## Bias 5V

Setup a current limited supply with 5V and about 20mA limit. Connect A0, A1, A2 (J3 pin 1, 3, 5), and 0V (J3 pin 2,4,6; J2 pin 3) to the supply return. Connect SUPPLY (J2 pin 2) and VCC (J3 pin 8) to the supply. Connect E3 (which has a pull down) to a switch that is connected to supply when closed. Verify that nE1 (J3 pin 10) and nE2 (J3 pin 9) are pulled down by 10k Ohm resistors. Measure the input current while disabled.

``` 
 TODO:  some data from unit(s)
{"DISABLED_mA":[0.2,] }
``` 

Close the switch that connects E3 to the 5V supply to turn on the current source that is used to test for a shorted bridge, wait for it to settle (about one second) and measure that the current drawn is less than 5 mA.

``` 
 TODO:  some data from unit(s)
{"ENABLED_mA":[3.7,] }
``` 

Add 100 Ohm load between BOOST (C4 plus pin) and 0V (J2 pin 3). Measure the current source.

``` 
{ "CURR_SOURCE_mA":[17.6,] }
``` 


## Charge To 9V

Setup current limited supply with 5V and about 400mA limit. Connect A1, A2 (J3 pin 3, 5), and 0V (J3 pin 2,4,6; J2 pin 3) to the supply return.  Connect A0, VCC (J3 pin 1, 8) and SUPPLY (J2 pin 2) to supply. Connect E3 (which has a pull down) to a switch that is connected to supply when closed. Connect 0 Ohm short between BOOST (C4 plus pin) and 0V (J2 pin 3). Turn on the supply and Check that boot supply is off (e.g. only current source). Which shows that a shorted bridge will lock out the supply.

```
{ "9VBOOSTOFF_mA":[17.6,]}
```

Open the 0 Ohm load and Check that the boost voltage is 9V.

```
{ "9VBOOST_V":[9.2,]}
```

Connect a 100 Ohm load between BOOST (C4 plus pin) and 0V (J2 pin 3). Check BOOST voltage and current draw.

```
{ "9VBOOSTLD_V":[9.16,],
"9VBOOSTLD_mA":[215,]}
```

NOTE: the 17mA current source is used to test for a short, if the voltage it causes is not high enough then the PMOS (Q19) that connects the boost to SUPPLY does not enable, also the shutdown hack (Q25) does not enable. These safty features that should prevent a shorted bridge from connecting to the supply.


## Charge To 12V

Setup current limited supply with 5V and about 400mA limit. Connect A1, A2 (J3 pin 3, 5), and 0V (J3 pin 2,4,6; J2 pin 3) to the supply return.  Connect A0, VCC (J3 pin 1, 8) and SUPPLY (J2 pin 2) to supply. Connect E3 (which has a pull down) to a switch that is connected to supply when closed. Connect 0 Ohm short between BOOST (C4 plus pin) and 0V (J2 pin 3). Jumper for 12V boots (J4 pin 2 to pin 3). Turn on the supply and Check that boot supply is off.

```
{ "12VBOOSTOFF_mA":[17.6,]}
```

Open the 0 Ohm short and Check that the boost voltage is 12V. 

```
{ "12VBOOST_V":[12.15,]}
```

Connect a 100 Ohm load between BOOST (C4 plus pin) and 0V (J2 pin 3). Check BOOST voltage and current draw.

```
{ "12VBOOSTLD_V":[9.9,],
"12VBOOSTLD_mA":[257,]}
```

NOTE: The boost supply is in current limit with the 100 Ohm load, and shows how much the SUPPLY needs to be able to provide if a brown out is to be avoided.


## Charge To 24V

Setup current limited supply with 5V and about 400mA limit. Connect A1, A2 (J3 pin 3, 5), and 0V (J3 pin 2,4,6; J2 pin 3) to the supply return.  Connect A0, VCC (J3 pin 1, 8) and SUPPLY (J2 pin 2) to supply. Connect E3 (which has a pull down) to a switch that is connected to supply when closed. Connect 0 Ohm short between BOOST (C4 plus pin) and 0V (J2 pin 3). Jumper for 24V boots (J4 pin 1 to pin 2). Turn on the supply and Check that boot supply is off.

    
```
{ "24VBOOSTOFF_mA":[17.6,]}
```

Open the 0 Ohm short and Check that the boost voltage is 24V. 

```
{ "24VBOOST_V":[24.8,]}
```

Connect the 100 Ohm load between BOOST (C4 plus pin) and 0V (J2 pin 3). Check BOOST voltage and current draw.

```
{ "24VBOOSTLD_V":[9.9,],
"24VBOOSTLD_mA":[257,]}
```

## K[1..3] Set and Reset

The [Solenoid] firmware can be used to test operation of the bridges with a LED string in place of the coil. 

Setup an RPUno and connect it to the K3 board as shown, but use the LED strings in place of the coils.

![Example](../Documents/Example.png "Example")

* NOTE: the LED's light up one string for each selection, e.g. SET is a different LED string than RESET for each pretend coil. To do this the LED's in the SET string are polarized in the opposite direction as the ones in RESET. The LED's can't withstand the reverse polarity of the applied voltage so a 1N4148 is also added to the string to block the reverse polarity.

When the RPUno is reset the firmware will operate each coil with a SET and then a RESET with a one-second pause for each operation. 



