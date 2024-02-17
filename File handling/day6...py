reclen = 10

with open('cities.bin',"wb") as f:
    n = int(input("enter the number of users"))
    for i in range(n):
        name = input("enter the name")
        name = name + (reclen - len(name)) * ' '
        name  = name.encode()
        f.write(name)


# program 2
reclen = 10
with open('cities.bin','rb') as f:
    n = int(input("record to read"))
    f.seek(reclen * (n-1))
    str = f.read(reclen)
    str = str.decode()
    print(str)


# program 3 ----->
# search the name in the file
import os
reclen = 10
size = os.path.getsize('cities.bin')
n = int(size/reclen)
with open('cities.bin','rb') as f:
    name = input('enter the name')
    name = name.encode()
    position = 0
    found = False

    for x in range(n):
        f.seek(position)
        str = f.read(reclen) #"ram          "
        if name in str:
            found = True
        position = position + reclen
    if found:
        print("user available")
    else:
        print("user not available")



import os
reclen = 10

size  = os.path.getsize('cities.bin')
n = int(size/reclen)
with open("cities.bin" , "r+b") as f:
    newname  = input("Enter the name")
    replace =  input("Name to replace")
    newname = newname + (reclen - len(newname)) * " "
    replace = replace + (reclen - len(replace)) * " "
    newname = newname.encode()
    replace = replace.encode()
    position = 0
    found = False
    for x in range(n):
        f.seek(position)
        str = f.read(reclen)
        print(str)
        print(replace)
        if str == replace:
            found = True
            break
        else:
            position = position + reclen

    if found:
            f.seek(-10,1)
            f.write(newname)
            print("city successfully replaced")
    else:
            print("city not found")
            # 0 - start of file
            # 1 - current position
            # 2 - end of file

