# f=open("myfile.txt")
# print(f.read())
# f.close()

# every time we open a file, we should close it after doing work

# with statement is used to open a file and automatically close it after doing work. it is a good practice to use with statement when working with files because it ensures that the file is properly closed even if an error occurs while working with the file.

with open("myfile.txt") as f:  # with statement automatically closes the file after doing work
    print(f.read()) 
# we don't need to call the close() method when using with statement because it is automatically called after the block of code inside the with statement is executed.