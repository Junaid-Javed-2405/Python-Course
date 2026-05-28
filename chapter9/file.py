#  files are used to store the data permanently. we can read and write data to files. we can also create and delete files.

f=open("file.txt","r") # r for read, w for write, a for append, x for create
data=f.read()
print(data)
f.close()

# default mode is read mode so there is not need to mention the r