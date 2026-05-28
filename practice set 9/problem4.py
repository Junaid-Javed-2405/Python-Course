word="donkey"

with open("practice set 9/donkey.txt","r") as f:
    content=f.read()

newContent=content.replace(word,"######")

with open("practice set 9/donkey.txt","w") as f:
    f.write(newContent)