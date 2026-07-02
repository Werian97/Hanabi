from graphic_modules.buttons import CardButton

class Card():
    def __init__(self, rank: str, suit: str):
        self.rank: str = rank
        self.suit: str = suit
        self.is_clued: bool = False
        self.positive_rank_clues: set[str] = set()
        self.negative_rank_clues: set[str] = set()
        self.positive_suit_clues: set[str] = set()
        self.negative_suit_clues: set[str] = set()
        self.button: CardButton = CardButton()
    
    def get_rank(self): #QUESTA SERVE PER ORDINARE IL TRASH
        return self.rank
    
    def __str__(self):
        return f"({self.rank}, {self.suit})"
   
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
         return self.rank == other.rank and self.suit == other.suit

    def precedent(self) -> "Card":
        return Card(str(int(self.rank)-1), self.suit)
    
    def short_str(self) -> str:
        return f"{self.suit[0]}{self.rank}"