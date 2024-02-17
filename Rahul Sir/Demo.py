#
# # #=========================
# # #day1
# # print("sai")  #sai
# # print("I am learning py")  #I am learning py
# # print("100+100")  #100+100
# #
# # print(100+100)  #200
# # print(100-100)  #0
# # print(100*100)  #10000
# # print(100/100)  #1.0
# # print(100%100)  # 0
# # print(100+100)  #200
# #
# # print('India will become superpower')  #India will become superpower
# # print('It's a cold day')
# # # Error single quote
# # print("gandhiji said,"i didnt said many things")
# # # Error mismatched quotes in "gandhiji said,"i didnt said many things"
# # #==========================
# # #day2-Variables
# # # print is a function
# # #  inside the () is called the Argument
# # #  we change the Argument to get different o/p
# # #  print is used to print the contents/argument as it is  , if it is inside
# # #  '' or " " or ''' '''
# # #
# # #     print('This is a new day')  #This is a new day
# # #     print("It's my book")       #It's my book
# # #     print('''gandhiji said,"you must speak truth"''')  #gandhiji said,"you must speak truth"
# #
# # # # Variables in Python
# # x = 100
# # print(x) #100
#
# # # allowed Variables
# i_am  =100
# i_am_  =100
# _i_am_  =100
# _i__am_  =100
# _1_1 =100
# #
# # print(_1_1)
# #
# # # not allowed
# # '''
# # @cool_boy = 100
# # $$193@123 = 100
# # 123 = 500
# # 1_200 =200
# # **123** = 200
# #
# # '''
# #
# # # allowed but not recommended
# # # avoid use of dunder Variables
# # __gaurav__ = "fun"
# # print(__gaurav__)
# # __gaurav__ = "not fun"
# # print(__gaurav__)
# #
# # #=================
# # #day3-data type
# # # variable assignment
# #
# # x = 100
# # y = 200
# # z = 300
# # print(x)
# # print(y)
# # print(z)
# #
# # x = "Ramesh"
# # print(x)
# #
# # # assigning the values to multiple variable in a single line
# # a,b,c = 20,30,40 #not recommended , poor readability
# #
# # print(a)
# # print(b)
# # print(c)
# #
# # # using id()
# #
# # s1 = 100
# # s2 = 100
# #
# # print(s1)
# # print(s2)
# #
# # print(id(s1))
# # print(id(s2))
# #
# # s1 = 300
# # print(id(s1))
# # print(id(s2))
# #
# # # Intro to strings Data type
# # # anything under
# # # ''
# # # " "
# # # ''' '''
# #
# # name  = "Nilesh"
# # print(name)
# # print(type(name))
# #
# # x = 100
# # print(type(x))
# #
# # pi = 3.1417
# # print(type(pi))
# #
# # z = "100"
# # print(type(z))
# #
# # # find the data type in the below eg
# # x = " "
# # y = ""
# # z = " ; "
# #
# # print(type(x))
# # print(type(y))
# # print(type(z))
# #
# # #================================
# # #day 4-string
# # # Escape character
# # #  /U
# # #  /t add a TAB
# # #  /n add a NEW LINE
# #
# # print(r"C:\Users\RAHUL\Documents\OneDjango\Hello\static")
# # print(r"C:\tanmay\Documents\OneDjango\Hello\static")
# # print("C:\\nilesh\Documents\OneDjango\Hello\static")
# #
# #
# # print("Ramesh , Suresh , Nitin")
# # print("Ramesh")
# # print("Suresh")
# # print("Nitin")
# #
# # print("Ramesh , \nSuresh , \nNitin")
# #
# # # Index
# # #         01234
# # name  =  "NAVIN"
# #
# # print(name)
# # print(name[0])
# # print(name[1])
# # print(name[5])
# #
# # #===============================
# # #day 5-string
# #
# # # Indexing
# # #         0123456
# # greet =  "WELCOME"
# # print(type(greet))
# #
# #
# # print(greet[0])
# # print(greet[5])
# # print(greet[1])
# #
# #
# # s = "It's a nice day"
# # print(s[2])
# # print(s[4])
# # print(s[5])
# #
# #
# # # # Slicing
# #
# # # var_name[start:end] wil go for n-1
# # # #         0123456
# # greet =  "WELCOME"
# #
# # print(greet[3:6])
# # print(greet[3:8])
# # print(greet[3:])
# # print(greet[:7])
# # print(greet[:3])
# #
# # #==============================
# # #day 6
# #
# # email = "MINSKOLE@GMAIL.COM"
# #
# # # Indexing
# # print(type(email)) #<class 'str'>
# # print(email)
# # print(email[8])
# # print(email[14])
# #
# # # Slicing
# # # var[start:stop] , n-1 stop value
# #
# # print(email[9:13])#GMAI
# # print(email[9:14])#GMAIL
# #
# # # Slicing with JUMP Values
# # # var_name[start:end:JUMP] wil go for n-1
# #
# # #         0123456
# # greet =  "WELCOME"
# #
# # print(greet[0:7:1])# no changes in skip value = 1
# # print(greet[0:7:2])# skip value = 2
# #
# # num = "0123456789"
# # print(type(num))
# # # even num from above string
# # print(num[0:10:2])
# # # odd num from above string
# # print(num[1:10:2])
# #
# # print(num[1:10:3])
# #
# # # Negative Indexing
# #
# # greet =  "WELCOME"
# # print(greet[3])
# # print(greet[-4])
# #
# # # for string revesal
# #
# # print(greet[::-1])# Skip value = -1
# #
# # # palindrome
# # name =  "Prakash"
# # print(name[::-1])
# #
# # # to get the last character in the string
# # s1 = "We are learning Python v3"
# # print(s1[-1])
# # s2 = "We are learning Python v4"
# # print(s2[-1])
# #
# # num_telephone = "022-22876345"
# # print(num_telephone[0:3])
# # print(num_telephone[3:4])
# # print(num_telephone[3])
# #
# #
# # #=======================
# # #day 7 -string method
# #
# #
# # greet =  "WELCOME"
# # print(greet)
# # print(greet[-1])
# # print(greet[-4:-1])
# # print(greet[-4:])
# # print(greet[-4:-2])
# # print(greet[-4:0])
# #
# #
# # # how to find the length of the string ??
# # # using len() method
# # s1 = "We are learning Python v3"
# # s2 = "We are learning Python v4"
# #
# # print(len(s1))
# # print(len(s2))
# # print(s1[24])
# # print(s2[24])
# #
# # greet =  "WELCOME"
# # # methods are pre written codes
# # # functions
# # # editing related methods
# #
# # name = "UmAkAnt"
# # print(type(name))
# #
# # # title()  Converts the first character of each word to upper case
# #
# # print(name.title())
# #
# # hobby = "to play Football"
# #
# # print(hobby.title())
# #
# #
# # # capitalize()	Converts the first character to upper case
# #
# # print(hobby.capitalize())
# # text = "hello word"
# # print(text.capitalize())
# #
# #
# # # casefold()		Converts string into lower case
# # #  it is   more aggressive
# #
# #
# # text = "HELLO wOrld"
# # print(text.casefold())
# # text2 = "HÉLLÔ WÖRLD"
# #
# #
# #
# # # lower()
# # text3 = "HELLO wOrld"
# # print(text3.lower())
# #
# #
# #
# # # swapcase()		Swaps cases, lower case becomes upper case and vice versa
# #
# # text  = "Hello World"
# # print(text.swapcase())
# #
# # # upper()			Converts a string into upper case
# #
# # text = "hello World"
# #
# # print(text.upper())
# #
# # # strip , to remove extra spaces leading and trailing
# # place  = "       Pune"
# # print(place.strip())
# #
# # fav = "i Love           Pune"
# # print(fav.strip())
# #
# # pin = "          400076         "
# # print(pin.strip())
# #
# # # boolean methods
# # # split
# #
# # # boolean methods
# # # True or False
# #
# # # endswith()		Returns true if the string ends with the specified value
# #
# # s = "Today is Monday"
# #
# # print(s.endswith("monday"))
# # print(s.endswith("Monday"))
# #
# # x = s.casefold()
# # print(x)
# # print(x.endswith("monday"))
# #
# # print(s.casefold().endswith("monday")) #we can use one method after another
# #
# # # isalnum()		Returns True if all characters in the string are alphanumeric
# #
# # p = "abc@123"
# # print(p.isalnum())
# #
# # q = "abc123"
# # print(q.isalnum())
# #
# # # isalpha()		Returns True if all characters in the string are in the alphabet
# #
# # ans = "pass123"
# # print(ans.isalpha())
# #
# # ans = "Password"
# # print(ans.isalpha())
# #
# # # find()			Searches the string for a specified value and returns the position of where it was found
# # text = "OpenAI is an artificial intelligence research organization."
# #
# #
# # print(text.find("OpenAI"))
# # print(text.find("google")) #-1 if the string is absent
# # print(text.find("artificial"))
# #
# # # index()			Searches the string for a specified value and returns the position of where it was found
# # print(text.index("OpenAI"))
# # print(text.index("artificial"))
# # # print(text.index("google")) #ValueError
# #
# # # replace()		Returns a string where a specified value is replaced with a specified value
# # s = "Today is weekend"
# # print(s.replace("weekend","weekday"))
# # print(s)
# #
# #
# # # strip()			Returns a trimmed version of the string
# # name = "           Prakash"
# # print(name.strip())
# #
# #
# # # split()			Splits the string at the specified separator, and returns a list
# #
# # s = "Today is weekend"
# # print(s.split(" "))
# #
# # email = "minskole@gmail.com"
# # print(email.split("@"))
# #
# # print(type(s))
# # print(type(email.split("@")))
# #
# # #===========================
# # #day 8 -
# # text = "this Is THE new ground for upCOMING matches"
# # print(text.title())
# # print(text.capitalize())
# # print(text.upper())
# #
# #
# #
# # # # boolean methods
# # # # True or False
# #
# # # # endswith()		Returns true if the string ends with the specified value
# #
# # s = "Today is Monday"
# # print(s.endswith("Monday"))
# # print(s.endswith("monday")) #case sensitive
# #
# # x = s.casefold()
# # print(x)
# # print(x.endswith("monday"))
# #
# #
# # # # isalnum()		Returns True if all characters in the string are alphanumeric
# #
# # p = "abc@123"
# # print(p.isalnum())
# #
# #
# # q = "abc123"
# # print(q.isalnum())
# #
# # # # isalpha()		Returns True if all characters in the string are in the alphabet
# #
# # ans = "pass123"
# # print(ans.isalpha())
# #
# # ans = "Password"
# # print(ans.isalpha())
# #
# #
# #
# #
# # # # find()			Searches the string for a specified value and returns the position of where it was found
# # text = "OpenAI is an artificial intelligence research organization."
# #
# # print(text.find("OpenAI")) #o/p will be the index posn of starting point of that string
# # print(text.find("research")) #o/p will be the index posn of starting point of that string
# # print(text.find("pushpak")) # o/p -1 , if the string is absent
# # print("Hi")
# #
# # # # index()			Searches the string for a specified value and returns the position of where it was found
# # print(text.index("OpenAI"))
# # print(text.index("research"))
# # print(text.index("pushpak"))# if the required string is missing , the code will break
# # print("Hi")
# #
# #
# # #==============================
# # #day - 8
# # # replace()		Returns a string where a specified value is replaced with a specified value
# # s = "Today is weekend"
# # ans  = s.replace('Today','Sunday')
# # print(ans)
# # print(s)
# # print(ans)
# #
# #
# # rule = "my way is the correct way"
# # print(rule.replace('way','path'))
# #
# #
# # # strip()			Returns a trimmed version of the string , only leading and trailing spaces
# # name = "           Prakash            1  "
# # print(name.strip())
# #
# #
# #
# # # split()			Splits the string at the specified separator, and returns a list
# # email = "min@skole@gmail.com"
# # new = email.split("@")
# # print(new)
# #
# # print(type(new)) #list
# #
# #
# # s = "Today is a good day"
# # print(s.split(" "))
# #
# # print(s.split("o"))
# #
# #
# #
# # song = '''
# # Jana-gana-mana-adhinayaka, jaya he
# #
# # Bharata-bhagya-vidhata.
# #
# # Punjab-Sindh-Gujarat-Maratha
# #
# # Dravida-Utkala-Banga
# #
# # Vindhya-Himachala-Yamuna-Ganga
# #
# # Uchchala-Jaladhi-taranga.
# #
# # Tava shubha name jage,
# #
# # Tava shubha asisa mage,
# #
# # Gahe tava jaya gatha,
# #
# # Jana-gana-mangala-dayaka jaya he
# #
# # Bharata-bhagya-vidhata.
# #
# # Jaya he, jaya he, jaya he, Jaya jaya jaya, jaya he!
# #
# # '''
# #
# # print(type(song))
# # print(len(song))
# #
# # print(song.count('Bharata'))
# # print(song.casefold().count('jaya he'))
# #
# # print(song.replace('Bharata',"India"))
#
#
