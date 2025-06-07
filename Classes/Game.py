
from computation.Classes.Card import Card, Deck
from Classes.Hand_Detection import detect_poker_hand
from Classes.sorting_algorithms import heap_sort, binary_insertion_sort, merge_sort, quick_sort
from Classes.Hand import Hand
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
    def draw_cards_from_deck(deck):
    while True:
            number_of_cards_to_be_drawn = int(input("How many cards would you like to draw? "))
            if 3 <= number_of_cards_to_be_drawn <= 15:
                return deck.draw(number_of_cards_to_be_drawn)
            else:
                print("Please choose a number between 3 and 15.")
        
def choose_sorting_algorithm(hand):
      """
        Prompt user to select a sorting algorithm for the drawn hand.
        Returns the selected algorithm as a function reference.
        """
    while True:
        number = int(input(
            "Choose the sorting algorithm:\n 1) Heap Sort;\n 2) Binary Insertion Sort;\n 3) Merge Sort;\n 4) Quick Sort;\n Choose one number: "))
        match number:
            case 1:
                hand = heap_sort(hand)
                break
            case 2:
                hand = binary_insertion_sort(hand)
                break
            case 3:
                hand = merge_sort(hand)
                break
            case 4:
                quick_sort(hand, 0, hand.get_quantity() - 1)
                break
            case _:
                print("Please type a number between 1 and 4.")

    return hand

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
