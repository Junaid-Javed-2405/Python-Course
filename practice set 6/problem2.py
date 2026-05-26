p1="Make alot of money"
p2="Click here "
p3="Subscribe this"
p4="Buy now"

a=input("Enter your comment here: ")

if(p1 in a or p2 in a or p3 in a or p4 in a):
    print("This is spam comment")
else:
    print("This is not spam")    