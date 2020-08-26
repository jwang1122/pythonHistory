"""
 Guess the number that computer make up.
"""
import random

player1 = input("Enter your name player1:")
player2 = input("Enter your name player2:")
print("Hello", player1)
print("Hello", player2)

random_number = random.randint(1, 100)
win = False
Turns_player1 = 0
Turns_player2 = 0
while win == False:
    print(player1, "turn")
    player1__guess = input("Enter a number between 1 and 100: ")
    

    Turns_player1 += 1
    if random_number == int(player1__guess):
        print("You won", player1)
        print("Number of turns you have used: ", Turns_player1)
        win == True
        break
    else:
        if random_number > int(player1__guess):
            print("Your Guess was too low, Please enter a higher number")
        else:
            print("your guess was too high, please enter a lower number")
    print(player2, "turn")
    player2__guess = input("Enter a number between 1 and 100: ")
    Turns_player2 += 1
    if random_number == int(player2__guess):
        print("You won", player2)
        print("Number of turns you have used: ", Turns_player2)
        win == True
        break
    else: 
        if random_number > int(player2__guess):
            print("Your Guess was too low, Please enter a higher number")
        else:
            print("your guess was too high, please enter a lower number")

    
    

    

    
        
