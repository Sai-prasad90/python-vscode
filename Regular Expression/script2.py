#program 1
import re

str = "an doctor a day keeps apple away"
# a = re.findall(r'a[\w]*',str)
# print(a) #['an', 'a', 'ay', 'apple', 'away'] problem with ay
a = re.findall(r'\ba[\w]*',str)
print(a) #['an', 'a', 'apple', 'away']

str1 = "Ankit birthday is on 29th feb. Which comes once in 4 years"
a1 = re.findall(r'\d[\w]*',str1)
print(a1) #['29th', '4']

str2 = "four . three, ninety , five , seven , hundred"
x1 = re.findall(r'\b\w\w\w\w\w\b',str2)
print(x1) #['three', 'seven']
x2=re.findall(r'\b\w{5}\b',str2)
print(x2)

str43 = "four . three, ninety , five , seven , hundred"
x3=re.findall(r'\b\w{4,}',str43)
print(x3) #['four', 'three', 'ninety', 'five', 'seven', 'hundred']

str5 = "four . three, ninety , five , seven , hundred"
x4=re.findall(r'\b\w{4,5}\b',str5)
print(x4) #['four', 'three', 'five', 'seven']

str6 = "four . three, ninety , five , seven , hundred , 54 , 6"
x5 = re.findall(r'\b\d+\b',str6)
print(x5) #['54', '6']

str7 = "four . three, ninety , five , seven , hundred , 54 , 6"

x6 = re.findall(r'\bt[\w]*\Z',str7)
print(x6)
x7 = re.findall(r'\An[\w]*',str7)
print(x7)














