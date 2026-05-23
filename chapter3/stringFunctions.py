a="junaid javed"

# tell the length of the string
print(len(a))

# tell is string starts with given string or not
print(a.startswith("junaid"))

# tell is string end with given string or not
print(a.endswith("javed"))

# captizile the first letter of the string
s="pakistan is beautiful country"
print(s.capitalize())

# find the given string in the original string and return index of first character

print(s.find(" c"))

# replace the given string with the new string
# this will replace the all occurrence of the string
print(s.replace("beautiful","wonderful"))

a="JJ"
# this print the lower case of the string
print(a.lower())

# this print the upper case of the string
print(a.upper())

# this split the string on the basis of seprator in the given string
print(s.split())
# split() will get the parameter on the basis of which it will split the string
print(s.split("i"))
# by default split() will split the string on the basis of space but we can also split the string on the basis of any character or string by passing it as a parameter in the split() function 