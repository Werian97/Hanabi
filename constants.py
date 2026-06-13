SUITS = ["red", "yellow", "green", "blue", "purple"]
RANKS = [1, 2, 3, 4, 5]
ORDERED_DECK: list[tuple[int, str]] = []
for suit in SUITS:
    for rank in RANKS:
        ORDERED_DECK.append((rank, suit))
        if rank != 5:
            ORDERED_DECK.append((rank, suit))
            if rank == 1:
                ORDERED_DECK.append((rank, suit))

PLAYERS = ["Alice", "Bob", "Cathy", "Donald", "Emanuele"]
INITIAL_CLUES = 8