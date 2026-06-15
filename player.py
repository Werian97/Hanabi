from deck import Deck
from constants import RANKS

class Player():
    def __init__(self, name: str):
        self.hand: Deck = []
        self.name = name
    
    def draw_a_card(self, deck: Deck) -> None:
        if deck == []:
            raise Exception("there are no cards in the deck")
        else:
            self.hand.append(deck.pop(0))
    
    def get_hand_ranks(self) -> set[str]:
        ranks: set[str] = set()
        list(map(lambda x: ranks.add(x.rank), self.hand)) #just being fancy
        return ranks

    def get_hand_suits(self) -> set[str]:
        suits: set[str] = set()
        list(map(lambda x: suits.add(x.suit), self.hand)) #just being fancy
        return suits
    
    def recieve_the_clue(self, clue: str) -> None:
        for card in self.hand:
            if clue in RANKS:
                if card.rank == clue:
                    card.positive_rank_clues.add(clue)
                else:
                    card.negative_rank_clues.add(clue)
            else:
                if card.suit == clue:
                    card.positive_suit_clues.add(clue)
                else:
                    card.negative_suit_clues.add(clue)
            
def get_valid_slot(player: Player, move_type: str) -> int:
    valid_slot_input = False
    while not valid_slot_input:
        try:
            slot: int = int(input(f"What slot do you want to {move_type}? Insert a number between 1 and {len(player.hand)}: "))
            if slot < 1 or slot > len(player.hand):
                print(f"There is no slot {slot}")
                continue
            valid_slot_input = True
        except Exception:
            print("Not a valid input")
    return slot