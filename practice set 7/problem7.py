n=int(input("enter a number: "))

noOfSpace=n-1
noOfStar=1
i=0

for i in range(0,n):
    for j in range(0,noOfSpace):
        print(" ",end="")
    for k in range(0,noOfStar):
        print("*",end="")
    print()
    noOfSpace-=1
    noOfStar+=2