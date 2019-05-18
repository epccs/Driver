#!/usr/bin/env python
import RPi.GPIO as GPIO
import os

# grep returns an exit-status of zero if it finds a match, and another value otherwise
if(os.system("groups | grep spi -")):
    print("this user is not in the spi group")
    print("sudo usermod -a -G spi <user>")
    exit()

if(os.system("groups | grep gpio -")):
    print("this user is not in the gpio group")
    print("sudo usermod -a -G gpio <user>")
    exit()

# bootload switch goes to BCM5
bootload_pin=5
# icsp switch goes to BCM13
icsp_pin=13

GPIO.setmode(GPIO.BCM)

use_bootload_pin_to_stop = 1

# pushing the pin will stop looping the loader but you will need to push the other pin one last time
def loaderStop_callback(channel):
    # the callback is ran as a seperate thread and apparently python makes a new value by default rather than using the global one
    global use_bootload_pin_to_stop
    if(use_bootload_pin_to_stop):
        print("icsp_pin falling event occured so use_bootload_pin_to_stop flag cleared")
        use_bootload_pin_to_stop = 0
        print("press icsp_pin again to end program")

GPIO.setup(bootload_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(bootload_pin, GPIO.FALLING, callback=loaderStop_callback)

GPIO.setup(icsp_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while (use_bootload_pin_to_stop):
        GPIO.wait_for_edge(icsp_pin, GPIO.FALLING)
        #edge detection should avoid repeated polling
        if (use_bootload_pin_to_stop):
            os.system("make linuxspi")
        #Send the Makefile rule to upload firmware over SPI hardware (e.g., avrdude -c linuxspi)
except:
    pass

GPIO.cleanup()

