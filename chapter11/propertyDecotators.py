class car:
    a=1

    def show(self):
        print("This is a car")
        print(self.a) # this is instance attribute

    @classmethod
    def show_class_attribute(cls):
        print("This is a class method")
        print(cls.a) # this is class attribute    

    @property
    def owner_name(self):
        return f"{self.fName} {self.lName} is a owner of this car"

    @owner_name.setter
    def owner_name(self,name):
        self.fName=name.split(" ")[0]
        self.lName=name.split(" ")[1]    


c1=car()
c1.owner_name="Junaid Javed"

print(c1.owner_name) # this is instance attribute


car.show_class_attribute()