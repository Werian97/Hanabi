from player import Player
from constants import MAX_CLUES

def determine_move(clues: int, line: str) ->str:
    line = line.strip()
    if len(line) != 1:
        raise Exception("Insert one letter")
    elif line == "P" or line == "p":
        return "play"
    elif line == "D" or line == "d":
        if clues < MAX_CLUES:
            return "discard"
        else:
            raise Exception("You cannot discard: you have too many clues")
    elif line == "C" or line == "c":
        if clues > 0:
            return "clue"
        else:
            raise Exception("You cannot clue: you have no clue token left")
    else:
        raise Exception("Invalid input")