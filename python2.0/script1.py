#day1
# x = 10
# print(x)
# x = 100
# print(x)

# # program 2
# a = 4
# b = 4

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# def Calculator(x1,y1):
#     print(x1+y1)
#     print(x1-y1)
#     print(x1*y1)
#     print(x1/y1)
#     print(x1%y1)

# Calculator(4,5)
# Calculator(2,4)

# # program 3
# # function without parameter and without return  type
# def add():
#     print(5+5)
# add()
# add()
# add()
# add()

# # function with parameter and without return type 

# def sub(a1,b1):
#     print(a1-b1)
# sub(2,4)
# sub(5,3)
# sub(0.25,3)


# # function with parameter and with return 

# def mult(x5,y5):
#     return x5 * y5
# a = mult(554,34)
# print(a)
# print(a / a)
# print(a % a)


# day2 

# a = 85
# print(a)
# print(type(a))


# b = 00.28
# print(b)
# print(type(b))

# c = True
# print(c)
# print(type(c))


# d = "sai"
# print(d)
# print(type(d))



# print(6 > 3)
# print(6 < 3)
# print(6 >= 3)
# print(6 <= 3)
# print(6 >= 6)
# print(6 <= 6)
# print(6 != 6)
# print(7 == 7)

# # logical operator
# # and  
# # True  and True   =====> True

# print(5 == 5 and 6 == 6)
# print(7 == 8 and 9 == 9)
# print(6 == 6 and 8 == 9)
# print(8 == 9 and 9 == 8)

#day 3
# logical operator 
# and 
#  true   and   true    -------> true 

print(6 == 6  and 51 == 51 )
print(60 != 60 and 15 == 15 )
print(14 == 14 and 26 == 70)
print(2 == 8 and 9 == 8 )
# or
# false   or    false  ===> false
print(6 == 6  or 51 == 51 )
print(60 != 60 or 15 == 15 )
print(14 == 14 or 26 == 70)
print(2 == 8 or 9 == 8 )

# not operator
print(not 7 == 7)
print(not 8 != 8)
print(not 7 == 6)

# conditional statements 
numT = 4

if numT > 0 and numT <= 5:
    print("10 % discount")
if numT > 5 and numT <= 10:
    print("20 % discount")
if numT > 10:
    print("30 % discount")

numT2 =  -17
if numT2 >= 0 and numT2 <= 5:
    print("5 % discount")
elif numT2 > 5 and numT2 <= 10:
    print("10 % discount")
elif numT2 > 10:
    print("20 % discounr")
else:
    print("incorrect input")

# program 3

marks = 35

if marks > 75:
    print("Grade A")
if marks >= 45:
    print("Grade B")
if marks >= 35:
    print("Grade C")

# program 4    

marks1 =85

if marks > 75:
    print("Grade A")
elif marks >= 45:
    print("Grade B")
elif marks >= 35:
    print("Grade C")
else:
    print("we are friends")


# program 5 
a = 25
b = 50

if a > b:
    print("a is greater")
else:
    print("b is greater")

# program 6 
    
x1 = 65
x2 = 64
x3 = 65

if x1 > x2 and x1 > x3:
    print("x1 is greater")
elif x2 > x1 and x2 > x3:
    print("x2 is greater")
else:
    print("x3 is greater")



















































