import random
import time
print("\t\t\t[ROCK PAPER AND SCISSOR ]")
text="Simple game , as you are already familiar with this.I am your Opponent,You have to WIN 3 rounds against me to WIN the GAME!! Best of Luck you will going need it ദ്ദി◝ ⩊ ◜.ᐟ   :"
for i in text.split():
    print(i,end=" ",flush=True)
    time.sleep(0.10)
gu=input("ROCK ! ..,PAPER! ,... SCISSOR!!: ")
gue=gu.capitalize()
ch=["Rock","Paper","Scissor"]
while gue not in ch:
    print("Please give your guess corrcetly from Rock,Paper and Scissor (¬_¬)")
    gu=input("ROOCK ! ..,PAAPER! ,... SCISSOR!!: ")
    gue=gu.capitalize()

bot=0
You=0
while bot!=3 and You!=3:
    chb=random.choice(ch)
    if chb=="Scissor" and gue=="Rock":
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
    if chb=="Scissor" and gue=="Paper":
        bot=bot+1
        print("Your Opponent replies with ",chb)
        print("Lol hahah! , You LOST!!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Paper" and gue=="Paper":
        print("Your Opponent replies with ",chb)
        print("It is a TIE!!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Paper" and gue=="Scissor":
        You=You+1
        print("Your Opponent replies with ",chb)
        print("Humph!,Fine You WON!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Rock" and gue=="Scissor":
        bot=bot+1
        print("Your Opponent replies with ",chb)
        print("Lol hahah! , You LOST!!")
        print("Your Score=",You,"Opponent Score=",bot)
    if chb=="Scissior" and gue=="Scissor":
        print("Your Opponent replies with ",chb)
        print("It is a TIE!!")
        print("Your Score=",You,"Opponent Score=",bot)
    if You==3:
        print("GGs!! You WON the game!! ٩(ˊᗜˋ*)و ♡ ")
    if bot==3:
        print("GGs!! You LOST the game!!(｡•́︿•̀｡)")
    if You!=3 and bot!=3:
        ch=["Rock","Paper","Scissor"]
        gu=input("Another Round , ROCK ! ..,PAPER! ,... SCISSOR!!: ")
        gue=gu.capitalize()
        while gue not in ch:
            print("Please give your guess corrcetly from Rock,Paper and Scissor (¬_¬)")
            gu=input("ROCK ! ..,PAPER! ,... SCISSOR!!: ")
            gue=gu.capitalize()
