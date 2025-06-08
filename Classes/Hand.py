class Hand:
    """
    Represents a hand of cards in a card game.
    """
    def __init__(self, hand):
        """
        Initializes the Hand with a list of cards.

        Args:
            hand (list): List of card objects.
        """
        self.hand = hand
        self.quantity = len(hand)

    def get_quantity(self):
        """
        Returns the number of cards in the hand.

        Returns:
            int: Number of cards.
        """
        return self.quantity

    def get_hand(self):
        """
        Returns the list of cards in the hand.

        Returns:
            list: The cards in the hand.
        """
        return self.hand

    def get_card_value(self, card_index):
        """
        Returns the value of a card at a specific index.

        Args:
            card_index (int): The index of the card.

        Returns:
            int: The value of the card.
        """
        return self.get_card(card_index).get_value()

    def show_hand(self):
        """
        Displays all cards in the hand.
        """
        for card in self.hand:
            card.show_card()

    def switch_cards(self, index_card1, index_card2):
        """
        Switches the positions of two cards in the hand.

        Args:
            index_card1 (int): Index of the first card.
            index_card2 (int): Index of the second card.
        """
        self.hand[index_card1], self.hand[index_card2] = self.hand[index_card2], self.hand[index_card1]

    def get_cards(self, index_card1, index_card2):
        """
        Returns a list of cards between two indices.

        Args:
            index_card1 (int): Starting index.
            index_card2 (int): Ending index.

        Returns:
            list: The selected cards.
        """
        cards = []
        for i in range(index_card1, index_card2):
            cards.append(self.get_card(i))
        return cards

    def get_card(self, index):
        """
        Returns the card at the specified index.

        Args:
            index (int): The card index.

        Returns:
            object: The card object.
        """
        return self.get_hand()[index]

    def __len__(self):
        """
        Returns the number of cards in the hand.

        Returns:
            int: Number of cards.
        """
        return self.quantity

    def __iter__(self):
        """
        Returns an iterator over the cards in the hand.

        Returns:
            iterator: Iterator over the cards.
        """
        return iter(self.hand)


    def __getitem__(self, idx):
        """
        Enables indexing to get a card from the hand.

        Args:
            idx (int): Index of the card.

        Returns:
            object: The card object.
        """
        return self.hand[idx]

