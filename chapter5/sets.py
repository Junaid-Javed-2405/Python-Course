#  sets

d=set() #this is empty set

s={1,2,3,4,5} # this is a set with 5 elements

# set does not allow duplicate values
s={1,2,3,4,5,1,2} # this will only store unique values
print(s) # this will print {1,2,3,4,5}

# set also contain different data types
s={1,2,3,"JJ","KK",1.5} # this set contains integers, strings and float
print(s) # this will print {1, 2, 3, 'JJ', 'KK', 1.5}   