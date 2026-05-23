#  list change its own value 
#  it does not create a new list like string it change the value of list by index

friend=["Ali","Ahmad","Ahsan",78,34.32,True]

friend.append("Junaid") # at last of the list insert the value
print(friend)



l1=[2,34,20,15,36,0,7,17]
l1.sort() # this will sort the list in ascending order
print(l1)

l1.sort(reverse=True) # this will sort the list in descending order
print(l1)

l1.reverse() # this will reverse the list
print(l1)   

l1.insert(5,20) #this will insert the value 20 at index 5
print(l1)


print(l1.pop(6)) # this will remove the value at index 6 and return the value that is removed
print(l1)


l1.remove(0) # this will remove the first occurence of the value 0 from the list
print(l1)