# faulty code
def change(l,word):
    n=[]
    for item in l:
        if not (item==word):
            n.append(item.strip())
        return n

l=["JJ","Ahmad","Ali","Talha","Hassan","Anas","Anas","Anas"]
print(change(l,"an"))