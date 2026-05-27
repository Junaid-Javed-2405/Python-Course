# Functions with Arguments

def goodDay(name, ending):
    print(f"Good Day {name}")
    print(ending)

name=input("Enter your name: ")
goodDay(name,"Have a nice day")


# returning values from function
def add(a,b):
    return a+b

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
sum=add(x,y)
print(f"The sum of {x} and {y} is {sum}")