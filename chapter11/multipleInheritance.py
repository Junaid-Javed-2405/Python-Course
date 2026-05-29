# this inheritance is used when a class is derived from more than one base class. The derived class inherits the properties and behaviors of all the base classes. This is also known as multiple inheritance. In multiple inheritance, the derived class can access the attributes and methods of all the base classes. The syntax for multiple inheritance is as follows:


# class DerivedClass(BaseClass1, BaseClass2, ...):
#     # body of the derived class


class employee:  #base class
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")                                                                                     

class department:
    def __init__(self,department_name):
        self.department_name=department_name

    def get_department(self):
        print(f"Department: {self.department_name}")

class programer(employee, department): #derived class

    def __init__(self,name,age,salary,programming_language,department_name ):
        super().__init__(name,age,salary) #super() is used to call the constructor of the base class and it is used to initialize the attributes of the base class in the derived class.
        self.programming_language=programming_language
        self.department_name=department_name

    def get_details(self):
        super().get_details() #super() is used to call the method of the base class and it is used to access the attributes and methods of the base class in the derived class.
        print(f"Programming Language: {self.programming_language}")
        self.get_department()

p1=programer("JJ",25,50000,"Python","CS")
p1.get_details()    