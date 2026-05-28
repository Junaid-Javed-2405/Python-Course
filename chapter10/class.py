#  class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.


# defining a class
class student:
    name="JJ"  #this is class attribute present in the class and can be accessed by all the objects of the class
    program="CS"
    rollno="m053"


# creating an object of the class
s1=student()
print(s1.name)
print(s1.program)
print(s1.rollno)    

s1.salary=50000 #this is object(instances) attribute which is specific to the object s1 and cannot be accessed by other objects of the class
print(s1.salary)