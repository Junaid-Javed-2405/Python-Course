d={}

name=input("Enter your name: ")
lang=input("Enter your language: ")

d.update({name:lang})
name1=input("Enter your name: ")
lang1=input("Enter your language: ")

d.update({name1:lang1})
name2=input("Enter your name: ")
lang2=input("Enter your language: ")

d.update({name2:lang2})
name3=input("Enter your name: ")
lang3=input("Enter your language: ")

d.update({name3:lang3})


print(d)

# if key will be same then it will update the value of that key instead of creating a new key. For example, if we enter the same name for name and name1, then it will update the value of that name instead of creating a new key.