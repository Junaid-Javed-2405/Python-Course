class calculator:
    n=0
    def __init_(self,n):
        self.n=n
        

    def square(self):
        return self.n**2

    def cube(self):
        return self.n**3

    def square_root(self):
        return self.n**0.5


c1=calculator(4)
print(c1.square())
print(c1.cube())
print(c1.square_root())        