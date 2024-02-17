# ternary operator

score = 40

result = "passed" if score >= 40 else "try again"

print(score)
print(result)


#==========================================

#for loop

# syntax in python
# for (var) in range():
#     print(var)

# in range(starting wali position, endposition,size)
#it will not print given ended position -1

for a in range(5):
    #no negative number will printed if printonly starting index
    #it printed  0-4 coz given number is 5 ie.-1
    print(a)                               #0 1 2 3 4

#table of two
for x in range(2,21,2):
    print(x)   # Output: 2 4 6 8 10 12 14 16 18 20


# print string multiple times
for m in range(5):
    print("python is stupid ")  # Output:python is stupid x 5



# reverse
for x in range(5,0,-1):
    print(x)            # Output: 5 4 3 2 1


# table of 45
for x in range(45,451,45):
    print(x)                     # Output: 45 90 135 180 225 270 315 360 405 450


# break with for

for a in range(1,10):
    if a == 4:   #//it will stop at 3 i.e. 4-1 coz it check first
        break
    print(a)           # Output: 1 2 3

for a in range(1,10):
    print(a)     #coz it check print first
    if a ==4:
        break             # Output: 1 2 3 4

#continue

for x in range(1,20):
    if(x == 10):
        continue  #it skip 10 and continues
    print(x)      # # Output: 1 2 3 4 5 6 7 8 9 11 12 13 14 15 16 17 18 19

for x in range(10,0,-2):
    if x == 4:
        continue   # it skips 4 and continues
    print(x)    # Output: 10 8 6 2