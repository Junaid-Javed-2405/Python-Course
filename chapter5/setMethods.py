#  Method of set

# add() method is used to add an element to the set
s={1,2,3,"JJ","KK",1.5} 
s.add(6) # this will add 6 to the set
print(s) # this will print {1, 2, 3, 'JJ', 'KK', 1.5, 6}

# len() method is used to get the number of elements in the set
print(len(s)) # this will print 7       

# remove() method is used to remove an element from the set
s.remove(1) # this will remove 1 from the set

#  clear() method is used to remove all the elements from the set
s.clear() # this will remove all the elements from the set
print(s) # this will print set() which is an empty set


#  pop() method is used to remove and return an arbitrary element from the set
s={1,2,3,"JJ","KK",1.5} 
print(s.pop()) # this will remove and return an arbitrary element from the set
print(s) # this will print the remaining elements in the set    

# pop ( is not recommended to use because it removes an arbitrary element from the set and we do not know which element will be removed

