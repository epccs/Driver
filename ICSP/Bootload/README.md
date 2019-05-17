# Bootload

## Overview

This program will run "make bootload" rule on the Pi Zero when the switch on BCM5 is pressed. Pressing the swithc on BCM13 will set a flag that ends the program with one last press on BCM5.

To install the scrip from the GitHub repository.

```
[mkdir bin]
cd bin
wget https://raw.githubusercontent.com/epccs/Driver/master/ICSP/Bootload/bootld.py
chmod ugo+x bootld.py
```

Login to the R-Pi using SSH and then cd into the folder where the make rule is and run this program. The terminal should show all the action.

```
# starting from remote host
ssh icsp1.local
cd Samba/git/RPUno/i2c-debug
python ./bin/bootld.py
# now when I push the switch (S1) on BCM5 the "make bootload" rule runs.
# push the switch (S3) on BCM13 to end this program with the next BCM5 event.
```