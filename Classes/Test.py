from Card_game import Card
from card_display import display_hand_ascii

# Cria algumas cartas de teste
hand = [
    Card(1, "spades"),     # A♠
    Card(12, "hearts"),    # Q♥
    Card(10, "diamonds"),  # 10♦
    Card(5, "clubs"),      # 5♣
    Card(13, "hearts")     # K♥
]

# Mostra as cartas em formato visual
display_hand_ascii(hand)
