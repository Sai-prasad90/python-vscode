# Single Inheritanc
class father:
    def __init__(self,fn,ln):
        self.firstname =  fn
        self.lastname = ln
    def display(self):
        print(self.firstname+self.lastname)

class son(father):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.ffname = ffn
    def display1(self):
        print(self.firstname+self.lastname)

saurabh = son("saurabh","bhoyar","deepakrao")
print(saurabh.firstname)
print(saurabh.lastname)
print(saurabh.ffname)
saurabh.display()
saurabh.display1()

#---------------------
# Multi-level
class GrandFather:
    def _init_(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayGName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def _init_(self, fn, ln,ffn):
        super()._init_(fn, ln)
        self.fname = ffn

    def displayFName(self):
        print(self.fname + self.lastName)

class Son(Father):
    def _init_(self, fn, ln, ffn,ssn):
        super()._init_(fn, ln, ffn)
        self.sname = ssn
    def displaySName(self):
        print(self.sname + self.lastName)

sai = Son("anna","wate","waman","saiprasad")

print(sai.firstName)
print(sai.lastName)
print(sai.sname)
print(sai.fname)

sai.displayFName()
sai.displayGName()
sai.firstName()

# program 3
# Herarchical inheritance
class Mother:
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):
        print(self.firstName + self.lastName)


class Son(Mother):
    def __init__(self, fn, ln, ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def displaySname(self):
        print(self.sname + self.lastName)

class Daughter(Mother):
    def __init__(self, fn, ln, dn):
        super().__init__(fn, ln)
        self.dname = dn

    def displayDname(self):
        print(self.dname + self.lastName)

abhi = Son("sandhya", "munje", "abhinav")
monu = Daughter("amruta", "munje", "amruta")

print(abhi.firstName)
print(abhi.lastName)
print(abhi.sname)
abhi.displaySname()
abhi.displayMName()

print(monu.firstName)
print(monu.lastName)
print(monu.dname)
monu.displayDname()
monu.displayMName() 




#multiple inheritance
class Father:
    def _init_(self, fn, ln):
        print("Father constructor called")
        self.firstName = fn
        self.lastName = ln

    def displayFName(self):
        print(self.firstName + self.lastName)


class Mother:
    def _init_(self, fn, ln):
        print("Mother constructor called")
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):
        print(self.firstName + self.lastName)


class Son(Mother, Father):
    def _init_(self, fn, ln, ssn):
        super()._init_(fn, ln)
        self.sname = ssn

    def displaySName(self):
        print(self.sname + self.lastName)


sai = Son("baba", "wate", "sai")