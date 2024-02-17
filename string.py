# string
x = "hello"
y = 'baby'
print(x)  #   hell
print(y)  #   baby
print(' The quote is "Try try but do not cry" ')



a = """
    I am learning javascript and python
    I find them 90 % similar 
    "hello"
    'bye'

"""
b = '''
    I am learning javascript and python
    I find them 90 % similar 
    "hello"
    'bye'
'''
"""
    This is multiline comment
"""

# program 2

first_name = "sai"
print(first_name)  #   sai
print(type(first_name))  #   <class 'str'>
print(first_name[0])  #   s

last_name = "prasad"
print(last_name[2])  #   a
print(last_name[-4])  #   a

# for loop
# range
for i in range(len(last_name)):
    # print(i)
    print(last_name[i])

# without range
for char in first_name:
    print(char)

# while
i1 = 0
while(i1 < len(last_name)):
    # print(i1)
    print(last_name[i1])
    i1 = i1 + 1