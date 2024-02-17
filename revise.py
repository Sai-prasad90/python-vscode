# # list
# # dictionary
# # tuple
# # set
#
# #list
# country = ["india","japan","indonasia","uae","denmark"]
# print(country[3]) #uae
# print(len(country)) #5
# country[2]="russia"
# print(country) #['india', 'japan', 'russia', 'uae', 'denmark']
# country.append("thailand")
# print(country) #append at last
# country.pop(2)
# print(country) #indo gone
# print(type(country)) #list
# country = ["india","japan","indonasia","uae","denmark"]
# if "japan" in country:
#     print("yes.Japan is there")#
# else:
#     print("Japan not found")
# country = ["india","japan","indonasia","uae","denmark"]
# country2=country
# print(country2)
# country2.reverse()
# print(country)
# country2.sort()
# print(country2) #abcd
# country=["india","china","thailand","korea","nepal"]
# country2=["uea","usa","canada","russia"]
# country.extend(country2)
# print(country)
#
# country3=['india', 'china', 'thailand', 'korea', 'nepal', 'uea', 'usa', 'canada', 'russia']
# # for i in country3:
# #     if i[0] == 'u':
# #         print(i) #starts with u
# for i in range(len(country3)):
#     if country3[i][0] == 'u':
#         print(country3[i])
#
# marks = [11, 22,44, 33, 55, 66]
# for i in marks:
#     if i > 40:
#         print(i)
# for i in range(len(marks)):
#     if marks[i] > 40:
#         print(marks[i])
#
# score = [5,6,0,2,7,6,8]
# a=0
# for items in score :
#     a= a+items
#     print(a) #34
#
# for num in score:
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
#
# score = [3, 8, 1, 4, 6, 7, 2]
# i = 0
# while i < len(score):
#     find = score[i]
# #
# #     if find % 2 == 0:
# #         print("even")
# #     else:
# #         print("odd")
# #     i = i+1
# #
# #
# # #dictionry
# # emp = {
# #     "name":"shreya",
# #     "age":28,
# #     "field":"interior",
# #     "Contact":90112430,
# #     "city":"nagpur"
# # }
# # a=emp["field"]
# # print(a) #single
# # a=emp["city"] = "pune"
# # print(emp)#city updated
# # a=emp["experiance"]="fresher"
# # print(emp) #key value added
# # copied_dict = emp.copy()
# # print("Copied Dictionary:", copied_dict)
# # age = emp.get("age")
# # print(age) #28
# # key = emp.keys()
# # print(key)
# # values = emp.values()
# # print(values)
# # key,value = emp.popitem()
# # print(key,value)
# # print(emp)
# # emp = {
# #     "name":"abhijit",
# #     "age":29,
# #     "field":"IT",
# #     "Contact":90112430,
# #     "city":"pune"
# # }
# # for key, value in emp.items():
# #     print(key , value)
# # for i in emp:
# #     emp.update({"company": "outscal"})
# # print(emp)
# emp = [
#     {
#         "name": "abhijit",
#         "age": 32,
#         "field": "IT",
#         "Contact": 90112430,
#         "city": "pune"
#     },
#     {
#         "name": "shivani",
#         "age": 29,
#         "field": "IT",
#         "Contact": 90112430,
#         "city": "banglore"
#     },
#     {
#         "name":"shreya",
#         "age":28,
#         "field":"interior",
#         "Contact":90112430,
#         "city":"nagpur"
#     }
# ]
#
# # for abc in emp:
# #     if "banglore" in abc['city']:
# #         print(abc['name'])
# #         break
# # else:
# #     print("Not found")
#
# for i in range(len(emp)):
#     if "banglore" in emp[i]['city']:
#         print(emp[i]['name'])
#
# i = 0
# while i < len(emp):
#     if emp[i]['age'] < 30:
#         print(emp[i]['name'])
#     i = i + 1

#tuple
tup = ("sai",28,"pune","shreya",26,"pune","priya",31,"pune")
# for i in tup:
#     print(i)
pune = 0
for i in range(len(tup)):
    if tup[i] == "pune":
        pune = i + 1
print(pune)

abc = ()
i = 0

while i < len(tup):
    if tup[i] != "pune":
        abc = abc + (tup[i],)
    i = i + 1

print(abc)
#string
# a="Guava is not only tasty but also good for health,"
# b="Eating guava is aiding in digestion and promoting a feeling of fullness."
# i = a + b
# print(i) #concaaaatt


