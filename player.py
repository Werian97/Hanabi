from deck import Deck

class Player():
    def __init__(self, name: str):
        self.hand: Deck = []
        self.name = name
    
    def draw_a_card(self, deck: Deck):
        if deck == []:
            raise Exception("there are no cards in the deck")
        else:
            self.hand.append(deck.pop(0))