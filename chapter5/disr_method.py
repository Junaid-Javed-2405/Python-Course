marks={ "JJ":50, "KK":60, "LL":70 }

# items() method is used to get the key value pairs 
print(marks.items()) 

# keys() method is used to get the keys of the dictionary
print(marks.keys())

#  values() method is used to get the values of the dictionary
print(marks.values())


#update() method is used to update the dictionary
marks.update({"MM":80}) #this will add a new key value pair to the dictionary
print(marks) 

marks.update({"JJ":90}) #this will update the value of key "JJ" to 90
print(marks)

# get() method is used to get the value of a key
print(marks.get("KK")) # this will print the value of key "KK" which    



# difference in get and [] operator is that if we try to access a key that does not exist in the dictionary using [] operator it will raise a KeyError but if we use get() method it will return None instead of raising an error 

print(marks["NN"]) # this will raise a KeyError because key "NN" does not exist in the dictionary
print(marks.get("NN")) # this will return None because key "NN" does not exist in the dictionary


# pop() method is used to remove a key value pair from the dictionary
marks.pop("KK") # this will remove the key value pair with key "KK" from the dictionary