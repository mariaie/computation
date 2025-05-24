from Classes.Card_game import Card
from Classes.Deck import Deck

# testando as classes:
if __name__ == "__main__":
    # Criação de duas cartas
    carta1, carta2 = Card(3, "hearts"), Card(6, "spades")
    print(f"Creating cards: {carta1} and {carta2}")

    # Criação do baralho
    deck = Deck()
    print(f"Deck contains: {len(deck.cards)}")
    print(deck)  # Mostra o baralho completo

    # Embaralhar o baralho
    deck.shuffle()
    print("Shuffled deck:")
    print(deck)  # Mostra o baralho embaralhado

    # Retirar 5 cartas
    drawn_cards = deck.draw(5)
    print("Drawn cards:")
    for card in drawn_cards:
        print(card)  # Mostra as cartas retiradas com representações visuais

    print(f"Remaining cards in deck: {len(deck.cards)}")
