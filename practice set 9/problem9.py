with open ("practice set 9/problem8.txt","r") as f:
    content1=f.read()


with open("practice set 9/problem8_copy.txt","r") as f:
    content2=f.read()

if(content1==content2):
    print("The content of both files is the same.")             
else:
    print("The content of both files is different.")    
    
