# Using a for loop to iterate from 1 to 9
for x in range(1, 10):
    print(x)
# Output: 1 2 3 4 5 6 7 8 9

# Generating the table of two using a for loop
for x in range(2, 22, 2):
    print(x)
# Output: 2 4 6 8 10 12 14 16 18 20

# Reversing the loop
for x in range(5, 0, -1):
    print(x)
# Output: 5 4 3 2 1

# Generating the table of 5 in reverse using a for loop
for x in range(50, 0, -5):
    print(x)
# Output: 50 45 40 35 30 25 20 15 10 5

# Using a break statement in a for loop
for x in range(1, 10):
    if x == 3:
        break
    print(x)
# Output: 1 2

# Using a break statement in a for loop (breaks after checking condition)
for x in range(2, 22, 2):
    print(x)
    if x == 14:
        break
# Output: 2 4 6 8 10 12 14

# Using a continue statement in a for loop
for x in range(1, 6):
    if x == 3:
        continue
    print(x)
# Output: 1 2 4 5

# Using a continue statement in a for loop (skips 14)
for x in range(20, 2, -2):
    if x == 14:
        continue
    print(x)
# Output: 20 18 16 12 10 8 6 4 2


# intialization
# while(condition):
    # statement
    # increment / decrement

# Program 2: While loop to print numbers from 1 to 4
g1 = 1
while g1 < 5:
    print(g1)
    g1 = g1 + 1
# Output: 1 2 3 4

# Program 3: While loop with a break statement
g2 = 1
while g2 <= 5:
    if g2 == 3:
        break
    print(g2)
    g2 = g2 + 1
# Output: 1 2

# Program 4: While loop to print even numbers up to 20 with a break statement
g3 = 2
while g3 <= 20:
    print(g3)
    if g3 == 14:
        break
    g3 = g3 + 2
# Output: 2 4 6 8 10 12 14

# Program 5: While loop to print even numbers up to 20 with a break statement (breaks before printing 14)
g3 = 2
while g3 <= 20:
    if g3 == 14:
        break
    print(g3)
    g3 = g3 + 2
# Output: 2 4 6 8 10 12

# Program 6: While loop to print numbers from 6 to 1 with a break statement
g4 = 6
while g4 >= 1:
    print(g4)
    if g4 == 3:
        break
    g4 = g4 - 1
# Output: 6 5 4 3

# Program 7: While loop with continue statement
g5 = 1
while g5 <= 5:
    if g5 == 3:
        g5 = g5 + 1
        continue
    print(g5)
    g5 = g5 + 1
# Output: 1 2 4 5


# Program 6: While loop to print numbers from 6 to 1 with a break statement
g4 = 6
while g4 >= 1:
    print(g4)      # Output: 6 # 5 # 4 # 3
    if g4 == 3:
        break       # Breaks out of the loop when g4 is 3
    g4 = g4 - 1     # Decrementing g4 by 1 in each iteration
# Final Output: 6 5 4 3

# Program 7: While loop with continue statement
g5 = 1
while g5 <= 5:
    if g5 == 3:
        g5 = g5 + 1   # Skip the value 3 and move to the next iteration
        continue      # Continue to the next iteration without executing the remaining code
    print(g5)         # Output: 1 # 2 # 4 # 5
    g5 = g5 + 1       # Incrementing g5 by 1 in each iteration
# Final Output: 1 2 4 5
