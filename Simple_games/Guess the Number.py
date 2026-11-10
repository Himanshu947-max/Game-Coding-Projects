#Guess the Number
import random as rd
import time
print("\t\t[GUESS THE NUMBER（∵）？]")
tx="Narrator: By your given range we will start the game as i will provide you hints and you have to guess the number."
for i in tx.split():
    print(i,end=" ",flush=True)
    time.sleep(0.20)
a=int(input("\t\t\t Enter lowest number for range= "))
b=int(input("Enter highest number for range = "))
print("            ")
print("|+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|")
r=rd.randint(a,b)
kp=0
tr=0
while kp!=r:
    print("Number of tries = ",tr)
    c=rd.randint(a,b)
    if c>r:
        print("HINT:- Number is smaller then ",c)
    if c<r:
        print("HINT:- Number is greater then ",c)
    kp=int(input("Give your guess now according to the hints:"))
    print("                                                          ")
    if r>kp>a:
        print("INCORRECT! It is greater then",kp)
        a=kp
    if r<kp<b:
        print("INCORRECT!! It is smaller then",kp)
        b=kp
    tr=tr+1
    if tr==0:
        print("Oops You have LOST the game (T^T) Try Again!")   
    if kp==r:
        print("Your Guess is correct . You have WON the game YAY(⁠≧⁠▽⁠≦⁠)!!")   