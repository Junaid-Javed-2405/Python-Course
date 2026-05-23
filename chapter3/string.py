# single quotes
a='jj'
# double quotes
b="JJ"
# triple quotes for multi  line string
c='''jj
junaid javed
JJ'''

print(a)
print(b)
print(c)

# string slicing
name="Junaid"
# String is mutiable so we can not change anything in the original string
# we have to store the new string in the new variable


# this will print the first 6 character of the string 0-5
name2=name[0:6]
print(name2)

# this will print the first 3 character of the string 0-2
name3=name[0:3]
print(name3)

# this will print the charcter from start to give index
name4=name[:3]
print(name4)

#this will print the charcter from given index to end of the string
name5=name[3:]
print(name5)


# negative indexing
# this will print the last character of the string
# -1 is the last character of the string and -2 is the second last character of the string and so on
name6=name[-1]
print(name6)