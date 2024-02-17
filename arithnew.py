
#immporting from folder


# 1st way

# import Package1.arithmatic
# arithmatic.add(5,25)
# arithmatic.sub(12,25)       #arithmatic not defined


#2nd way

import Package1.arithmatic as ab

ab.add(5,5)
ab.sub(1,5)

#3rd way

from Package1.arithmatic import *
add(12,5)
sub(2,5)


#4rth way

from Package1.arithmatic import sub
sub(1,2)