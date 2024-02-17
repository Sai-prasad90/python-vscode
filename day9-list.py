# Initial list of names
names = ["sai", "shreya", "priya"]
print(names)   # Output: ["sai", "shreya", "priya"]

# Creating a reference to the same list
names2 = names
print(names2)  # Output: ["sai", "shreya", "priya"]
print(names)   # Output: ["sai", "shreya", "priya"]

# Modifying an element in the shared list
names2[1] = "chetan"
print(names)   # Output: ["sai", "chetan", "priya"]
print(names2)  # Output: ["sai", "chetan", "priya"]

# Removing an element using the remove method
cities = ["mumbai", "banglore", "kolkata"]
cities.remove("mumbai")
print(cities)  # Output: ["banglore", "kolkata"]

# Removing an element using the pop method
cities2 = ["mumbai", "banglore", "kolkata"]
cities2.pop(1)
print(cities2)  # Output: ["mumbai", "kolkata"]

# Clearing the entire list
cities2.clear()
print(cities2)  # Output: []
#list
# Finding the index of an element in the list
# List
# Finding the index of an element in list
fruits = ["apple", "mango", "banana", "papaya", "apple", "mango", "grapes", "apple"]
q111 = fruits.index("apple", 1, 5)  # Error
q11 = fruits.index("apple")# 0
q1 = fruits.index("apple", 2)       # 4
print(q1)
a= fruits

# Reversing the list
cities = ["goa", "nagpur", "wardha", "chennai", "pune"]
cities.reverse()
print(cities)   # Output: ["pune", "chennai", "wardha", "nagpur", "goa"]

# Sorting the list
cities.sort()
print(cities)  # Output: Error (variable name is misspelled)
print(cities)   # Output: ["chennai", "goa", "nagpur", "pune", "wardha"]

# Appending an element to the list
country = ["india", "bangladesh", "srilanka", "cuba"]
country.append("thailand")
print(country)  # Output: ["india", "bangladesh", "srilanka", "cuba", "thailand"]

# Inserting an element at a specific position
country.insert(2, "china")
print(country)  # Output: ["india", "bangladesh", "china", "srilanka", "cuba", "thailand"]

# Extending one list with another
numberA = [11, 22, 33]
numberB = [44, 55, 66]
numberB.extend(numberA)
print(numberA)  # Output: [11, 22, 33]
print(numberB)  # Output: [44, 55, 66, 11, 22, 33]

# Counting occurrences of an element in the list
animals = ["dog", "lion", "tiger", "rabbit", "snake", "dog"]
q22 = animals.count("dog")
print(q22)  # Output: 2

# Copying a list and modifying the copy
h = [11, 22, 33]
j = h.copy()
j[0] = 111
print(j)  # Output: [111, 22, 33]
print(h)  # Output: [11, 22, 33]
