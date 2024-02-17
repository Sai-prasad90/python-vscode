# program 1

# f = open("myfile.txt",'w')
#
# e = input('Enter the name')
#
# f.write(e)
#
# f.close()

#
# # program 2
# f = open('myfile.txt','r')
# str = f.read()
# print(str)
# f.close()
# #
# #
# # # program 3
# f = open('myfile.txt','w')
# print("Enter '@' to exit")
# while str != '@':
#     str = input("Please enter multiple names")
#     if str != '@':
#         f.write(str + "\n")
# f.close()

# program 4
f = open('myfile.txt','+a')
print("Enter '@' to exit")
while str != '@':
    str = input("Please enter multiple names")
    if str != '@':
        f.write(str + "\n")
f.seek(0,0)
str = f.read()
print(str)
f.close()