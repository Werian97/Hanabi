import random
from game_engine.constants import ORDERED_DECK, SUITS
from game_engine.card import Card

from functools import reduce

Deck = list[Card]

def get_new_deck() -> Deck:
    deck = ORDERED_DECK.copy()
    random.shuffle(deck)
    return deck

def calculate_points(stacks: Deck) -> int:
    return reduce(lambda sum_so_far, card: sum_so_far + int(card.rank), stacks, 0)

def add_to_trash(trash: list[Deck], discarded_card: Card) -> None:
    suit_index: int = SUITS.index(discarded_card.suit)
    trash[suit_index].append(discarded_card)
    trash[suit_index].sort(key=Card.get_rank)

def get_deck_seed(deck: Deck) -> str:
    return "There's still work to do!"

def convert_seed_to_deck(seed: str) -> Deck:
    pass