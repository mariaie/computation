from Classes.hand import hand  

#heap sort
def heapify(hand, hand_size, i):
    largest = i  # Assume que o maior é a raiz
    left = 2 * i + 1  # Índice do filho à esquerda
    right = 2 * i + 2  # Índice do filho à direita

    # Se o filho da esquerda for maior que a raiz
    if left < hand_size and hand.get_card_value(left) > hand.get_card_value(largest):
        largest = left

    # Se o filho da direita for maior que o maior até agora
    if right < hand_size and hand.get_card_value(right) > hand.get_card_value(largest):
        largest = right

    # Se o maior não for a raiz
    if largest != i:
        hand.switch_cards(i, largest)
        heapify(hand, hand_size, largest)  # Aplica heapify recursivamente


def heap_sort(hand):
    hand_size = hand.get_quantity()

    # 1. Constrói o max-heap (reorganiza a lista)
    for index in range(hand_size // 2 - 1, -1, -1):
        heapify(hand, hand_size, index)

    # 2. Extrai elementos um a um
    for size in range(hand_size - 1, 0, -1):
        hand.switch_cards(0, size)
        heapify(hand, size, 0)  # Reorganiza o heap com os restantes

    return hand
  
#binary insertion sort
def binary_search(hand, val, start, end):
    while start < end:
        mid = (start + end) // 2
        if hand.get_card_value(mid) < val:
            start = mid + 1
        else:
            end = mid
    return start


def binary_insertion_sort(hand):
    for index in range(1, hand.get_quantity()):
        val = hand.get_card_value(index)
        pos = binary_search(hand, val, 0, index)
        hand = Hand(hand.get_cards(0, pos) + [hand.get_card(index)] + hand.get_cards(pos, index) + hand.get_cards(index+1, hand.get_quantity()))

    return hand

#merge sort

def merge(left_half, right_half):
    result = []
    i = j = 0

    # Junta de forma ordenada
    while i < left_half.get_quantity() and j < right_half.get_quantity():
        if left_half.get_card_value(i) <= right_half.get_card_value(j):
            result.append(left_half.get_card(i))
            i += 1
        else:
            result.append(right_half.get_card(j))
            j += 1

    # Adiciona os restantes elementos
    result.extend(left_half.get_cards(i, left_half.get_quantity()))
    result.extend(right_half.get_cards(j, right_half.get_quantity()))

    return Hand(result)


def merge_sort(hand):
    if hand.get_quantity() <= 1:
        return hand

    # Divide
    mid = hand.get_quantity() // 2
    left_half = merge_sort(Hand(hand.get_cards(0, mid)))
    right_half = merge_sort(Hand(hand.get_cards(mid, hand.get_quantity())))

    # Conquista (fusão)
    return merge(left_half, right_half)
#quick sort
def quick_sort(hand, low, high):
    if low < high:
        pivot_index = partition(hand, low, high)
        quick_sort(hand, low, pivot_index - 1)
        quick_sort(hand, pivot_index + 1, high)

def partition(hand, low, high):
    pivot = hand.get_card_value(high)
    i = low - 1
    for j in range(low, high):
        if hand.get_card_value(j) <= pivot:
            i += 1
            hand.switch_cards(i, j)
    hand.switch_cards(i + 1, high)
    return i + 1

