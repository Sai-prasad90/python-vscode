reclen = 10

with open('cities.bin',"wb") as f:
    n = int(input("enter number of users"))
    for i in range(n):
        name = input("enter name")
        name = name + (reclen-len(name)) * ' '
        name = name.encode()
        f.write(name)

