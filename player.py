from deck import Deck, Card
from deck import get_color
from constants import SUITS

class Player():
    def __init__(self, name: str):
        self.hand: Deck = []
        self.name = name
    
    def draw_a_card(self, deck: Deck):
        if deck == []:
            raise Exception("there are no cards in the deck")
        else:
            self.hand.append(deck.pop(0))
    
    def play(self, stacks: Deck) ->bool:
        slot: int = get_valid_slot(self, "play")
        card_to_play: Card = self.hand.pop(slot-1)
        suit_index: int = SUITS.index(card_to_play[1])
        if stacks[suit_index] == (card_to_play[0]-1, card_to_play[1]):
            stacks[suit_index] = card_to_play
            return True
        else:
            return False
    
    def discard(self, trash: list[Deck]):
        slot: int = get_valid_slot(self, "discard")
        discarded_card = self.hand.pop(slot-1)
        suit_index: int = SUITS.index(discarded_card[1])
        trash[suit_index].append(discarded_card)
        trash[suit_index].sort(key=get_color)
            
def get_valid_slot(player: Player, move: str) -> int:
    valid_slot_input = False
    while valid_slot_input == False:
        try:
            slot: int = int(input(f"What slot do you want to {move}? Insert a number between 1 and {len(player.hand)} "))
            if slot < 1 or slot > len(player.hand):
                print(f"There is no slot {slot}")
                continue
            valid_slot_input = True
        except Exception:
            print("Not a valid input")
    return slot