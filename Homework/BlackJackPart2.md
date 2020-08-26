# Black Jack: Part 2 - The Deck

## Involved Class
```
Card; 
BlackJackCard; 
Deck
```

## Involved test code
```
CardTestOne.py
test_card.py
DackTestOne.py
test_deck.py
```

## Deck Description
Write the Deck class. Deck is a collection of Card references stored in an ArrayList. Each of the Card references in the ArrayList will refer to some type of Card object. You should use your already written Card and BlackJackCard class.
Complete the Deck class
```py
class Deck:
    NUMFACES = 13
    NUMSUITS = 4
    NUMCARDS = 52

    def __init__(self):
        # initialize data - stackOfCards - topCardIndex
        self.topCardIndex = 51
        self.stackOfCards = []

        # loop through suits
		# loop through faces
		# add in a new card

    def __repr__(self):
        return 
    def setTopCardIndex(self, n):
        # setter
        pass

    def setStackOfCards(self,cards):
        # setter
        pass

    def shuffle(self):
        # shuffle the deck
        # reset variables as needed
        pass

    def getCard(self):
        return self.topCardIndex

    def size(self):
        return 52

    def numCardsLeft(self):
        return 0

    def nextCard(self):
        self.topCardIndex -= 1
        return self.stackOfCards[self.topCardIndex]
```

Deck Test Code
```py
from card import *

deck = Deck()

for i in range(Deck.NUMCARDS):
    print(i, ":", deck.nextCard())
print()

```
Expected Results:
```
0 : (QUEEN of HEARTS)
1 : (JACK of HEARTS)
2 : (TEN of HEARTS)
3 : (NINE of HEARTS)
4 : (EIGHT of HEARTS)
5 : (SEVEN of HEARTS)
6 : (SIX of HEARTS)
7 : (FIVE of HEARTS)
8 : (FOUR of HEARTS)
9 : (THREE of HEARTS)
10 : (TWO of HEARTS)
11 : (ACE of HEARTS)
12 : (KING of SPADES)
13 : (QUEEN of SPADES)
14 : (JACK of SPADES)
15 : (TEN of SPADES)
16 : (NINE of SPADES)
17 : (EIGHT of SPADES)
18 : (SEVEN of SPADES)
19 : (SIX of SPADES)
20 : (FIVE of SPADES)
21 : (FOUR of SPADES)
22 : (THREE of SPADES)
23 : (TWO of SPADES)
24 : (ACE of SPADES)
25 : (KING of CLUBS)
26 : (QUEEN of CLUBS)
27 : (JACK of CLUBS)
28 : (TEN of CLUBS)
29 : (NINE of CLUBS)
30 : (EIGHT of CLUBS)
31 : (SEVEN of CLUBS)
32 : (SIX of CLUBS)
33 : (FIVE of CLUBS)
34 : (FOUR of CLUBS)
35 : (THREE of CLUBS)
36 : (TWO of CLUBS)
37 : (ACE of CLUBS)
38 : (KING of DIAMONDS)
39 : (QUEEN of DIAMONDS)
40 : (JACK of DIAMONDS)
41 : (TEN of DIAMONDS)
42 : (NINE of DIAMONDS)
43 : (EIGHT of DIAMONDS)
44 : (SEVEN of DIAMONDS)
45 : (SIX of DIAMONDS)
46 : (FIVE of DIAMONDS)
47 : (FOUR of DIAMONDS)
48 : (THREE of DIAMONDS)
49 : (TWO of DIAMONDS)
50 : (ACE of DIAMONDS)
51 : (KING of HEARTS)
```