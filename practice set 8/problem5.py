
def pattern(n):
    if(n==0):
        return
    print("*"*n,end="")
    print()
    pattern(n-1)

pattern(3)            