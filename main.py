class Animal:
    def __init__(self, name="Animal name"):
        self.name = name

    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name) 

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)  

    def make_sound(self):
        print("Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.make_sound()
cat.make_sound()