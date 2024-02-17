# program 1

f  = open("myfile2.txt","w")
str = input("Enter the name")
f.write(str)
f.close()

# program 2
f  = open("myfile2.txt","r")
e = f.read()
print(e)
f.close()


# program 3
f = open('myfile2.txt','a+')
print("Enter '@' to exist")
while str != "@":
    str = input("Enter the name")
    if str != "@":
        f.write(str + "\n")
f.close()

# program 4
f = open('myfile3.txt','a+')
print("Enter '@' to exist")
while str != "@":
    str = input("Enter the name")
    if str != "@":
        f.write(str + "\n")
f.seek(0,0)
# f.seek("offset","fromwhere")
# f.seek(10,0) # 10 bytes from start of the file
# f.seek(10,1) # 10 bytes from currect position
# f.seek(10,2) # 10 bytes starting from last
q = f.read()
print(q)
f.close()