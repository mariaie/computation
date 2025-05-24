# Card objects must store information regarding their value and their suit.
# You do not need to consider Jokers or any other type of cards.
# - Values: 1 (Ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen and King.
# - Suits: Spades, Clubs, Hearts and Diamonds

from colorama import init, Fore, Style

init(autoreset=True)


class Card:
    """
    A class to represent a playing card.

    Attributes:
        value_names (dict): A dictionary mapping card values (1-13) to their names.
        suit_names (dict): A dictionary mapping suit names to their string representations.
        suit_symbols (dict): A dictionary mapping suit names to their symbols.
    """

    value_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suit_names = ["spades","clubs","diamonds","hearts"]

    # dictionary with symbols
    suit_symbols = {
        "spades": " ♠",
        "clubs": " ♣",
        "hearts": " ♥",
        "diamonds": " ♦"
    }

    def __init__(self, value, suit):
        """
        Initialize a Card object.

        Args:
            value (int): The card's value from 1 to 13 (1 = Ace, 13 = King).
            suit (str): The suit of the card ('spades', 'clubs', 'hearts', 'diamonds').

        Raises:
            ValueError: If value is not between 1 and 13.
            ValueError: If suit is not valid.
        """
        if not isinstance(value, int) or not (1 <= value <= 13):
            raise ValueError("The card value must be between 1 and 13.")

        suit_lower = suit.lower()
        if suit_lower not in self.suit_names:
            raise ValueError("The card suit is invalid.")

        self.value = value - 1  # Internally store as index (0–12)
        self.suit = suit_lower

    def __str__(self):
        """
        Return a string representation of the card.

        Returns:
            str: A string representation of the card (e.g., 'Ace♠', '10♥').
        """

        symbol = self.suit_symbols[self.suit]
        name = self.value_names[self.value]

        if self.suit in ["hearts", "diamonds"]:
            color = Fore.RED
        else:
            color = Fore.BLACK

        return f"{color}{name}{symbol}{Style.RESET_ALL}"

    def __repr__(self):
        """
        Return a technical string representation of the card.

        Returns:
            str: A string representation for debugging (e.g., 'Card(value=1, suit='spades')').
        """
        return f"Card(value={self.value}, suit={self.suit})"

