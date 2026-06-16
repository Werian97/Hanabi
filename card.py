class Card():
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.positive_rank_clues: set[str] = set()
        self.negative_rank_clues: set[str] = set()
        self.positive_suit_clues: set[str] = set()
        self.negative_suit_clues: set[str] = set()
    
    def get_rank(self):
        return self.rank
    
    def __str__(self):
        return f"({self.rank}, {self.suit})"
   
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
         return self.rank == other.rank and self.suit == other.suit

def precedent(card: Card) -> Card:
        return Card(str(int(card.rank)-1), card.suit)