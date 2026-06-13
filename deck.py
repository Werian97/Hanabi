import random
from constants import ORDERED_DECK
from collections.abc import Callable

Deck = list[tuple[int, str]]

def get_new_deck() -> Deck:
    deck = ORDERED_DECK.copy()
    random.shuffle(deck)
    return deck

def get_hand_capacity(players_number: int) -> int:
    if players_number in [2, 3]:
        return 5
    elif players_number in [4, 5]:
        return 4
    raise Exception("Not valid input. You can choose between 2 and 5 players")