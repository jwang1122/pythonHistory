# Black Jack: Part 3 - The Player

## Involved Class
```
Card; 
BlackJackCard; 
Deck
Player
```

## Involved test code
```
CardTestOne.py
test_card.py
DackTestOne.py
test_deck.py
PlayerTestOne.py
```

Write a Player Class that has the following methods in it:
```
addCardToHand( Card temp )
resetHand()
hit()
setWinCount( int numWins )
getWinCount()
getHandSize()
getHandValue()
```
The Player class should have a list to hold the Cards in the player’s hand and an int to store the winCount. You should also have the following dunder function:

```py
__repr__(self):
    return "hand = " + hand + " - # wins " + winCount
```

For the hit method, the player will always hit when the hand value is less than or equal to 10 and will always not hit when the hand value is more than or equal to 20. Otherwise, there is a 50/50 chance for the Player to hit.
```py
class Player:
    def __init__(self):
        pass
    
    def addCardToHand(self, card):
        pass

    def getHandValue(self):
        pass

    def hit(self):
        pass
    
```

Use the PlayerTestOne module to test what you wrote

```py
from card import *

p1 = Player()
deck = Deck()
deck.shuffle()

p1.addCardToHand(deck.nextCard())
p1.addCardToHand(deck.nextCard())

print(p1)
print("hand value:")
print(p1.getHandValue())

p1.addCardToHand(deck.nextCard())
p1.addCardToHand(deck.nextCard())

print(p1)
print("hand value:")
print(p1.getHandValue())

print(p1.hit())
```

Remember that you should use your already written Card, BlackJackCard, and Deck class.

SAMPLE OUTPUT

your Player.__repr__(self): should have simillar output as below
```
hand=[THREEofDIAMONDS|value=3,FOURofCLUBS|value=4]- #wins0 handValue
7

hand = [THREE of DIAMONDS | value = 3, FOUR of CLUBS | value = 4, SEVEN of SPADES | value=7,NINEofCLUBS|value=9]- #wins0
handValue
23
false

hand = [TWO of DIAMONDS | value = 2, TWO of CLUBS | value=4,JACKofSPADES|value=10]- #wins0
```

Do you want to hit?(Y or N)false

```
hand = [TWO of DIAMONDS | value = 2, TWO of CLUBS | value=4,JACKofSPADES|value=10]- #wins0
```
Do you want to hit?(Y or N)true
```
hand = [TWO of DIAMONDS | value = 2, TWO of CLUBS | value=4,JACKofSPADES|value=10]- #wins0
```
Do you want to hit?(Y or N)false
hand = [TWO of DIAMONDS | value = 2, TWO of CLUBS | value=4,JACKofSPADES|value=10]- #wins0
```
Do you want to hit?(Y or N)true
