with open("practice set 9/oldFile.txt","r") as f:
    content=f.read()

with open("practice set 9/newFile.txt","w") as f:    
    f.write(content)    


    # This code reads the content of "oldFile.txt" and writes it to "newFile.txt".
    # here we use module to delete the file content and write new content in it.
    # we learn it later