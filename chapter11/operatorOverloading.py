class temp:
    def __init__(self,n):
        self.n=n

    def __add__(self,other):# this is a special method which is used to overload the + operator
        return self.n + other.n    


a= temp(5)
b=temp(10)
print(a+b) 