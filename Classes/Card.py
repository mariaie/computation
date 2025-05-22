# Card objects must store information regarding their value and their suit.
# You do not need to consider Jokers or any other type of cards.
# - Values: 1 (Ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen and King.
# - Suits: Spades, Clubs, Hearts and Diamonds

class Card:
    # dictionary with values
    value_names = {
        1: "Ace"
        2: "2"
        3: "3"
        4: "4"
        5: "5"
        6: "6"
        7: "7"
        8: "8"
        9: "9"
        10: "10"
        11: "Jack"
        12: "Queen"
        13: "King"
    }
    # dictionary with suits
    suit_names = {
        "spades" : "spades"
        "clubs" : "clubs"
        "diamonds" : "diamonds" 
        "hearts" : "hearts"
    }
    # dictionary with symbols
    suit_symbols = {
        "spades": " ♠",
        "clubs": " ♣",
        "hearts": " ♥",
        "diamonds": " ♦"

    }
    def __init__(self, value, suit):
        """"Initialize a card with a value between 1 and 13 and a suit"""
        if value not in self.value_names:
            raise ValueError("The card number needs to be between 1 and 13:)")
        if suit not in self.suit_names:
            raise ValueError("The card suit is invalid:)")

        self.value = value
        self.suit = suit

    def __str__(self):
        """Return a representation of the card(ex: 'Ace♠', '10♥')"""
        return f"{self.value_names[self.value]}{self.suit_symbols[self.suit]}"
    def __repr__(self):
        """"Return a representation of the card"""
        return f"Card(value={self.value}, suit={self.suit})"

carta1 = Card(1, "Hearts")
print(carta1)          # Saída: Ace♥
print(carta1.suit)     # Saída: Hearts (nome original, útil para comparações)

carta2 = Card(12, "Diamonds")
print(carta2)          # Saída: Queen♦
















