# Card objects must store information regarding their value and their suit.
# You do not need to consider Jokers or any other type of cards.
# - Values: 1 (Ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen and King.
# - Suits: Spades, Clubs, Hearts and Diamonds

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

