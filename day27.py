class Myclass:
    n = 0
    def __init__(self):
        Myclass.n = Myclass.n + 1

    @staticmethod
    def noObject():
        print(Myclass.n)

obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
obj4 = Myclass()

Myclass.noObject()