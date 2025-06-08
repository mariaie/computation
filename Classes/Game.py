from Classes import Deck, Hand
from Hand_Detection import detect_poker_hand
from Sorting_algorithms import heap_sort,binary_insertion_sort,merge_sort,quick_sort
from colorama import init

init(autoreset=True)


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
        self.combination_counts = {
            "High Card": 0,
            "One Pair": 0,
            "Two Pair": 0,
            "Three of a Kind": 0,
            "Straight": 0,
            "Flush": 0,
            "Full House": 0,
            "Four of a Kind": 0,
            "Straight Flush": 0,
            "Royal Flush": 0
        }
        self.playing = True

    def start(self):
        """
        Start the game loop:
        - Show welcome message
        - Ask to play
        - Manage replay logic
        """
        print("\n=== Welcome to the Poker Hand Detector! ===\n")
        print("You can draw between 3 and 15 cards")
        print("You can sort your hand using Heap Sort, Binary Insertion Sort, Merge Sort or Quick Sort.")

        first_round = True

        while self.playing:
            if first_round:
                play = input("\nDo you want to play a hand? (yes/no): ").lower()
                first_round = False
            else:
                play = input("\nWould you like to play another round or leave the game (play/exit)? ").lower()

            if play in ['y', 'yes', 'play']:
                self.play_round()
            elif play in ['n', 'no', 'exit']:
                self.playing = False
            else:
                print("Please provide a valid answer as shown in parentheses.")

        print("\nThank you for playing! See you next time.\n")

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
        print('Shuffling the deck...')
        deck = Deck()
        deck.shuffle()
        print(f"Deck after shuffling with {len(deck.cards)} cards available!")

        hand = self.draw_cards_from_deck(deck)
        sorted_hand = self.choose_sorting_algorithm(hand)

        self.display_hand(sorted_hand)

        combination = detect_poker_hand(sorted_hand)
        self.display_results(combination)

    def draw_cards_from_deck(self, deck):
        """
        Draw cards from the deck based on user input.
        Validates the number of cards (3-15).
        """
        while True:
            try:
                num_cards = int(input("\nHow many cards do you want to draw? (3 to 15): "))
                if 3 <= num_cards <= 15:
                    return Hand(deck.draw(num_cards))
                else:
                    print("Please choose a number between 3 and 15.")
            except ValueError:
                print("Please enter a valid number.")

    def choose_sorting_algorithm(self, hand):
        """
        Prompt user to select a sorting algorithm for the drawn hand.
        Returns the sorted hand.
        """
        print("\nYour current hand:", end=" ")
        for card in hand.get_hand():
            print(card, end=" ")
        print()

        print("\nChoose a sorting algorithm to sort your hand:")
        print("1 - Heap Sort")
        print("2 - Merge Sort")
        print("3 - Binary Insertion Sort")
        print("4 - Quick Sort")

        while True:
            try:
                choice = int(input("\nYour choice: "))
                if choice == 1:
                    return heap_sort(hand)
                elif choice == 2:
                    return merge_sort(hand)
                elif choice == 3:
                    return binary_insertion_sort(hand)
                elif choice == 4:
                    quick_sort(hand, 0, hand.get_quantity() - 1)
                    return hand
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

    def display_hand(self, hand):
        """
        Print the sorted hand to the console in a readable format.
        """
        print("\nYour sorted hand:", end=" ")
        for card in hand.get_hand():
            print(card, end=" ")
        print()

    def display_results(self, combination):
        """
        Show detected poker hand(s) and update tally.
        """
        if combination in self.combination_counts:
            self.combination_counts[combination] += 1

        print(f"\nDetected combination: {combination}!\n")

        print("Combinations found so far:")
        for combo, count in self.combination_counts.items():
            print(f"- {combo}: {count}")
