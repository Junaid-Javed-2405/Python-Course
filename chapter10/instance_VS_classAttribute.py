#  class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.


# defining a class
class student:
    name="JJ"  #this is class attribute present in the class and can be accessed by all the objects of the class
    program="CS"
    rollno="m053"


# creating an object of the class
s1=student()
s1.program="IT" #this is object(instances) attribute 
print(s1.program)

# here we get the value of program as IT because we have changed the value of program for the object s1 but if we create another object s2 and access the program attribute then we will get the value of program as CS because it is a class attribute and it is not changed for the object s2

# instance has higher pritority than the  class attribute
 