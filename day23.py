# program 1
# Defining a function 'add' that takes two parameters and returns their sum
def add(x, y):
    return x + y

# Calling the 'add' function with arguments 12 and 4, storing the result in 'q1'
q1 = add(12, 4)
# Printing the result of the addition
print(q1)

# program 2
# Creating a lambda function 'add' that takes two parameters and returns their sum
add = lambda x, y: x + y
# Calling the lambda function with arguments 13 and 4, storing the result in 'q2'
q2 = add(13, 4)
# Printing the result of the lambda function
print(q2)

# program 3
# Creating a lambda function 'sqr' that takes one parameter and returns its square
sqr = lambda x: x * x
# Calling the lambda function with argument 2, storing the result in 'e'
e = sqr(2)
# Printing the result of the lambda function
print(e)

# program 4
# Defining a function 'additionAll' that takes any number of arguments and returns their sum
def additionAll(*args):
    print(args)
    total = 0
    # Summing up all the arguments
    for i in args:
        total = total + i
    return total

# Calling the 'additionAll' function with multiple arguments, storing the result in 'f'
f = additionAll(12, 33, 44, 55, 66, 77, 88, 99, 100, 101)
# Printing the result of the addition
print(f)

# program 5
# Defining a function 'updateCity' that takes keyword arguments and modifies 'city' to "nashik"
def updateCity(**kwargs):
    print(kwargs)
    kwargs['city'] = "nashik"
    return kwargs

# Calling the 'updateCity' function with keyword arguments, storing the result in 'f2'
f2 = updateCity(fullName="sai", city="pune", age=27)
# Printing the updated keyword arguments
print(f2)

# program 6
# Defining a function 'addition' with default values for parameters
def addition(x=4, y=6):
    print(x + y)

# Calling the 'addition' function with default values and specific values
addition()
addition(1, 2)

# program 7
# Defining a function 'addition' with parameters in a different order
def addition(x3, x2, x1):
    print(x3 + x2 + x1)
    print(x3)

# Calling the 'addition' function with named arguments
addition(x1=3, x2=4, x3=10)
