SUITS = ["red", "yellow", "green", "blue", "purple"]
RANKS = [1, 2, 3, 4, 5]

class Card():
    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit
    
    def get_rank(self):
        return self.rank
    
    def __str__(self):
        return f"({self.rank}, {self.suit})"
    
    def __repr__(self):
        return str(self)


ORDERED_DECK: list[Card] = []
for suit in SUITS:
    for rank in RANKS:
        ORDERED_DECK.append(Card(rank, suit))
        if rank != 5:
            ORDERED_DECK.append(Card(rank, suit))
            if rank == 1:
                ORDERED_DECK.append(Card(rank, suit))

PLAYERS = ["Alice", "Bob", "Cathy", "Donald", "Emanuele"]
INITIAL_CLUES = 8
MAX_CLUES = 8