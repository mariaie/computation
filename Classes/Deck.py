# A Deck must contain a full set of 52 unique cards, corresponding to every
#  combination of value and suit. To store a sequence of Card objects.
#  Must implement the necessary functionalities (or methods) for the deck, including:
#  • Shuffling — randomizing the order of the cards in the deck.
#  • Drawing — returning a specific number of cards.

import random
from Classes.Card_game import Card


class Deck:
    """
    A class to represent a deck of cards.

    Attributes:
        cards (list): A list of Card objects representing the deck.
    """

    def __init__(self):
        """
        Initialize a Deck object with 52 unique cards.
        """
        self.cards = []
        for suit in Card.suit_names:
            for value in range(1, 14):  # 1 to 13 inclusive
                self.cards.append(Card(value, suit))

    def __str__(self):
        """
        Return a string representation of the deck.

        Returns:
            str: A string representation of the deck, showing all cards.
        """
        return "\n".join(str(card) for card in self.cards)

    def __repr__(self):
        """
        Return a detailed string representation of the deck.

        Returns:
            str: A detailed string representation of the deck, showing all cards.
        """
        return f"Deck({self.cards})."

    def shuffle(self):
        """
        Shuffle the deck of cards.
        """
        random.shuffle(self.cards)

    def draw(self, num_cards=1):
        """
        Draw a specific number of cards from the deck.

        Args:
            num_cards (int): The number of cards to draw (default is 1).

        Returns:
            list: A list of Card objects drawn from the deck.

        Raises:
            ValueError: If the number of cards to draw exceeds the number of cards in the deck.
        """
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards in the deck to draw the requested number.")

        drawn_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return drawn_cards
