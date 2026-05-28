#  self is passed as a parameter to the method of the class and it is used to access the attributes and methods of the class. It is a convention to use self as the name of the first parameter of the method but we can use any name instead of self. The self parameter is automatically passed by the Python interpreter when we call a method of the class. We do not need to pass it explicitly. The self parameter is used to refer to the current instance of the class and it is used to access the attributes and methods of the class.

#  class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.


# defining a class
class student:
    name=""  #this is class attribute present in the class and can be accessed by all the objects of the class
    program=""
    rollno=""

# constructor 
    def __init__(self,name,program,rollno):  #dundar method is a special method in Python that is used to initialize the attributes of the class. It is called when an object of the class is created. The __init__ method takes self as the first parameter and it can take other parameters as well. The __init__ method is used to set the initial values of the attributes of the class when an object is created.
        self.name=name
        self.program=program
        self.rollno=rollno
        print("I am creating an object of the class student")

    def get_details(self):
        print (f"Name: {self.name}, Program: {self.program}, Roll No: {self.rollno}")


# creating an object of the class
s1=student("JJ","CS","M053")
s1.get_details()