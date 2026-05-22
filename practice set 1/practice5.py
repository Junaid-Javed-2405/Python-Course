import os

# directory choose
directory_path='/'

# add content of directory to a list
content=os.listdir(directory_path)
#  print the content of the directory
for n in content:
 print(n)