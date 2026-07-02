from game_engine_modules.deck import Deck
from game_engine_modules.constants import RANKS

class Player():
    def __init__(self, name: str):
        self.hand: Deck = []
        self.name = name
        self.index: int
    
    def draw_a_card(self, deck: Deck) -> None:
        if deck == []:
            raise Exception("there are no cards in the deck")
        else:
            self.hand.insert(0, deck.pop(0))
    
    def get_hand_ranks(self) -> set[str]:
        ranks: set[str] = set()
        for card in self.hand:
            ranks.add(card.rank)
        return ranks

    def get_hand_suits(self) -> set[str]:
        suits: set[str] = set()
        for card in self.hand:
            suits.add(card.suit)
        return suits
    
    def recieve_the_clue(self, clue: str) -> None:
        for card in self.hand:
            if clue in RANKS:
                if card.rank == clue:
                    card.positive_rank_clues.add(clue)
                    card.is_clued = True
                else:
                    card.negative_rank_clues.add(clue)
            else:
                if card.suit == clue:
                    card.positive_suit_clues.add(clue)
                    card.is_clued = True
                else:
                    card.negative_suit_clues.add(clue)

    def get_possible_clues(self) ->dict[str, set[str]]:
        possible_clues: dict[str, set] = {
            "ranks": self.get_hand_ranks(),
            "suits": self.get_hand_suits()
        }
        return possible_clues