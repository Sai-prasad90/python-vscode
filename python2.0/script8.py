# list comprehension
# list comprehension ----- output list
# [expression: loop: condition]

# Generating a list of multiples of 2 (table of 2)
x = [1,2,3,4,5,6,7,8,9,10]
x2 = [i * 2 for i in x]
print(x2)

# Filtering even numbers from the list
x2 = [i for i in x if i % 2 == 0]
print(x2)

# Filtering odd numbers from the list
x3 = [i for i in x if i % 2 != 0]
print(x3)

# Converting names to uppercase
names = ["samiksha", "saurabh", "jatau", "shri"]
x4 = [i.upper() for i in names]
print(x4)

# Filtering names ending with 'h' and converting them to uppercase
names = ["samiksha", "saurabh", "jatau", "shri"]
x4 = [i.upper() for i in names if i.endswith('h')]
print(x4)

# Extracting the first character from each name
names = ["samiksha", "saurabh", "jatau", "shri"]
x5 = [i[0] for i in names]
print(x5)

# Extracting 'firstName' from a list of dictionaries
x6 = [
    {"firstName": "sai", 
     "lastName": "wate", 
     "age": 26, 
     "vehicle": True},
    {"firstName": "Samiksha", 
     "lastName": "Hundey", 
     "age": 26, 
     "vehicle": False},
    {"firstName": "Chetan", 
     "lastName": "Aag", 
     "age": 25, 
     "vehicle": True},
    {"firstName": "Shreya", 
     "lastName": "Tol"}
]
x7 = [x['firstName'] for x in x6]
print(x7)

# Filtering even numbers from a list
x8 = [11, 22, 33, 44]
x9 = [x for x in x8 if x % 2 == 0]
print(x9)

# Using ternary operator to determine if a number is even or odd
x10 = ["even" if x % 2 == 0 else "odd" for x in x8]
print(x10)

# Filtering students based on age and vehicle possession
students = [
    {"firstName": "sai", 
     "lastName": "wate", 
     "age": 26, 
     "vehicle": True},
    {"firstName": "Samiksha", 
     "lastName": "Hundey", 
     "age": 26,
       "vehicle": False},
    {"firstName": "Chetan", 
     "lastName": "Aag",
       "age": 25, 
       "vehicle": True},
    {"firstName": "Shreya", 
     "lastName": "Tol", 
     "age": 25, 
     "vehicle": True}
]

# Filtering students who are 18 years old or older and have a vehicle
q3 = [i['firstName'] for i in students if i['age'] >= 18 and i['vehicle'] == True]
print(q3)

# Using ternary operator to filter students based on age and vehicle possession
q4 = [x['firstName'] if x['age'] > 18 and x['vehicle'] else None for x in students]
print(q4)

# Filtering out None values from the list
q4 = [x for x in q4 if x != None]
print(q4)
