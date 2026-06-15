from player import Player
from constants import RANKS

def get_valid_clue_target(names: list[str]) -> str:
    valid_target: bool = False
    while not valid_target:
        target = input(f"Choose between {names}: ")
        if target in names:
            valid_target = True
        else:
            print("Not a valid target. Remember that this game is case sensitive")
    return target

def get_possible_clues(player_target: Player) ->dict[str, set[str]]:
    possible_clues: dict[str, set] = {
        "ranks": player_target.get_hand_ranks(),
        "suits": player_target.get_hand_suits()
    }
    return possible_clues

def check_the_clue(clue: str, possible_clues: dict[str, set[str]]) -> str:
    clue = clue.strip()
    clue = clue.lower()
    if clue in RANKS:
        if clue in possible_clues["ranks"]:
            return clue    
    elif clue in ["red", "r"] and "red" in possible_clues["suits"]:
        if "red" in possible_clues["suits"]:
            return "red"
    elif clue in ["yellow", "y"] and "yellow" in possible_clues["suits"]:
        if "yellow" in possible_clues["suits"]:
            return "yellow"
    elif clue in ["green", "g"] and "green" in possible_clues["suits"]:
        if "green" in possible_clues["suits"]:
            return "green"
    elif clue in ["blue", "b"] and "blue" in possible_clues["suits"]:
        if "blue" in possible_clues["suits"]:
            return "blue"
    elif clue in ["purple", "p"] and "purple" in possible_clues["suits"]:
        if "purple" in possible_clues["suits"]:
            return "purple"
    else:
        raise Exception("Invalid input")
    raise Exception("Empty clues are not allowed")
