a=input("Enter number 1: ")
b=input("Enter number 2: ") 

print("The number 1 is: ", a)
print("The number 2 is: ", b)

# this sum is always return the string so a+b will be contatenate so we have to use the function of the type casting 

print("the sum before type cast is : ", a+b)

# after type casting
print("The sum after type cast is: ", int(a)+int(b))