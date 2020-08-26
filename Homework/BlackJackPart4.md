# Black Jack: Part 4 – The Dealer Class
## involved classes
```
DealerTestOne
Dealer
Card
BlackJackCard
Deck
Player
```
Write the Dealer class that extends the Player class. The dealer will always hit if the hand value is less than or equal to 16. Use all the previous classes you have written.

* The Dealer Class will be
```py
# define Dealer class here 
# instance variable - Deck
# constructors 
# method to shuffle 
# method to deal a card 
# hit method goes here
```
* The DealerTestOne Class will be
```py
from card import *

dealer = Dealer()
player = Player("John")

dealer.shuffle()
    
player.addCardToHand(dealer.deal())
dealer.addCardToHand(dealer.deal())
player.addCardToHand(dealer.deal())
dealer.addCardToHand(dealer.deal())

playerTotal = player.getHandValue()
dealerTotal = dealer.getHandValue()

print("Player:")
print("Hand Value:: ", playerTotal)
print("Hand Size:: ", player.getHandSize())
print("Cards in Hand:: ", player)

print("Dealer:")
print("Hand Value:: ", dealerTotal)
print("Hand Size:: ", dealer.getHandSize())
print("Cards in Hand:: ", dealer)

if playerTotal>21 and dealerTotal<=21:
    print("Dealer wins - Player busted!")
elif playerTotal<=21 and dealerTotal>21:
    print("Player wins - Dealer busted!")
elif playerTotal>21 and dealerTotal>21:
    print("Both players bust!")
elif playerTotal<dealerTotal:
    print("Dealer has bigger hand value!")
else:
    print("Player has bigger hand value!")
```

* A Sample Output will be
```
PLAYER
Hand Value :: 13
Hand Size :: 2 John::hand=[9 of Clubs | value=9,4 of Spades | value=4] - # wins 0
DEALER
Hand Value :: 15
Hand Size :: 2
Cards in Hand :: hand = [5 of DIAMONDS | value = 5, 10 of CLUBS | value = 10] - # wins 0
Dealer has bigger hand value!
```