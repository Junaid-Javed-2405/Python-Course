word=["donkey","bad","good","loyal"]

with open("practice set 9/problem5.txt","r") as f:
    content=f.read()

for w in word:
    content=content.replace(w,"#"*len(w))

with open("practice set 9/problem5.txt","w") as f:
    f.write(content)