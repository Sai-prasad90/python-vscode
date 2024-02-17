# Program 1
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tableOfTwo = []

# Using a for loop to iterate over each element in the list and multiply it by 2
for item in x:
    tableOfTwo.append(item * 2)

# Print the result
print(tableOfTwo)

# Program 2
# Using list comprehension to achieve the same result as Program 1 in a more concise way
q3 = [item * 2 for item in x]
print(q3)

# Program 3
birthYear = [1989, 1990, 1991, 1992]
ages = []

# Calculating the age for each birth year using a for loop
for x in range(len(birthYear)):
    ag = 2023 - birthYear[x]
    ages.append(ag)
print(ages)

# Using list comprehension to achieve the same result as Program 3
ages2 = [2023 - item for item in birthYear]
print(ages2)

# Program 4
marks = [33, 44, 66, 88, 34, 55, 67]
above40 = []

# Filtering marks greater than 40 using a for loop and if condition
for item in marks:
    if item > 40:
        above40.append(item)
print(above40)

# Using list comprehension to achieve the same result as Program 4
above40two = [item for item in marks if item > 40]
print(above40two)

# Program 5
square = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using list comprehension to calculate the square of each element
squares = [item * item for item in square]
print(squares)

# Program 6
names = ["chinmay", "sarika", "pooja", "ram", "satish"]

# Using list comprehension to convert each name to uppercase
capitalNames = [item.upper() for item in names]
print(capitalNames)

# Program 7
numbersB = [33, 444, 5, 6]

# Using list comprehension to create a list with "even" for even numbers and "odd" for odd numbers
even = ["even" for item in numbersB if item % 2 == 0]
print(even)
