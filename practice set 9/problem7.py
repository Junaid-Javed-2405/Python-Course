with open ("practice set 9/problem7.txt","r") as f:
    lines=f.readlines()

lineno=1
for line in lines:
    if("JJ" in line):
        print("JJ is present in the line.")
        print(lineno)  
        break
    lineno+=1
else:
    print("JJ is not present in the file.")      