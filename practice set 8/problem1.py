
def greatestNumber(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

n=int(input("Enter first Number: "))
m=int(input("Enter second Number: "))
p=int(input("Enter Third Number: "))

print(f"The greatest number among {n}, {m} and {p} is {greatestNumber(n,m,p)}")