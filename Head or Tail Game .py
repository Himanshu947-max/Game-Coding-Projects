#Coin Toss game
import random
print("\t\t[Head Or Tail?]\t\t\t")
g=input("|\tEnter your choice Head or Tail? :")
b=g.capitalize()
ev=('Head','Tail')
a = random.choice(ev)
print("|\tThe Result of the Toss is:",a)
if a==b:
    print("|\tYay!(⁠≧⁠▽⁠≦⁠)You have won the toss!")    
if a!=b:
    print("|\tOops! :( You have lost the toss!")
if b not in (ev):
    print("|\tPlease Type your choice Correctly again -_-")    