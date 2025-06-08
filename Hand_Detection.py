from collections import Counter


def is_one_pair(hand):
    """
    Returns True if hand contains exactly one pair.
    Assumes hand is a list of Card objects with a value attribute
    """
    # Extract just the card values from the hand
    value_counts = Counter(card.value for card in hand)
    # Finds pairs
    pairs = [value for value, count in value_counts.items() if count == 2]
    # Finds card values that appear 3 or more times, invalid
    three_or_more = [value for value, count in value_counts.items() if count > 2]
    # Return true if hand contains one pair
    return len(pairs) == 1 and len(three_or_more) == 0


def is_two_pair(hand):
    """
    Returns True if hand contains exactly two distinct pairs.
    Assumes hand is a list of Card objects with a value attribute
    """
    value_counts = Counter(card.value for card in hand)
    pairs = [v for v, count in value_counts.items() if count == 2]
    three_or_more = [v for v, count in value_counts.items() if count > 2]
    return len(pairs) == 2 and len(three_or_more) == 0


def is_three_of_a_kind(hand):
    """
    Returns True if hand contains exactly three cards of the same value,
    and no additional pair(i.e, not a full house)
    """
    value_counts = Counter(card.value for card in hand)
    has_three = any(count == 3 for count in value_counts.values())
    pairs_or_more = sum(1 for count in value_counts.values() if count >= 2)
    # Exactly on triplet, no pair
    return has_three and pairs_or_more == 1


def is_straight(hand):
    """
    Returns True if hand contains 5 consecutive card values.
    Assumes hand is a list of Card objects with a value attribute
    """
    if len(hand) < 5:
        return False
    # Remove Duplicates
    values = sorted(set(card.value for card in hand))

    # Check normal straights (Ace high)
    for i in range(len(values) - 4):
        if values[i + 4] - values[i] == 4 and len(set(values[i:i + 5])) == 5:
            return True
    # Special case: Ace Low Straight (A,2,3,4,5)
    # card.value is 0-12, so Ace=0, King=12
    if set([0, 1, 2, 3, 4]).issubset(values):
        return True

    return False


def is_flush(hand):
    """
    Returns True if hand contains 5 or more cards of the same suit
    """
    if len(hand) < 5:
        return False

    suit_counts = Counter(card.suit for card in hand)
    return any(count >= 5 for count in suit_counts.values())


def is_full_house(hand):
    """
    Returns True if hand contains 3 of a kind + a pair
    """
    value_counts = (Counter(card.value for card in hand))
    has_three = any(count == 3 for count in value_counts.values())
    has_pair = any(count == 2 for count in value_counts.values())
    return has_three and has_pair


def is_four_of_a_kind(hand):
    """
    Returns True if hand contains four cards of the same value.
    """
    value_counts = Counter(card.value for card in hand)
    return any(count == 4 for count in value_counts.values())


def is_straight_flush(hand):
    """
    Returns True if hand contains a straight flush.
    A straight of 5 cards all in the same suit.
    """
    if len(hand) < 5:
        return False
    # Group cards by suit
    suits = {}
    for card in hand:
        suits.setdefault(card.suit, []).append(card)
    # Check for straight in each suit group
    for same_suit_cards in suits.values():
        if len(same_suit_cards) >= 5:
            if is_straight(same_suit_cards):
                return True
    return False


def is_royal_flush(hand):
    """
    Returns True if hand contains a royal flush
    (10, J, Q, K, A in same suit)
    """
    # Values for 10 through Ace = [9, 10, 11, 12, 0]
    royal_values = {9, 10, 11, 12, 0}

    # Group by suit
    suits = {}
    for card in hand:
        suits.setdefault(card.suit, []).append(card)

    for suit_cards in suits.values():
        suit_values = set(card.value for card in suit_cards)
        if royal_values.issubset(suit_values):
            return True
    return False


def detect_poker_hand(hand):
    """
    Determines the best poker hand in the given hand.
    Returns the name of the hand
    Checks hands in order from strongest to weakest
    """
    if is_royal_flush(hand):
        return "Royal Flush"
    elif is_straight_flush(hand):
        return "Straight Flush"
    elif is_four_of_a_kind(hand):
        return "Four of a Kind"
    elif is_full_house(hand):
        return "Full House"
    elif is_flush(hand):
        return "Flush"
    elif is_straight(hand):
        return "Straight"
    elif is_three_of_a_kind(hand):
        return "Three of a kind"
    elif is_two_pair(hand):
        return "Two Pair"
    elif is_one_pair(hand):
        return "One Pair"
    else:
        return "No valid poker hand"
