# Define a function named addA that takes two parameters x and y and returns their sum.
def addA(x,y):
    return x + y 

# Call the addA function with arguments 23 and 5, store the result in variable e.
e = addA(23,5)

# program 1
# Define a function named addition that takes three parameters: fn (a function), x, and y.
def addition(fn,x,y):
    # Call the function represented by fn with arguments x and y, store the result in variable e.
    e = fn(x,y)
    # Return the result stored in e.
    return e

# Define a lambda function named add that takes two parameters and returns their sum.
add = lambda x,y: x+y

# Call the addition function with the add lambda function, 12, and 4 as arguments, store the result in variable result.
result = addition(add,12,4)
# Print the result.
print(result) # Output: 16

# program 2
# Define a lambda function named sub that takes two parameters and returns their difference.
sub = lambda x,y: x-y

# Define a function named subtraction that takes three parameters: fn (a function), a, and b.
def subtraction(fn,a,b):
    # Call the function represented by fn with arguments a and b, store the result in variable e.
    e = fn(a,b)
    # Return the result stored in e.
    return e

# Call the subtraction function with the sub lambda function, 12, and 4 as arguments, store the result in variable result2.
result2 = subtraction(sub,12,4)
# Print the result2.
print(result2) # Output: 8

# Define a variable x and assign it the value 10.
x = 10 
# Print the value of x.
print(x) # Output: 10
# Print the lambda function sub.
print(sub) # Output: <function <lambda> at 0x...>
# Call the sub lambda function with arguments 23 and 3.
sub(23,3) # Output: 20

# program 3
# Define a function named multiplication that returns a lambda function.
def multiplication():
    # Return a lambda function that takes two parameters and returns their product.
    return lambda x,y: x*y

# Call the multiplication function and store the returned lambda function in result3.
result3 = multiplication()
# Call the lambda function stored in result3 with arguments 34 and 5, store the result in variable e2.
e2 = result3(34,5)
# Print the value of e2.
print(e2) # Output: 170
