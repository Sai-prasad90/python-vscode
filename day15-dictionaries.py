listA = ["sai","prasad",25,456]
# Retrieve
print(listA[0])  #  sai

# Update
listA[1] = "wate"
print(listA)  # ['sai', 'wate', 25, 456]
# # Add
listA.append("pune")
print(listA)   #['sai', 'wate', 25, 456, 'pune']
# # Delete
# # ==del listA
#
# # Total number of elements
print(len(listA))  #  5
#
listA = ["sai","wate",15,6788]
for item in listA:
    print(item)             #sai wate 15 6788
#
for item in range(len(listA)):
    print(listA[item])    #printsame)

# # Dictionary
info = {
    "firstName":"sai",
    "lastName":"wate",
    "age":25,
    "rollNo":655
}
# # Dictionary does not store values by index
q2 = info['firstName']
print(q2)  #  sai
#
# # Update
a=info['lastName'] = "wate"
print(a)    #wate
# # Add


info['city'] = "delhi"
print(info) #{'firstName': 'sai', 'lastName': 'wate', 'age': 25, 'rollNo': 655, 'city': 'delhi'}
#
# # Delete
# # del info

print(len(info))  #5
#
# # Check whether an element is present
# # Looping through the list

cities = ["warora","nashik","nagpur"]
for item in cities:
    print(item) #print list
print("warora" in cities)  #True

info2 = {
    "firstName":"sai",
    "lastName":"wate",
    "age":26
}
print("age" in info2)  # True
for item in info2:
    # print(item)
    print(item, info2[item]) #firstName sai lastName wate age 26
# #
car = {
    "color":"black",
    "model":"gls",
    "company":"mercedes"
}
# #
for item in car:
    print(item, car[item]) #color black model gls company mercedes

#
# # # get()
q3 = car.get("model")
print(q3) #gls