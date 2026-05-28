f=open("myfile.txt")


# wholeFile=f.readlines() # readlines() method reads all the lines of a file and returns a list of lines. it returns an empty list when the end of the file is reached.
# print(wholeFile)


# line1=f.readline()
# line2=f.readline()
# line3=f.readline()
# line4=f.readline()
# line5=f.readline()
# line6=f.readline()


# print(line1)
# print(line2)
# print(line3)
# print(line4)
# print(line5)
# print(line6)  #readline() method reads one line at a time. it returns an empty string when the end of the file is reached.

line=f.readline()
while(line!=""):  #this loop will continue until the end of the file is reached. when the end of the file is reached, readline() method will return an empty string and the loop will terminate.
    print(line)
    line=f.readline()



f.close()

# notes: realine return string 
#  realines return list of lines
