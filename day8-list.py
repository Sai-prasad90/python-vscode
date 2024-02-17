# Initial list of cities
cities = ["pune", "mumbai", "banglore", "kolkata"]
print(cities)
# Output: ["pune", "mumbai", "banglore", "kolkata"]

# Accessing individual elements of the list
print(cities[0])
# Output: pune

print(cities[1])
# Output: mumbai

print(cities[2])
# Output: banglore

print(cities[3])
# Output: kolkata

# Loop through the list using range
for x in range(len(cities)):
    print(cities[x])
# Output:
# pune
# mumbai
# banglore
# kolkata

# Program 2 - List of countries
countries = ["india", "argentina", "uae", "UK"]
for x in range(len(countries)):
    print(countries[x])
# Output:
# india
# argentina
# uae
# UK

# Program 3 - List of fruits
fruits = ["apple", "mango", "banana", "grapes"]
for a in fruits:
    print(a)
# Output:
# apple
# mango
# banana
# grapes

# Program 4 - Variable assignments
a = 10
print(a)
# Output: 10

b = a
print(b)
# Output: 10

b = 900
print(b)
# Output: 900

print(a)
# Output: 10

# Lists and variable assignments
listA = [11, 22, 33]
print(listA)
# Output: [11, 22, 33]

listB = listA
print(listB)
# Output: [11, 22, 33]

# Changing the value in listB
listB[0] = 99
print(listB)
# Output: [99, 22, 33]

# Note: Since listB is assigned to listA, changing listB also affects listA
print(listA)
# Output: [99, 22, 33]
