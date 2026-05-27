#  function is a block of code which only runs when it is called. we can pass data, known as parameters, into a function. a function can return data as a result.

# funcction defination
def greet():
    print("Hello, welcome to my channel")


#Function call
greet()



# Average function
def avg():  #defining a function
    a=int(input("Enter a marks:"))
    b=int(input("Enter a marks:"))
    c=int(input("Enter a marks:"))
    average=(a+b+c)/3
    print(f"The average of three marks is {average}")

# Function call
avg()