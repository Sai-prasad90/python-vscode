#Membership Operators:
#   - In (in)
#   - Not in (not in)
# Case sensitive

list_vo = ['A', 'E', 'I', 'O', 'U']


print("a" in list_vo)  # Output: False

print("A" in list_vo)  # Output: True

print("z" in list_vo)  # Output: False

print("a" not in list_vo)  # Output: True

print("z" not in list_vo)  # Output: True

print("A" not in list_vo)  # Output: False




# boolean o/p of data types

# Output for the given programs:

print(1)                #  1
print(type(1))          # Output: <class 'int'>
print(bool(1))          # Output: True

print(0)                # Output: 0
print(type(0))          # Output: <class 'int'>
print(bool(0))          # Output: False only for ZERO is an INTEGER

print(3)                # Output: 3
print(type(3))          # Output: <class 'int'>
print(bool(3))          # Output: True

print('0')              # Output: 0
print(type('0'))        # Output: <class 'str'>
print(bool('0'))        # Output: True

print(bool(True))       #True
print(bool(False))      # False

print(bool(''))         #False Empty will always be FALSE
print(bool(' '))        #True space is there

print(bool([1,2,3]))     #True
print(bool([0,0,0]))     #True
print(bool([0]))         #True because it array is not empty ?
print(bool([]))          # False Empty will always be FALSE

print(bool((1,2,3)))     # True
print(bool((1)))         # True

print(bool((0)))         # False as it's an INTEGER ZERO

print(bool((5-5)))        #False in arithmacit
print(bool((True-True)))  #False True - True results in 0


# print(bool((0,)))        # True (TRUE as it's a TUPLE)
# print(type((0,)))        # tuple (TRUE as it's a TUPLE)
#
# print(bool(0))           # Output: False (FALSE as it's an INTEGER ZERO)
# print(bool(00))          # Output: False (FALSE as it's an INTEGER ZERO)
# print(bool(0.0))         # Output: False (FALSE as it's an INTEGER ZERO)
#
# print(bool((0,0)))       # Output: True (TRUE as it's a tuple with elements)
# print(bool(()))          # Output: False (Empty will always be FALSE)
#
# print(bool(False))       # Output: False
# print(bool((False,False)))# Output: True
