import random
from game_engine_modules.constants import RANKS, SUITS, SEED_DICTIONARY, CLUE_ALIASES
from game_engine_modules.card import Card

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
    return "".join(
        SEED_DICTIONARY[card.short_str()]
        for card in deck
    )

def convert_seed_to_deck(seed: str) -> Deck:
    deck: Deck = []
    card_data: str = "prova"
    for char in seed:
        for key, value in SEED_DICTIONARY.items():
            if value == char:
                card_data = key
        deck.append(Card(card_data[1], CLUE_ALIASES.get(card_data[0], "ERROR")))
    return deck


ORDERED_DECK: list[Card] = []
for suit in SUITS:
    for rank in RANKS:
        ORDERED_DECK.append(Card(rank, suit))
        if int(rank) != 5:
            ORDERED_DECK.append(Card(rank, suit))
            if int(rank) == 1:
                ORDERED_DECK.append(Card(rank, suit))