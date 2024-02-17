
#dictionary

listA = ["sai","wate",25,687846]
# retrive
print(listA[0])  # sai
# update
listA[1] = "prasad"
# add
listA.append("warora")
# delete
# del listA
# total number of element
print(len(listA))  # 4

# listA = ["sai","wate",25,66688]
for item in listA:
    print(item)
# sai
# prasad
# 25
# warora

for item in range(len(listA)):
    print(listA[item])
# sai
# prasad
# 25
# warora

# dict
info = {
    "firstName": "sai",
    "lastName": "wate",
    "age": 25,
    "rollNo": 6465
}
# dict does not store the value by index
q2 = info['firstName']
print(q2)  # sai
# update
info['lastName'] = "prasad"
# add
info['city'] = "indore"
print(info)
# {'firstName': 'sai', 'lastName': 'prasad', 'age': 25, 'rollNo': 6465, 'city': 'indore'}
# delete
# del info
print(len(info))  # 5

# Check whether the element is present
# looping through the list
cities = ["thane", "pune", "nagpur"]
for item in cities:
    print(item)
# thane
# pune
# nagpur
print("thane" in cities)  # True

info2 = {
    "firstName": "sai",
    "lastName": "wate",
    "age": 14
}
print("age" in info2)  # True
for item in info2:
    # print(item)
    print(item, info2[item])
# firstName sai
# lastName wate
# age 14

car = {
    "color": "black",
    "model": "gls",
    "company": "mercedes"
}
for item in car:
    print(item, car[item])
# color black
# model gls
# company mercedes

# get()
q3 = car.get("model")
# Dictionary
info = ["sai", "wate", 25, 56846]
info2 = {
    "firstName": "sai",
    "lastName": "wate",
    "age": 34,
    "skills": ["python", "html css", "javascript"]
}
print(info2)
# {'firstName': 'sai', 'lastName': 'wate', 'age': 34, 'skills': ['python', 'html css', 'javascript']}
# Dictionary stores the value by index
# print(info2[0])

# retrieve
q1 = info2['firstName']
print(q1)  # sai

# update
info2['firstName'] = "himanshi"
print(info2)
# {'firstName': 'himanshi', 'lastName': 'wate', 'age': 34, 'skills': ['python', 'html css', 'javascript']}

# add
info2['city'] = "bangalore"
print(info2)
# {'firstName': 'himanshi', 'lastName': 'wate', 'age': 34, 'skills': ['python', 'html css', 'javascript'], 'city': 'bangalore'}

# delete
# del info2
print(len(info2))  # 5

# dictionary
vehicle = {
    "color": "red",
    "type": "sedan",
    "regNo": 552
}
# get()
print(vehicle.get('regNo'))  # 552
# vehicle['regNogg']
q1 = vehicle.get("regNoo")
print(q1)  # None

# program 2  # pop()
vehicle = {
    "color": "red",
    "type": "sedan",
    "regNo": 123
}
vehicle.pop('color')
print(vehicle)
# {'type': 'sedan', 'regNo': 123}

# program 3
vehicle.clear()
print(vehicle)  # {}

# program4
student = {
    "firstName": "sai",
    "lastName": "wate",
    "age": 25,
    "skills": ["python", "typescript", "javascript"]
}
print(student)
print(type(student))  # <class 'dict'>
print("age" in student)  # True
print(student.keys())
# dict_keys(['firstName', 'lastName', 'age', 'skills'])

for key in student.keys():
    print(key)
# firstName
# lastName
# age
# skills

for val in student.values():
    print(val)
# sai
# wate
# 25
# ['python', 'typescript', 'javascript']

for k, v in student.items():
    print(k, v)
# firstName sai
# lastName wate
# age 25
# skills ['python', 'typescript', 'javascript']

country = {
    "cities": 356,
    "states": 29,
    "pincode": 1000
}
print(country['cities'])  # 356
for key in country:
    print(key, country[key])
# cities 356
# states 29
# pincode 1000

for key in country.keys():
    print(key)
# cities
# states
# pincode

for val in country.values():
    print(val)
# 356
# 29
# 1000

for k, v in country.items():
    print(k, v)
# cities 356
# states 29
# pincode 1000
