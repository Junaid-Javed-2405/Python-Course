a=(1,2,3,4,"jj","kk",True,34.32)
print(a)
print(type(a))


# count the given element in the tuple
print(a.count("jj"))

# index of the given element in the tuple only first occurrence
print(a.index(34.32))

# tuple lenght 
print(len(a))

# tuple slicing is as same in the string slicing
print(a[0:4])           

# minimum in the tuple if tuple is truly numeric otherwise it will give error
t=(1,2,3,4)

print(min(t))

# if we want to find the minimum in the tuple with some non numeric element then we have to use slicing to get only numeric element and then find the minimum
print(min(a[0:4]))


# same for maximum in the tuple 
print(max(t))

#  sum function is used to find the sum of all the numeric element in  the tupple
print(sum(t))