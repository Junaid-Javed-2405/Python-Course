# Default Parameter is a parameter that takes a default value if no argument is passed during the function call. It is defined by assigning a value to the parameter in the function definition.


def greet(name , greeting="Good Day"):
    print(f"{greeting} {name}")

greet("Junaid")  # this will print "Good Day Junaid" because we have not passed any argument for the greeting parameter, so it takes the default value "Good Day"    

greet("Junaid","Hello")  # this will print "Hello Junaid" because we have passed "Hello" as an argument for the greeting parameter, so it takes the value "Hello" instead of the default value "Good Day"