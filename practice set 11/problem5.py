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


v1=vector(2,3)
v2=vector(4,5)
v3=v1+v2
v4=v1*v2
print(v3)       