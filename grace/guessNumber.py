"""
 GRACE Y GUESS NUMBER GAME 
 Guess the number that computer make up.
 HW: Make it run twice and which run has the least number of guesses 
"""
import random

random_number = random.randint(1, 100)
win = False
Turns = 0
while win == False:
    Your_guess = input("Enter a number between 1 and 100: ")
    Turns += 1
    if random_number == int(Your_guess):
        print("You won!")
        print("Number of turns you have used: ", Turns)
        win == True
        break
    else:
        if random_number > int(Your_guess):
            print("Your Guess was low, Please enter a higher number")
        else:
            print("your guess was high, please enter a lower number")

print()

random_number = random.randint(1, 100)
win = False
Turns2 = 0
while win == False:
    Your_guess = input("Enter a number between 1 and 100: ")
    Turns2 += 1
    if random_number == int(Your_guess):
        print("You won!")
        print("Number of turns you have used: ", Turns2)
        win == True
        break
    else:
        if random_number > int(Your_guess):
            print("Your Guess was low, Please enter a higher number")
        else:
            print("your guess was high, please enter a lower number")

print()

if (Turns>Turns2):
    print ("Player two won because they guessed the least amount of times")
elif (Turns<Turns2):
    print ("Player one won because they guessed the least amount of times")
else:
    print ("You tied")
    