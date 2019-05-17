# Shutdown

## Overview

This program will shutdown the Pi Zero when the switch on BCM6 is pressed.

I place the script in /home/rsutherland/bin and make it executable, then tell the system to run it from /etc/rc.local

```
[su rsutherland]
[mkdir bin]
cd bin
wget https://raw.githubusercontent.com/epccs/RPUpi/master/Shutdown/shutdown-sw.py
chmod ugo+x shutdown-sw.py
sudo nano /etc/rc.local
```

Follow these rc.local [recommendations].

[recommendations]: https://www.raspberrypi.org/documentation/linux/usage/rc-local.md

```
...
python /home/rsutherland/bin/shutdown-sw.py &
exit 0
```

To test run it sudo is needed.

``` 
sudo python /home/rsutherland/bin/shutdown-sw.py &
``` 
