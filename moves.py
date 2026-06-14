from player import Player

def determine_move(line: str) ->str:
    line = line.strip()
    if len(line) != 1:
        raise Exception("Insert one letter")
    elif line == "P" or line == "p":
        return "play"
    elif line == "D" or line == "d":
        return "discard"
    elif line == "C" or line == "c":
        return "clue"
    else:
        raise Exception("Invalid input")