# tuple is immutable as similar to string
# () is used for tuple
a=(1,2,3,4)
print(type(a))

# if we want to make a tuple with only one element then we have to put a comma after the element
b=(1,)
print(b[0])


# if we put nothing in the () then python will consider it as an empty tuple
c=()
print(type(c))

# if we put one element in the () without comma then python will consider it as an integer
d=(1)               
print(type(d))