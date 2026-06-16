from card import Card

SUITS: list[str] = ["red", "yellow", "green", "blue", "purple"]
RANKS: list[str] = ["1", "2", "3", "4", "5"]
CLUE_ALIASES: dict[str, str] = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "r": "red",
    "red": "red",
    "y": "yellow",
    "yellow": "yellow",
    "g": "green",
    "green": "green",
    "b": "blue",
    "blue": "blue",
    "p": "purple",
    "purple": "purple",
}
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