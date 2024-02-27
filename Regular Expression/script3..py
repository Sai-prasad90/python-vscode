 
import re
#
# # program  1
# str = "saiprasad:9011212430"
# # print(str)
# # e = re.search(r'\d+',str)
# # print(e.group()) #9011212430
#
# e = re.search(r'\D+',str)
# print(e.group()) #saiprasad:
# #
# f = re.search(r'[\w]* [\w]*',str)
# if f:
#     print(f.group())
# else:
#     print("not found") #not found
#
# #=====
# str = "sai sameer shreya sanskruti sam sumit "
# g = re.findall(r'\bs[am][\w]*',str)
# print(g) #['sai', 'sameer', 'sanskruti', 'sam']
# #
# # # program 3
# str = 'shreya 19-08-1998 priya 21-05-1993'
# f = re.findall(r'\d{2}-\d{2}-\d{4}',str)
# print(f) #['19-08-1998', '21-05-1993']
# #
# # # program 4
# str2= 'shreya 19-8-1998 priya 21-5-1993'
# f = re.findall(r'\d{2}-\d{1,2}-\d{4}',str2)
# print(f) #['19-8-1998', '21-5-1993']
# #
# # # program 5
# str3  = "hello world"
# g = re.search(r'^he',str3)
# print(g.group()) #he
# #
# # # program 6
# str4  = "hello world"
# g = re.search(r'world$',str4)
# print(g.group()) #world
# #
# # #program 7
# str5  = "hello World"
# g = re.search(r'world$',str5,re.IGNORECASE)
# print(g.group()) #World
# #
# # # program 8
# students = "I got 80 marks I got 100 marks"
# print(re.findall(r'\d{2,3}',students)) #80 100
# #
# #
# students = "Sai got 80 marks Shreya got 100 marks"
# x = re.findall(r'[A-Z][a-z]*',students)
# print(x) ['Sai', 'Shreya']
# #
# #program 9
#
import re

strS = 'The morning meeting will be scheduled at 8am or 9am , evening at 8pm or 9pm'
a1 = re.findall(r'\b\d[2]*', strS)
print(a1)
