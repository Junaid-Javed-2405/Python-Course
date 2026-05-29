class employee:
    a=1

class department(employee):
    b=2

class programer(department):  
    c=3


p1=programer()
print(p1.a) # this is inherited from employee class
print(p1.b) # this is inherited from department class   
print(p1.c) # this is present in programer class


p2=department()
print(p2.a) # this is inherited from employee class     
print(p2.b) # this is present in department class
