"""
 Guess the number that computer make up.
"""
import random

def play(player, turns, random_number):
    print("",player, " it is your turn.") 
    your_guess = input("Enter a number between 1 and 100: ")
    if random_number == int(your_guess):
        print("",player," won!")
        print("Number of turns",player," used:", turns)
        return True
    else:
        if random_number > int(your_guess):
            print(player," , your Guess was low, Please enter a higher number")
        else:
            print(player," , your guess was high, please enter a lower number")
        return False

random_number1 = random.randint(1, 100)
random_number2 = random.randint(1,100)
turns = 0
print(random_number1)
print(random_number2)
player_1 = input("Player 1, please enter your name: ")
player_2 = input("Player 2, please ebter your name: ")

while True:
    turns += 1
    if(play(player_1, turns, random_number1)): break
    if(play(player_2, turns, random_number2)): break
