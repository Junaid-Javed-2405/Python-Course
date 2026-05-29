class complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    
    def __add__(self,other):
        real=self.real+other.real
        imaginary=self.imaginary+other.imaginary
        return complex(real,imaginary)
    
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
    
    
c1=complex(2,3)
c2=complex(4,5)
c3=c1+c2
print(c3)
