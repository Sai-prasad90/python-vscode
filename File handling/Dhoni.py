# ================
f1 = open('dhoni.png','rb')
f2 = open('msdhoni.png', 'wb')

bytes = f1.read()
f2.write(bytes)

f1.close()
f2.close()

# ================
with open('Dhoni.txt','w') as f:
    f.write("He is good player \n")
    f.write("coz of him we won wc \n")


# with open('dhoni.txt', 'w') as f:
#     f.write("He is legendary cricketer \n ")
#     f.write("coz of him india won wc \n ")
#
# with open('dhoni.txt', 'r') as f:
#     for line in f:
#         print(line)


# ==============
# pyhton boject ---binary file --- serialization
# binary file --- python object -- deserialization

# class Emp :
#     def __init__ (self,fn,ln,ag,no)
#         self.firstname = fn
#         self.lastname = ln
#         self.age = ag
#         self.number = no
#
# import pickle
# f = open('emp.dat','wb')
# n = int(input("number of employees"))
#
# # for i in range(n):
#     fn = input("Enter firstname")
#     ln = input("Enter lastname")
#     ag = input("Enter age")
#     no = input("Enter number")
#
#     Emp(fn,ln,ag,no):


