# program
class Calculator:
    # class level variable
    c = 25
    def __init__(self,x,y,z):
        # instance variable
        self.x = x
        self.y = y
        self.z = z

sai = Calculator(122,133,144)
sameer = Calculator(121,131,141)
print(sai.x)
print(sai.y)
print(sai.z)
print(sai.c)

print(sameer.x)
print(sameer.y)
print(sameer.z)
print(sameer.c)
sameer.c = 90

print(sai.c)
print(sameer.c)

# program 2   // changing value of instance level variable

class CalculatorB:
    a = 25
    def __init__(self,x,y):
        self.x = x
        self.y = y

    # instance level method
    def changeX(self,change):
        self.x = change

shreya = CalculatorB(10,5)
print(shreya.x)
print(shreya.y)
shreya.changeX(45)
print(shreya.x)


class CalculatorC:
    c = 18
    def __init__(self ,x,y):
        self.x = x
        self.y = y

    @classmethod
    def changeC(cls,ch):
        cls.c = ch
chetan = CalculatorC(3,4)
print(chetan.x)
print(chetan.y)
print(chetan.c)
aditi = CalculatorC(13,14)
print(aditi.x)
print(aditi.y)
print(aditi.c)
CalculatorC.changeC(45)
print(chetan.c)
print(aditi.c)

chetan.c = 99
print(aditi.c)
print(chetan.c)


