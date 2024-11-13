class Animal:
    name = ""
    MIN_COORD = 0
    MAX_COORD = 100
    def __init__(self, name):
        self.name = name

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD
    @classmethod
    def test(cls):
        print("Test")
        return 0
    def defaultmet(self, name):
        print("Something")
        return self.name

    @staticmethod
    def printName(name):
        return name

    def __del__(self):
        print("Animal name is ")


cat = Animal("Cher")
print(cat.name)
print(Animal.validate(18))
print(Animal.test())
print(Animal.printName("Sara"))
cat.defaultmet("Name")