# len() function is used to find the length of the string, list, tuple, dictionary, set etc. It returns the number of items in an object. It is a built-in function in Python.

class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)

    def __mul__(self,other):
        return vector(self.x*other.x,self.y*other.y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"
    
    def __len__(self):
        return (self.x**2 + self.y**2)**0.5 # this is the length of the vector which is calculated using the formula of the length of the vector which is sqrt(x^2 + y^2)


v1=vector(2,3)
v2=vector(4,5)
v3=v1+v2
v4=v1*v2
print(v3)       
print(v4)
print(len(v1)) # this will print the length of the vector v1 which is calculated using the formula of the length of the vector which is sqrt(x^2 + y^2)