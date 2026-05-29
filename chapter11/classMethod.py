class car:
    a=1

    def show(self):
        print("This is a car")
        print(self.a) # this is instance attribute

    @classmethod
    def show_class_attribute(cls):
        print("This is a class method")
        print(cls.a) # this is class attribute    


c1=car()
c1.a=45

c1.show() #this piece of code will print the value of a=45 because here is instance attribute and instance attribute has higher priority than class attribute


# if we want to acces the class attribute we have to use the class method @classmethod and we have to use the class name to access the class attribute


car.show_class_attribute()