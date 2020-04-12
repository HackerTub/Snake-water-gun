import random
import time

list = ["s", "w", "g"]
list1=["snake","water","gun"]
h_score=0
c_score=0
chance = 10
print("!!GAME!!\nSNAKE | WATER | GUN]n enter E to exit")

while chance > 0:
    print('\nchoose \ns for SNAKE\nw for WATER\ng for GUN')
    ch = input()
    cmp = random.choice(list)
    if ch=="e" or ch=="E":
        break
    for i in list1:
        time.sleep(0.2)
        print(i,end="  ")
        time.sleep(0.3)
    print("\nYOU-->",ch,"COMPUTER-->",cmp,"\n")
    if ch == "s" and cmp == "w":

        h_score = h_score+1
        print("!!YOU WIN !!\n YOUR SCORE=",h_score,"  COMPUTER SCORE",c_score)

    elif ch=="s" and cmp=="g":
        c_score=c_score+1
        print("!!COMPUTER WINS !!..\n YOUR SCORE=",h_score,"  COMPUTER SCORE",c_score)
    elif ch=="w" and cmp=="g":
        h_score=h_score+1
        print("!!YOU WIN !!\n YOUR SCORE=",h_score,"  COMPUTER SCORE",c_score)
    elif ch=="w" and cmp=="s":
        c_score=c_score +1
        print("!!COMPUTER WINS !!..\n YOUR SCORE=",h_score,"  COMPUTER SCORE",c_score)
    elif ch=="g" and cmp=="s":
        h_score = h_score +1
        print("!!YOU WIN !!\n YOUR SCORE=",h_score,"  COMPUTER SCORE",c_score)
    elif ch=="g" and cmp=="w":
        c_score = c_score +1
        print("!!COMPUTER WINS !!..\n YOUR SCORE=",h_score,"  COMPUTER SCORE",c_score)

    else:
        print(" !!TIE!! \nYOUR SCORE=",h_score,"  COMPUTER SCORE",c_score)


    chance = chance - 1
    print("CHANCES LEFT ->",chance)
if h_score>c_score:
    print('\n\n!!!!!!YOU WIN !! !!!!')
elif h_score<c_score:
    print("\n\n!!COMPUTER  WINS!!")
else:
    print('\n\n!!TIE!!')

