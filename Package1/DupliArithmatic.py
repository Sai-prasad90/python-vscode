

import arithmatic     #first way

arithmatic.add(8,15)
arithmatic.sub(12,16)

#2ndway
import arithmatic as cal #giving new name

cal.add(5,4)
cal.sub(16,14)

#3rd way

# from arithmatic import *   #imports all mehtods
from arithmatic import add  #imports specific method
add(25,6)
# sub(15,15)  #not deined

from arithmatic import add,sub
add(12,25)
sub(12,85)


