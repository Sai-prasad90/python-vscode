# # Program 1
class student:
    firstName = None
    lastName = None
    age = None
    rollNo = None
    def displayName(self):
        print(self.firstName + self.lastName)
#
# sai = student()
# print(sai.firstName)
# print(sai.lastName)
# print(sai.age)
# print(sai.rollNo)
# sai.displayName()none
sai = student()
sai.firstName = "sai"
sai.lastName = "sai"
sai.age = 26
sai.rollNo = 64
print(sai.firstName)
print(sai.lastName)
print(sai.age)
print(sai.rollNo)
sai.displayName()

# program 2
class Person:
    def __init__(self, fn, ln, ag, roll):   #constructor
        self.firstName = fn
        self.lastName = ln
        self.age = ag
        self.rollNo = roll

    def displayName(self):
        if self.firstName is not None and self.lastName is not None:
            print(self.firstName + " " + self.lastName)
        else:
            print("Name not available")

sai = Person("sai", "prasad", 26, 645)
shreya = Person("shreya", "tol", 19, 185)

sai.displayName()
shreya.displayName()
