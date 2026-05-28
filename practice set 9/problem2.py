import random

def game():
    print("You are playing a game.....")

    score=random.randint(1,100)
   

    with open("hi-score.txt") as f:
        hiscore=f.read()     
        if(hiscore==""):
            hiscore=0
        else:
            hiscore=int(hiscore)

    if(score>hiscore):
        with open("hi-score.txt", "w") as f:
            f.write(str(score))

    return score


score=game()
print("Your score is: ",score)