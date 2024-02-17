# program 1

birthYear = [1989, 1990, 1991, 1992]
ages = []  # [34]

# Calculate ages and append to the 'ages' list
for x in range(len(birthYear)):
    x = 2023 - birthYear[x]
    ages.append(x)

print(ages)  # Output: [34, 33, 32, 31]


# program 2

marks = [22, 33, 44, 66, 7, 8, 99, 44, 66, 77]
above50 = []

# Find marks above 50 and append to 'above50' list
for x in marks:
    if x > 50:
        above50.append(x)

print(above50)  # Output: [66, 99, 66, 77]


# program 3

marks3 = [88, 77, 88, 99, 88, 99, 00, 99, 00, 88]
indexOf88 = []
removeEvenIndexElement = []

# Find indices of 88 in 'marks3' and append to 'indexOf88'
for item in range(len(marks3)):
    if marks3[item] == 88:
        indexOf88.append(item)

# Remove elements at even indices from 'marks3' and append to 'removeEvenIndexElement'
for item in range(len(marks3)):
    if item % 2 == 0:
        continue
    removeEvenIndexElement.append(marks3[item])

print(removeEvenIndexElement)  # Output: [77, 99, 99, 99, 88]


# program 4

marks = [11, 22, 33, 44, 55, 66]
total = 0
total2 = 0

# Calculate the sum of all elements in 'marks'
for item in marks:
    total = total + item

print(total)  # Output: 231

# Calculate the sum of elements at odd indices in 'marks'
for item in range(len(marks)):
    if item % 2 == 0 and item != 0:
        total2 = total2 + marks[item]

print(total2)  # Output: 110
