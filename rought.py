class personA:
    def __init__(self,fn,ln,ag):
        self.firstName=fn
        self.lastName=ln
        self.age=ag

    def displayNameA(self):
        print(self.firstName+" "+self.lastName)

a = personA("sai",'wate',26)
a.displayNameA()