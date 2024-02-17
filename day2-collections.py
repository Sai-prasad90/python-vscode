# program 1
x = 10
print(x)
print(type(x))
# 10, -90,0

# program 2

x1 = 10.9
print(x1)
print(type(x1))
#12.4 , 55.6 , 0.56

# program 3
z = True
print(z)
print(type(z))
# True or False

# program 4
d = "sai"
print(d)
print(type(d))
# "A","a","123@sda"," "


#collection
# 1. String
# 2. List
# 3. Tuple
# 4. Set
# 5. Dictionary

# String
a = "robert"
print(a)
print(type(a))
# Output:
# robert
# <class 'str'>

# List (multiple elements under one memory)
city = ["pune", "chandrapur", "nasik"]
print(city)
roll_No = [84, 995, 85, 45, 61]
print(roll_No)
print(type(city))
print(type(roll_No))
# Output:
# ['pune', 'chandrapur', 'nasik']
# [84, 995, 85, 45, 61]
# <class 'list'>
# <class 'list'>

# Tuple (fixed length, always under round brackets)
fruits = ("mango", "banana", "orange", "kiwi")
print(fruits)
print(type(fruits))
# Output:
# ('mango', 'banana', 'orange', 'kiwi')
# <class 'tuple'>

# Set (does not allow duplicates)
names = {"sai", "chetan", "saurya", "alok", "chetan"}
print(names)
print(type(names))
# Output:
# {'alok', 'saurya', 'chetan', 'sai'}
# <class 'set'>

# Dictionary
info2 = ["sai", "prasad", 25, 9011212430]
info3 = {
    "firstName": "sai",
    "lastName": "prasad",
    "age": 25,
    "contactNo": 9011212430
}
print(type(info3))
print(info2)
# Output:
# <class 'dict'>
# ['sai', 'prasad', 25, 9011212430]
