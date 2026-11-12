import random
import time
print("\t\t\t[ROCK PAPER AND SCISSIOR]")
text="Simple game as you are already familiar with this.I am your Opponent,You have to WIN 5 Times against Me to WIN the GAME!! Best of Luck you will going need it"
for i in text.split():
    print(i,end=" ",flush=True)
    time.sleep(0.10)
gu=input("ROCK ! ..,PAPER! ,... SCISSIOR!!: ")
gue=gu.capitalize()
ch=["Rock","Paper","Scissior"]
while gue not in ch:
    print("Please give your guess corrcetly from Rock,Paper and Scissior")
    gu=input("ROOCK ! ..,PAAPER! ,... SCISSIOR!!: ")
    gue=gu.capitalize()

bot=0
You=0
while bot!=5 or You!=5:
    chb=random.choice(ch)
    if chb=="Scissior" and gue=="Rock":
        You=You+1
        print("Your Opponent replies with ",chb)
        print("Humph!,Fine You WON!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Paper" and gue=="Rock" :
        bot=bot+1
        print("Your Opponent replies with ",chb)
        print("Lol hahah! , You LOST!!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Rock" and gue=="Rock":
        print("Your Opponent replies with ",chb)
        print("It is a TIE!!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Rock" and gue=="Paper":
        You=You+1
        print("Your Opponent replies with ",chb)
        print("Humph!,Fine You WON!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Scissior" and gue=="Paper":
        bot=bot+1
        print("Your Opponent replies with ",chb)
        print("Lol hahah! , You LOST!!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Paper" and gue=="Paper":
        print("Your Opponent replies with ",chb)
        print("It is a TIE!!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Paper" and gue=="Scissior":
        You=You+1
        print("Your Opponent replies with ",chb)
        print("Humph!,Fine You WON!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Rock" and gue=="Scissior":
        bot=bot+1
        print("Your Opponent replies with ",chb)
        print("Lol hahah! , You LOST!!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Scissior" and gue=="Scissior":
        print("Your Opponent replies with ",chb)
        print("It is a TIE!!")
        print("Your Score=",You,"Opponent Score=",bot)
    if You==5:
        print("GGs!! You WON the game!! ")
    if bot==5:
        print("GGs!! You LOST the game!! ")
        break
    ag=input("Another Round , ROCK ! ..,PAPER! ,... SCISSIOR!!: ")
    age=ag.capitalize()
    ch=["Rock","Paper","Scissior"]
    while age not in ch:
        print("Please give your guess corrcetly from Rock,Paper and Scissior")