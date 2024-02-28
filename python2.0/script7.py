names = ["sai","manish","spruha","sai"]
names2 = names
names2[0] = "shreya"
print(names)
print(names2)

  # append()
names.append("chetan")
print(names)

#pop
names.pop()
print(names)
names.pop(1)
print(names)

#remove
names.remove("manish")
print(names)

#clear
names.clear()
print(names)

#count
a  = names.count('sai')
print(a)

#reverse
names.reverse()
print(names)


# insert
names.insert(3,"anamika")
print(names)

#sort
names.sort()
print(names)

#copy
listD = names.copy()
listD[1] = "sameerr"
print(listD)
print(names)


#extend
names.extend(["samiksha","saurabh","jatau","shri"])
print(names)
b = names.index(4)
print(b)


#====
birthYear = [1165,1545,1925,2024]
age = []
for x in birthYear:
    age.append(2024 - x)
print(age)

#=====
marks = [58.25,58,12,96,95,75,35,29]
above40 = []
for x in marks:
    if x> 40:
        above40.append(x)
print(above40)

#===
numbers = [11,22,33]
sum  = 0 
for x in numbers:
    sum = sum + x
print(sum)


#=====
cities = ["pune","banglore","delhi"]
for x in cities:
    print("welcome to "+ x)

