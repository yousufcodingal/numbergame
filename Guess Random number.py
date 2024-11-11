import time 
import random

number = random.randint(1,100)
def intro():
    print("May i ask your name")
    global name 
    name = input()
    print(name+", we are gonna play a game. I am thinking a number between 1-100.")
    if(number%2==0):
        x = 'even'
    else:
        x = 'odd'
    print("\n this is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead.guess!")

def pick():
    guesses=0
    while guesses < 6:
        time.sleep(.25)
        enter = input("guess: ")
        try:
            guess=int(enter)
            if guess <= 100 and guess >= 1:
                guesses = guesses+1
                if guesses<6:
                    if guess<number:
                        print("number you have entered is to low")
                    if guess>number:
                        print("number you have entered is to high")
                    if guess != number:
                        time.sleep(.5)
                        print("try again")
                    if guess == number: 
                        break
            if guess>100 or guess<1:
                print("number not in range")
                time.sleep(.25) 
                print("please enter a number 1-100")
        except:
            print("i dont think "+enter+"is a number.sorry")
    if guess == number:
        guesses = str(guesses)
        print("good job! {} you gussed the number in {} guesses".format(name,guesses))
    if guess != number:
        print("no, the number i was thinking was "+str(number))
playagain = "yes" 
while playagain == "yes" or playagain == "y" or playagain == "YES":
    intro()
    pick()
    print("Do u want to play again")
    playagain = input()