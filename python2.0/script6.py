fruits = ["apple","mango","banana","watermelon","lemon","guava","mango"]
fr = fruits
fr[0] = "kiwi"
print(fr)
print(fruits)

#append
fruits.append("grapes")
print(fruits)

#pop
fruits.pop()
print(fruits)

#pop index
fruits.pop(1)
print(fruits)

#remove
fruits.remove("lemon")
print(fruits)


# clear
fruits.clear()
print(fruits)

#count
a1 = fruits.count('mango')
print(a1)

# reverse 
fruits.reverse()
print(fruits)

# insert
fruits.insert(3,"avacado")
print(fruits)

# sort
fruits.sort()
print(fruits)

