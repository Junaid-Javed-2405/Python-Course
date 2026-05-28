f=open("poem.txt")
data=f.read()

if("twinkle" in data):
    print("twinkle is present in the poem.")
else:
    print("twinkle is not present in the poem.")

f.close()        