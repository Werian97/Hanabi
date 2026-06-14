from deck import Deck
from constants import SUITS, RANKS
from card import Card
from card import precedent
from functools import reduce

class Player():
    def __init__(self, name: str):
        self.hand: Deck = []
        self.name = name
    
    def draw_a_card(self, deck: Deck) -> None:
        if deck == []:
            raise Exception("there are no cards in the deck")
        else:
            self.hand.append(deck.pop(0))
    
    def play(self, stacks: Deck) ->bool:
        slot: int = get_valid_slot(self, "play")
        card_to_play: Card = self.hand.pop(slot-1)
        suit_index: int = SUITS.index(card_to_play.suit)
        if stacks[suit_index] == precedent(card_to_play):
            stacks[suit_index] = card_to_play
            return True
        else:
            return False
    
    def discard(self, trash: list[Deck]) -> None:
        slot: int = get_valid_slot(self, "discard")
        discarded_card = self.hand.pop(slot-1)
        suit_index: int = SUITS.index(discarded_card.suit)
        trash[suit_index].append(discarded_card)
        trash[suit_index].sort(key=Card.get_rank)
    
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
            
def get_valid_slot(player: Player, move: str) -> int:
    valid_slot_input = False
    while valid_slot_input == False:
        try:
            slot: int = int(input(f"What slot do you want to {move}? Insert a number between 1 and {len(player.hand)}: "))
            if slot < 1 or slot > len(player.hand):
                print(f"There is no slot {slot}")
                continue
            valid_slot_input = True
        except Exception:
            print("Not a valid input")
    return slot