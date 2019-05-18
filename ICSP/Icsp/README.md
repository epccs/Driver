# In Circuit Serial Programming

## Overview

This program will run "make linuxspi" rule on the Pi Zero when the switch on BCM13 is pressed. Pressing the switch on BCM5 will set a flag that ends the program with one last press on BCM13.

To install the scrip from the GitHub repository.

```
[mkdir bin]
cd bin
wget https://raw.githubusercontent.com/epccs/Driver/master/ICSP/Icsp/icsp.py
chmod ugo+x icsp.py
```

Login to the R-Pi using SSH and then cd into the folder where the make rule is and run this program. The terminal should show all the action.

```
# starting from remote host
ssh icsp1.local
cd Samba/git/RPUpi/Remote
# build the hex file befor runing the python script
make
python ./bin/icsp.py
# now when I push the switch (S3) on BCM13 the "make linuxspi" rule runs.
# push the switch (S1) on BCM5 to end this program with the next BCM13 event.
# wow that is fast, under 3 seconds.
```