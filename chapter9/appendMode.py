f=open("myfile.txt","a") # open file in append mode
f.write("\nThis is a new line.") # write to the file
f.close() # close the file

# append mode is used to add new data to the end of the file without overwriting the existing data. when we open a file in append mode, the file pointer is placed at the end of the file. if the file does not exist, it will be created.