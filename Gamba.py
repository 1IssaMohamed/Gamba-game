#here are the rules for the game 
#there are 10 marbles in a abg, 5 green, 3 red, 1 black, 1 white

#black=10X win
#green=win same amount as you bet
#red=lose same amount as you bet
#white=lose 5X that you bet

#marbles reset after each round, so the probabilites are constant
#you start with x money and decide how much draws youre going to do 
#before each draw you decide how much youre gonna bet
#game auto ends if you lose half your money that you start with 

#print data as you go through
from random import randint
import random
bag=['red','red','red','green','green','green','green','green','white','black']
random.shuffle(bag)
mulla=int(input("how much money you gon start with?"))
rounds=int(input("how many rounds are you going to gamble?"))
start=mulla
end=mulla*.5
print(f"You will be forced to stop if you get under ${mulla*.5}.\nBe careful!")
for x in range(rounds):
    bet=int(input(f"how much are you going to bet in round #{x+1}?"))
    while(bet>mulla):
        bet=int(input("you dont got the facilities for that buddy, retry"))
    x=randint(0,10)
    if mulla<end:
        break
    elif bag[x]=='red':
        print(f"you got red so you lose ${bet}")
        mulla-=bet
    elif bag[x]=='green':
        print(f"you got green so you win ${bet}")
        mulla+=bet
    elif bag[x]=='white':
        print(f"you got whtie so you lose ${bet*5}")
        mulla-=bet*5
    elif bag[x]=='black':
        print(f"you got black so you win ${bet*10}")
        mulla+=bet*10
    print(f"you have ${mulla} remainig")
if mulla>end:
    print("Congrats on completing the game!")
    if mulla>start:
        print(f"you went up {mulla-start}!")
    else:
        print(f"unfourtanately, you lost {start-mulla}.")
else:
    print(f"I warned you...\nYou have ${mulla} remaining, you lose! ")

    