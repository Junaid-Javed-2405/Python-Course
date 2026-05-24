s=set()

s.add(1)
s.add(1.0)
s.add("1")

print(len(s))# this will print 2 because 1 and 1.0 are considered the same element in a set, while "1" is a different element.