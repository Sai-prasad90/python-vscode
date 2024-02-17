# program 1

years = [2000, 1995, 1988, 1992]
resulting_values = []  # Placeholder for resulting values

# Calculate values and append
for year in years:
    value = 2050 - year
    resulting_values.append(value)

print(resulting_values)  # Output: [50, 55, 62, 58]


# program 2

data = [30, 42, 60, 75, 55, 80, 65, 70, 85, 50]
above_70 = []  # Placeholder for values above 70

# Find values above 70
for value in data:
    if value > 70:
        above_70.append(value)

print(above_70)  # Output: [75, 80, 85]


# program 3

numbers_list = [88, 77, 88, 99, 88, 99, 00, 99, 00, 88]
index_list = []  # Placeholder for indices of 88
odd_indices_elements = []  # Placeholder for elements at odd indices

# Find indixes of 88
for index in range(len(numbers_list)):
    if numbers_list[index] == 88:
        index_list.append(index)

# Remove elements '
for index in range(len(numbers_list)):
    if index % 2 == 0:
        continue
    odd_indices_elements.append(numbers_list[index])

print(odd_indices_elements)  # Output: [77, 99, 99, 99, 88]


# program 4

items = [4, 8, 12, 16, 20, 24]
total_sum = 0
sum_odd_indices = 0

# Calculate the sum of all elements
for item in items:
    total_sum = total_sum + item

print(total_sum)  # Output: 84

# Calculate the sum of elements
for index in range(len(items)):
    if index % 2 == 0 and index != 0:
        sum_odd_indices = sum_odd_indices + items[index]

print(sum_odd_indices)  # Output: 36
