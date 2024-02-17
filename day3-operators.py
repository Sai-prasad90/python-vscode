# Operators
# 1.Arithmatic Operations
# 2.Comparision Operations
# 3.Logical Operations


#arithmatic
# + - * / % are arithmatic operators
a = 5
b = 9
print(a+b)
A = 70
W = 25
print(A+W)
print(A-W)
print(A*W)
print(A/W)
print(A%W)
print((A+W),(A-W),(A*W),(A/W),(A%W))
SName = "Sai"
LName = " Wate"
print(SName + LName)

# Comparison Operators
# < > <= >= == != result always boolean

print(8 < 2)
print(12 > 8)
print(5 !=  58)
print(8 ==  5.52)
print(5.52 == 2)
print(0.25 >=  0.25)
print(71 <= 78)
print(9 <= 9.01)
print(12 >=  18)


#Logical Operatiots
# And True and True ===> True other all are false
# Or False or False ====> False all other are true. At least one true needed
# Not True==>False , False==>True

print(3 == 3 and 4 == 4)  # True
print(3 != 3 and 4 == 4)  #  False
print(3 == 3 and 4 != 4)  #  False
print(3 != 3 and 4 != 4)  #  False

# Logical OR Operations
print(3 == 3 or 4 == 4)   #  True
print(3 != 3 or 4 == 4)   #  True
print(3 == 3 or 4 != 4)   # True
print(3 != 3 or 4 != 4)   #  False

# Logical NOT Operations
print(not(6 == 3))  # True
print(not (6 == 6))  #False