from game_engine.deck import Deck
from game_engine.move import Move

from game_engine.deck import get_deck_seed
from game_engine.constants import PLAYERS


class History():
    def __init__(self, players_number: int, deck: Deck):
        self.players_number = players_number
        self.deck = deck
        self.moves: list[Move] = []
    
    def add_move(self, move: Move) -> None:
        self.moves.append(move)
    
    def record_history(self) -> None:
        with open("Records", mode='a') as file:
            file.write(self.format_history())
    
    def format_history(self) -> str:
        deck_string = write_deck(self.deck)
        moves = write_moves(self.players_number, self.moves)
        strings: list[str] = []
        strings.append("\n-------------o==oo===========ooo===========oo==o-------------")
        strings.append(f"Number of players = {self.players_number}")
        strings.append("-------------------------------------------------------------")
        strings.append(f"Initial deck seed = {deck_string}")
        strings.append("-------------------------------------------------------------")
        strings.append(f"The moves where:\n{moves}")
        strings.append("-------------o==oo===========ooo===========oo==o-------------\n\n")
        return "\n".join(strings)
    
def write_deck(deck: Deck) -> str:
    return get_deck_seed(deck)

def write_moves(players_number: int, moves: list[Move]) -> str:
    move_strings = []
    names = PLAYERS[:players_number]
    for i in range(len(moves)):
        move_strings.append(f"{names[i % players_number]} {str(moves[i])}\n")
    return "\n".join(move_strings)