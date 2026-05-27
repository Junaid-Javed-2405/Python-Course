# 0 for water
# 1 for snake
# -1 for gun

import random 

computer=random.choice([1,0,-1])
computer_dict={1:"snake",0:"Water",-1:"Gun"}

user=int(input("Enter 1 for snake, 0 for water and -1 for gun: "))
while(user not in [1,0,-1]):
    user=int(input("Invalid input! Please enter 1 for snake, 0 for water and -1 for gun: "))
user_dict={1:"snake",0:"Water",-1:"Gun"}

print(f"Computer Choose: {computer_dict[computer]}")
print(f"You Choose: {user_dict[user]}")

if(computer==user):
    print("It's a draw!")
elif(computer==1 and user==-1) or (computer==0 and user==1) or (computer==-1 and user==0):
    print("You win!")
else:
    print("Computer wins! \nYou lose!")