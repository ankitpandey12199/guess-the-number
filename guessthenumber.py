
#from math import radians
import random

def gameLevel():
    print("enter the level of game:")
    print("press 1 for easy ")
    print("press 3 for medium ")
    print("press 3 for difficult ")
    a=input()
    if(a=='1'):
        return random.randint(0,20)
    elif (a=='2'):
        return random.randint(20,50)
    else:
        return random.randint(50,100)

def guesser( n):
    count=1
    
    while True:
       a=input("\nguess  the number:")
       a=int(a)
       if a==n:
          print("you guessed in "+str(count)+" attempts .")
          return
       elif a<n:
          print("too low ,guess higher")
       else:
          print("too high ,guess lower")  
       count+=1;

play =1
while play==1:
    a=gameLevel()
    guesser(a)
    play=input("do you want to play again?? if yes print 1 else 0:")


    

    

