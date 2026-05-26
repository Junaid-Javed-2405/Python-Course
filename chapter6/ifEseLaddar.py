
a=int(input("Enter your age: "))

if(a>18):
    print("Your are eligible to vote")
elif(a<0):
    print("Age cannot be negative")    
elif(a==18):
    print("You are just eligible to vote")    
else:
    print("Your are not eligible to vote")    