#list comprehension
# Table of Four
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tableOfFour = [item * 4 for item in x]
print(tableOfFour)  # [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]

# Q3
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
q3 = [item * 2 for item in x]
print(q3)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Ages
birthYear = [1989, 1990, 1991, 1992]
ages = [2023 - item for item in birthYear]
print(ages)  #  [34, 33, 32, 31]

# Marks above 40
marks = [33, 44, 66, 88, 34, 55, 67]
above40 = [item for item in marks if item > 40]
print(above40)  #  [44, 66, 88, 55, 67]

# Squares
square = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [item * item for item in square]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Capital Names
names = ["sai", "shreya", "sameer", "acchala", "gandharv"]
capitalNames = [item.upper() for item in names]
print(capitalNames)  #  ['SAI', 'SHREYA', 'SAMEER', 'ACCHALA', 'GANDHARV']

# ======================
names = ['SAI', 'SHREYA', 'SAMEER', 'ACCHALA', 'GANDHARV']
lower = [item.lower() for item in names]
print(lower)  #  ['sai', 'shreya', 'sameer', 'acchala', 'gandharv']

# ================
names = ['SAI', 'SHREYA', 'SAMEER', 'ACCHALA', 'GANDHARV']
Friend = ["mi. " + item for item in names]
print(Friend)  #['Mi. SAI', 'Mi. SHREYA', 'Mi. SAMEER', 'Mi. ACCHALA', 'Mi GANDHARV']

# ===================
numbersB = [33, 444, 5, 6]
even = ["even" for item in numbersB if item % 2 == 0]
print(even)  # ['even', 'even']

numbersB = [33, 444, 5, 6 ,21 , 22 ,66 ]
even = ["even"if  item % 2 == 0  else "odd" for item in numbersB]
print(even)


