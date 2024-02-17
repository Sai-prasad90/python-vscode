
numbers = [11,22,33]
print(numbers[0])       #11
print(type(numbers))    #list


names = ["apple","banana","mango","pinapple","wattermelon"]
print(names)      #it will print array
print(names[2])   # mango
print(names[4])   #watttermelon

# # mixed
mixedArray = ["sai","warora",9011212430,True ] #array allows all types string int floa boolean
#

# Creating a list of cities
cities = ["lukhnow", "banaras", "ayodhya", "prayagraj"]

# Finding the length of the list
q1 = len(cities)
print(q1)  # Output: 4 (length of the list)
print(type(q1))  # Output: <class 'int'> (type of q1)

# Retrieving an element from the list
print(cities[0])  # Output: lukhnow

# Updating an element in the list
cities[0] = "delhi"
print(cities)  # Output: ['delhi', 'banaras', 'ayodhya', 'prayagraj']

# Adding an element to the end of the list
cities.append("lukhnow")
print(cities)  # Output: ['delhi', 'banaras', 'ayodhya', 'prayagraj', 'lukhnow']

# Deleting an element using pop method
cities.pop(2)
print(cities)  # Output: ['delhi', 'banaras', 'prayagraj', 'lukhnow']

# Deleting an element using remove method
cities.remove("lukhnow")
print(cities)  # Output: ['delhi', 'banaras', 'prayagraj']

# Looping through elements in the list
for city in cities:
    print(city)
# Output: delhi
#         banaras
#         prayagraj

# Checking if an element is available in the list
print("delhi" in cities)  # Output: True
print("agra" in cities)   # Output: False

# Conditional check in a list
if "agra" in cities:
    print("City available")
else:
    print("City not available")
# Output: City not available

