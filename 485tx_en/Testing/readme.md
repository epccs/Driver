# Description

This is a list of Test preformed on each board after assembly.

# Table of References


# Table Of Contents:

1. Basics
2. Assembly check
3. IC Solder Test
4. Bias
5. TBD


## Basics

These tests are for an assembled 485tx_en board 18250^0 which may be referred to as a Unit Under Test (UUT). If the UUT fails and can be reworked then do so, otherwise it needs to be scraped. 

__Warning__: never use a soldering iron to rework ceramic capacitors due to the thermal shock.

Items used for test.

![ItemsForTest](./18250_ItemsUsedForTest.jpg "Items used for test")

## Assembly check

After assembly check the circuit carefully to make sure all parts are soldered and correct. The device marking is labeled on the schematic and assembly drawing.


## IC Solder Test

Check that a diode drop to 0V is present from a circuit board pad that is connected to each of the pins of the IC's. Measure with a DMM's diode test. Consult the schematic to determine which pins can be skipped (e.g. ground, power rail, A/B RS485 lines...).


## Bias

Setup a current limited supply with 5V and about 20mA limit. Connect the supply to the Tranceiver VCC input (J2 pin1) and 0V (J2 pin4). Measure the input current.

``` 
{ "TXCVR_IN_CURR_mA":[1.9,] }
``` 

Connect the supply to the Buffer UART_IOREF input (J1 pin3) and 0V (J1 pin1). Measure the input current.

``` 
{ "IOFFBUF_IN_CURR_mA":[1.7,] }
``` 

## USBuart 

Connect a USBuart and use its 17mA current source to drive the 485tx_en buffer. Open the port and measure the voltage on UART_IOREF input (J1 pin3). Verify echo on RX (note receiver is on).

```
picocom -b 38400 /dev/ttyUSB1
...
Terminal ready
asdf
```

``` 
{ "UART_IOREF_AT_17mA_V":[4.7,] }
``` 


