class animals:
    pass

class pet(animals):
    pass

class dog(pet):
    @staticmethod
    def bark():
        print("Woof! Woof!")

a=dog()
a.bark()        