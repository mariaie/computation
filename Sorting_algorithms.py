from Classes.Hand import Hand


# Heap Sort
def heapify(hand, hand_size, i):
    """
        Rearranges the elements of the hand to maintain the heap property.

        Args:
            hand (Hand): The hand of cards to be sorted
            hand_size (int): The size of the hand
            i (int): The index of the current element being heapified

        Returns:
            None
    """
    largest = i  # Assume the largest is the root
    left = 2 * i + 1  # Index of the left child
    right = 2 * i + 2  # Index of the right child

    if left < hand_size and hand.get_card_value(left) > hand.get_card_value(largest):
        largest = left

    if right < hand_size and hand.get_card_value(right) > hand.get_card_value(largest):
        largest = right

    # If the right child is larger than the largest so far
    if largest != i:
        hand.switch_cards(i, largest)
        (hand, hand_size, largest)  # Recursively apply heapify


def heap_sort(hand):
    """
       Sorts the hand using the Heap Sort algorithm.

       Args:
           hand (Hand): The hand of cards to be sorted

       Returns:
           Hand: The sorted hand
    """
    hand_size = hand.get_quantity()

    # Build the max-heap
    for index in range(hand_size // 2 - 1, -1, -1):
        heapify(hand, hand_size, index)

    # Extract elements one by one
    for size in range(hand_size - 1, 0, -1):
        hand.switch_cards(0, size)
        heapify(hand, size, 0)  # Reorganize the heap with the remaining elements

    return hand


# Binary Insertion Sort
def binary_search(hand, val, start, end):
    """
        Performs a binary search to find the correct position for a value.

        Args:
            hand (Hand): The hand of cards
            val (int): The value to be inserted
            start (int): The starting index of the search range
            end (int): The ending index of the search range

        Returns:
            int: The index where the value should be inserted
    """
    while start < end:
        mid = (start + end) // 2
        if hand.get_card_value(mid) < val:
            start = mid + 1
        else:
            end = mid
    return start


def binary_insertion_sort(hand):
    """
        Sorts the hand using the Binary Insertion Sort algorithm.

        Args:
            hand (Hand): The hand of cards to be sorted

        Returns:
            Hand: The sorted hand
    """
    for index in range(1, hand.get_quantity()):
        val = hand.get_card_value(index)
        pos = binary_search(hand, val, 0, index)
        hand = Hand(
            hand.get_cards(0, pos) + [hand.get_card(index)] + hand.get_cards(pos, index) + hand.get_cards(index + 1,
                                                                                                          hand.get_quantity()))

    return hand


# Merge Sort
def merge(left_half, right_half):
    """
        Merges two sorted halves into a single sorted hand.

        Args:
            left_half (Hand): The left half of the hand
            right_half (Hand): The right half of the hand

        Returns:
            Hand: The merged and sorted hand
    """
    result = []
    i = j = 0

    # Merge in sorted order
    while i < left_half.get_quantity() and j < right_half.get_quantity():
        if left_half.get_card_value(i) <= right_half.get_card_value(j):
            result.append(left_half.get_card(i))
            i += 1
        else:
            result.append(right_half.get_card(j))
            j += 1

    # Add remaining elements
    result.extend(left_half.get_cards(i, left_half.get_quantity()))
    result.extend(right_half.get_cards(j, right_half.get_quantity()))

    return Hand(result)


def merge_sort(hand):
    """
        Sorts the hand using the Merge Sort algorithm.

        Args:
            hand (Hand): The hand of cards to be sorted

        Returns:
            Hand: The sorted hand
    """
    if hand.get_quantity() <= 1:
        return hand

    # Divide
    mid = hand.get_quantity() // 2
    left_half = merge_sort(Hand(hand.get_cards(0, mid)))
    right_half = merge_sort(Hand(hand.get_cards(mid, hand.get_quantity())))

    # Conquer (merge)
    return merge(left_half, right_half)


# Quick Sort
def quick_sort(hand, low, high):
    """
        Sorts the hand using the Quick Sort algorithm.

        Args:
            hand (Hand): The hand of cards to be sorted
            low (int): The starting index of the range to be sorted
            high (int): The ending index of the range to be sorted

        Returns:
            None
    """
    if low < high:
        pivot_index = partition(hand, low, high)
        quick_sort(hand, low, pivot_index - 1)
        quick_sort(hand, pivot_index + 1, high)


def partition(hand, low, high):
    """
        Partitions the hand around a pivot for Quick Sort.

        Args:
            hand (Hand): The hand of cards to be partitioned
            low (int): The starting index of the range
            high (int): The ending index of the range

        Returns:
            int: The index of the pivot after partitioning
        """
    pivot = hand.get_card_value(high)
    i = low - 1
    for j in range(low, high):
        if hand.get_card_value(j) <= pivot:
            i += 1
            hand.switch_cards(i, j)
    hand.switch_cards(i + 1, high)
    return i + 1
