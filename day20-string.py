# program 7
str1 = "sai"
str2 = "prasad"
print(str1 + str2)  #   saiprasad

# program 8
name = "sai wate"
age = 34
info = "My name is {} and age is {}".format(name, age)   #placeholder {}
print(info)  #   My name is sai wate and age is 34
print(f"My name is {name} and age is {age}")  #   My name is sai wate and age is 34

# program 9
info2 = "i am learning nothing"
info3 = info2.replace("nothing", "something")
print(info3)  #   i am learning something

# program 10
fruit = "apple"
info4 = fruit.startswith("a")
info5 = fruit.startswith("App")
print(info4)  #   True
print(info5)  #   False

# program 11
fruit = "papaya"
info6 = fruit.endswith("ya")
info7 = fruit.endswith("a")
print(info6)  #   True
print(info7)  #   False

# program 12
city = " istambul "
info8 = city.lstrip()
x = len(info8)
print(x)  #   8

info9 = city.rstrip()
x = len(info9)
print(x)  #   8

# program 13
city = "pune"
print(city.index("n"))  #   2
print(city.index("p"))  #   0

# program 14
listA = [11, 22, 33, 44, 55, 66]
listA[0] = 111
print(listA)  #   [111, 22, 33, 44, 55, 66]

# program 15
info9 = "sai".isalpha()
print(info9)  #   True
info10 = "446898468".isdigit()
print(info10)  #   True
print("864@".isalnum())  #   False
