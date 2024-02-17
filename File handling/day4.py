#to check file in our directory
# model ==>single file
# multiple models ==> package
# multiple packages -->  library

import os ,sys
# print(os.path) # will give current path
name = input("Enter the filesname : ")
if os.path.isfile(name):

    f = open(name,"r")
else :
    sys.exit()
i = f.read()
print(i)
f.close()