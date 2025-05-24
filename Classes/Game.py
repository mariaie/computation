
from computation.Classes.Card import Card, Deck
"""""""""""
=== Welcome to the Poker Hand Detector! ===

Do you want to play a hand? (yes/no): y

How many cards do you want to draw? (3 to 15): 5

Choose a sorting algorithm:
1 - Heap Sort
2 - Merge Sort
3 - Binary Insertion Sort
4 - Quick Sort

Your choice: 2

Your sorted hand: 3♦ 6♠ 6♣ 9♥ K♦

Detected combination: One Pair!

Combinations found so far:
- One Pair: 1
- Two Pair: 0
- Three of a Kind: 0
- Straight: 0
- Flush: 0
- Full House: 0
- Four of a Kind: 0
- Straight Flush: 0
- Royal Flush: 0

Do you want to play again? (y/n): n

Thank you for playing! See you next time.
"""""""""""

class Game:
    """
    Main class that controls the overall game flow.
    Handles user interaction, deck creation, hand drawing, sorting,
    poker hand detection, and replay logic.
    """

    def __init__(self):
        """
        Initialize game state, including deck, combination counter, and session status.
        """
        pass

    def start(self):
        """
        Start the game loop:
        - Show welcome message
        - Ask to play
        - Manage replay logic
        """
        pass

    def play_round(self):
        """
        Run one full round:
        - Ask number of cards
        - Shuffle and draw cards
        - Ask for sorting algorithm
        - Sort and show hand
        - Detect poker hand
        - Update and show combination stats
        """
        pass

    def choose_sorting_algorithm(self):
        """
        Prompt user to select a sorting algorithm for the drawn hand.
        Returns the selected algorithm as a function reference.
        """
        pass

    def display_hand(self, hand):
        """
        Print the sorted hand to the console in a readable format.
        """
        pass

    def display_results(self, combination):
        """
        Show detected poker hand(s) and update tally.
        """
        pass
