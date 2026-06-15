import random
from constants import ORDERED_DECK, SUITS
from collections.abc import Callable
from card import Card
from functools import reduce

Deck = list[Card]

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

def calculate_points(stacks: Deck) -> int:
    return reduce(lambda sum_so_far, card: sum_so_far + int(card.rank), stacks, 0)

def add_to_trash(trash: list[Deck], discarded_card: Card) -> None:
    suit_index: int = SUITS.index(discarded_card.suit)
    trash[suit_index].append(discarded_card)
    trash[suit_index].sort(key=Card.get_rank)