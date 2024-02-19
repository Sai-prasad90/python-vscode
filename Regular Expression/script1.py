# \d - 0-9
# \w - A-Z a-z 0-9
# \b - space around
# \A - startwith
# \Z -endswith
# \W - non alpha numaric


import re

str = "sam man can wan run fun gun mum mon sun"
 #print start with m
a = re.search(r'm\w\w',str)  #r - raw string
print(a) #<re.Match object; span=(4, 7), match='man'>
print(a.group()) #man
if a:
    print(a.group())
else:
    print("doesnt found")
#run mum sun
b= re.search(r'\wun',str)
if b:
    print(b.group()) #run
else:
    print("not found")


#program2

str1 = "man,,fam,fan,sum,sun,run,ran,rum"
#ends with m
c = re.search(r'\w\wm',str1)
if c :
    print(c.group()) #sum
else:
    print("not found")

d = re.findall(r'f\w\w',str1)
print(d) #['fam', 'fan']
#end with
c1 = re.findall(r'\wan',str1)
print(c1)  #['man', 'fan', 'ran']

#program2   match
day = "mon tue wed thu fri sat sun"
q = re.match(r"s\w\w",day)
if q:
    print(q.group()) #while using match it should be at star of string
else:
    print("not found") #not found


#program 4
str3 = "A 'good' coder; always know python's regular expresssion"
#W as it alphanumaric
q2 = re.split(r'\W+',str3) #means non alphanumaric folloed by  any charector
print(q2) #['A', 'good', 'coder', 'always', 'know', 'python', 's', 'regular', 'expresssion']

info = "sai :9011212430"
print( re.split(r'\W+',info)) #['sai', '9011212430']
#
# program 5 #sustitute - replace
str4 = "My main domain is javascript"
q = re.sub(r'javascript','python',str4)
print(q)