"""
 Guess the number that computer make up.
"""
import random

def play(player, turns, random_number):
    print("",player, ", it is your turn.") 
    your_guess = input("Enter a number between 1 and 100: ")
    if random_number == int(your_guess):
        print("",player," guessed the number! ", random_number)
        print("Number of turns",player," used:", turns)
        return True
    else:
        if random_number > int(your_guess):
            print(player," , your guess was low, please enter a higher number")
        else:
            print(player," , your guess was high, please enter a lower number")
        return False

random_number1 = random.randint(1, 100)
random_number2 = random.randint(1, 100)
turns1 = 0
turns2 = 0
print(random_number1)
print(random_number2)
player_1 = input("Player 1, please enter your name: ")
player_2 = input("Player 2, please enter your name: ")

while True:
    turns1 += 1
    turns2 += 1
    if (play(player_1, turns1, random_number1)):
            if (play(player_2, turns2, random_number2)): 
                print("Both players tied!")
                break
            else:
                print(player_1, "won!")
                break
    else:
        if (play(player_2, turns2, random_number2)):
            print(player_2, "won!")
            break
print("Game over")
