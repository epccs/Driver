# Description

Some lessons I learned doing K3.

# Table Of Contents:

2. [^1 NMOS Source And Drain Flip](#1-nmos-source-and-drain-flip)
1. [^1 Enable Current Source](#1-enable-current-source)


## ^1 NMOS Source And Drain Flip

I count at least three excuses so far... But, had a good helping of fresh beets during lunch, I have seen that they lower blood pressure, I think they also lower irritability. Anyway, what ever the reason mistakes happen and need to be found and fixed. Q28 source and drain need to be flipped, but Q26 is history.

![NMOS Source Drain Flip](16276^1,NmosSourceDrainFlip.png)


## ^1 Enable Current Source

To save power I want to be able to turn off the test current when not using the boost supply. 

![Enable CC Sch](16276^1,E3BiasCS.png)
![Enable CC Board](16276^1,E3BiasCSBoard.png)

Also, I'm going to ditch the external PMOS, the storage power can be discharged on a coil, and it is not a general purpose supply.





