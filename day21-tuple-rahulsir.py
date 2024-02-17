# Original list using square brackets (mutable list)
list_fruits = ['apple', 'mango', 'guava', 'chiku', 'apple', 'banana']
list_num = [11, 22, 33, 44, 55]
list_alnum = [11, 'a', 22, 'e', 33, 'i']

print(list_fruits)
print(type(list_fruits))

# Converting list to tuple using parentheses (immutable tuple)
list_fruits = ('apple', 'mango', 'guava', 'chiku', 'apple', 'banana')
print(list_fruits)
print(type(list_fruits))

list_alnum = (11, 'a', 22, 'e', 33, 'i')
print(list_alnum)
print(type(list_alnum))

# Trying to modify a tuple (will raise an error)
# list_num.append(66)  # Uncommenting this line will result in an error
# print(list_num)

# Accessing elements of a tuple
print(list_fruits[0])

# Tuples with different data types
tup_one = (11, 22, 33, 44)
print(tup_one)

tup_two = (11, 22, 33, [1, 2, 3, 4, 5])
print(tup_two)

tup_three = (11, 22, 33, [1, 2, 3, 4, 5], (2, 4, 6, 8))
print(tup_three)

# Methods in Tuple
print(tup_one.index(11))  # Index of the first occurrence of 11
print(tup_one.index(44))  # Index of the first occurrence of 44
print(tup_one.count(44))  # Count occurrences of 44
print(tup_three.count(2))  # Count occurrences of 2 in the third tuple
print(tup_three[3][4])  # Accessing element inside a nested list

# Packing and Unpacking
tup_fruits = ('apple', 'mango', 'guava', 'chiku', 'apple', 'banana')  # Packing
print(tup_fruits[0])  # Accessing the first element
print(tup_fruits[3])  # Accessing the fourth element
print(tup_fruits[4])  # Accessing the fifth element

a, b, c, d, e, f = tup_fruits  # Unpacking
print(a)  # Output: apple
print(c)  # Output: guava
