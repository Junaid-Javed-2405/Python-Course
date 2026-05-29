class employee:  #base class
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


class programer(employee): #derived class

    def __init__(self,name,age,salary,programming_language):
        super().__init__(name,age,salary) #super() is used to call the constructor of the base class and it is used to initialize the attributes of the base class in the derived class.
        self.programming_language=programming_language

    def get_details(self):
        super().get_details() #super() is used to call the method of the base class and it is used to access the attributes and methods of the base class in the derived class.
        print(f"Programming Language: {self.programming_language}")



p1=programer("JJ",25,50000,"Python")
p1.get_details()        