a1=int(input("Enter a marks: "))
a2=int(input("Enter a marks: "))
a3=int(input("Enter a marks: "))


total_prentage=(a1+a2+a3)/300*100

if(total_prentage>=40):
    if(a1>=33 and a2>=33 and a3>=33):
        print("You are pass")
    else:           
        print("You are fail due to less marks in one subject")
else:   print("You are fail due to less percentage")            