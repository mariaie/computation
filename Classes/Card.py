# Card objects must store information regarding their value and their suit.
# You do not need to consider Jokers or any other type of cards.
# - Values: 1 (Ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen and King.
# - Suits: Spades, Clubs, Hearts and Diamonds
from colorama import init, Fore, Style
init(autoreset=True)
class Card:
    # dictionary with values
    value_names = {
        1: "Ace",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "Jack",
        12: "Queen",
        13: "King",
    }
    # dictionary with suits
    suit_names = {
        "spades" : "spades",
        "clubs" : "clubs",
        "diamonds" : "diamonds",
        "hearts" : "hearts",
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

        suit_lower = suit.lower()
        if suit_lower  not in self.suit_names:
            raise ValueError("The card suit is invalid:)")

        self.value = value
        self.suit = suit_lower

    def __str__(self):
        """Return a representation of the card(ex: 'Ace♠', '10♥')"""
        symbol = self.suit_symbols[self.suit]
        name = self.value_names[self.value]

        if self.suit in ["hearts", "diamonds"]:
            color = Fore.RED
        else:
            color = Fore.BLACK

        return f"{color}{name}{symbol}{Style.RESET_ALL}"

    def __repr__(self):
        """"Return a representation of the card"""
        return f"Card(value={self.value}, suit={self.suit})"

#um pequeno teste
if __name__ == "__main__":

    carta1 = Card(4, "hearts")
    print(carta1)

    carta2 = Card(12, "diamonds")
    print(carta2)

    carta3 = Card(1, "spades")
    print(carta3)

    carta4 = Card(10, "clubs")
    print(carta4)











