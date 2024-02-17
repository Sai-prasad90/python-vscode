#conditional statement

# conditional statement always use in the case of one input and multiput output

#only if time consuming as it goes through all steps even if condition excecuted before
# Purchase Discount Scenario
purchase = 4000

# Using multiple if statements to determine the discount
if purchase > 0 and purchase <= 1000:
    print("5% off")
if purchase > 1000 and purchase <= 2500:
    print("10% off")
if purchase > 2500:
    print("25% off")
# Output: 25% off

# Using if-elif-else statements to determine the discount
if purchase > 0 and purchase <= 1000:
    print("5% off")
elif purchase > 1000 and purchase <= 2500:
    print("10% off")
elif purchase > 2500:
    print("25% off")
else:
    print("potato")
# Output: 25% off

# Grading based on marks
marks = 79

# Using multiple if statements to determine the grade
if marks >= 90 and marks <= 100:
    print("You have secured Grade A")
if marks >= 75 and marks < 90:
    print("You have secured Grade B")
if marks >= 50 and marks < 75:
    print("You have secured Grade C")
if marks >= 45 and marks < 50:
    print("You are Pass")
# Output: You have secured Grade B
# You have secured Grade C

# Using if-elif-else statements to determine the grade
marks = 15

if marks >= 90 and marks <= 100:
    print("You have secured Grade A")
elif marks >= 75 and marks < 90:
    print("You have secured Grade B")
elif marks >= 50 and marks < 75:
    print("You have secured Grade C")
elif marks >= 45 and marks < 50:
    print("You are Passe")
else:
    print("Better luck next time")
# Output: Better luck next time

# Comparing values of a and b
a = 25 + 36
b = 12 + 0

if a > b:
    print("a is greater")
else:
    print("b is greater")
# Output: a is greater

# Ternary operator for comparing c and d
c = 25
d = 12
print("c is greater") if c > d else print("d is greater")
# Output: c is greater

# Ternary operator for comparing e and f
e = 2 * 5
f = 5 * 5
print("e is greater") if 3 * e > 2 * f else print("f is greater")
# Output: f is greater
