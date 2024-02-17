
# loop 
for x in range(1,5):
    print(x)

for x in range(6):
    print(x)

for x in range(2,21,2):
    print(x)

for x in range(50,0,-5):
    print(x)

for x in range(1,6): 
    if x == 3:
        break 
    print(x) 

for x in range(5,1,-1): 
    print(x)
    if x == 3:
        break 

for x in range(1,6): 
    if x == 3:
        continue
    print(x) 

# print 1 to 3

t1 = 1
while(t1 <= 3):
    print(t1) 
    t1 = t1 + 1 

#print 1 to 5 
t2 = 1
while(t2 <= 5):
    print(t2)
    t2 = t2 + 1

#table of 2 
t3 = 2
while t3 <= 20:
    print(t3)
    t3 = t3 + 2

#table of 5
t4 = 50
while t4 >= 5:
    print(t4)
    t4 = t4 - 5 

#break with while
t5 = 1 
while t5 <= 5:
    if t5 == 3:
        break
    print(t5)
    t5 = t5 + 1 
#====
t6 = 5
while t6 >= 1:
    print(t6) 
    if t6 == 3:
        break
    t6 = t6 - 1

# continue with while
t7 = 2
while t7 <= 5:
    if t7 == 3:
        t7 = t7 + 1
        continue
    print(t7)  
    t7 = t7 + 1   