from player import Player
from game import Game
from move import Move, Clue, Play, Discard
from card import Card

from game import calculate_points, get_hand_capacity
from constants import MAX_CLUES, RANKS

def get_number_of_players() -> int:
    valid_player_count = False #exit condition for the how-many-players-while
    while not valid_player_count:
        try:
            players_number: int = int(input("How many players?: ")) #number of players
            if players_number not in [2, 3, 4, 5]:
                raise Exception("Not valid input. You can choose between 2 and 5 players")
            valid_player_count = True
        except ValueError:
            print("Only digits allowed")
        except Exception as e:
            print(e)
    return players_number


def print_player_hand(player: Player, others: list[Player]) -> None:
    print("\n\n")
    print(f"{player.name} it's your turn. This is your hand:")
    print(", ".join(string_on_terminal(card, False) for card in player.hand))
    print("\n\n")
    print("These are other players' hands:")
    for npc in others:
        npc_hand = ", ".join(string_on_terminal(card, True) for card in npc.hand)
        print(f"{npc.name}'s hand is \n{npc_hand}\n")

def print_end_message(game: Game) -> None:
        if game.exit_conditions.win or game.exit_conditions.end:
            points = calculate_points(game.stacks)
            print(f"CONGRATULATIONS! You totalized {points} points")
        else:
            print("Oh no! That was strike 3. The game is over. You totalized 0 points")

def print_game_state(game: Game) -> None:
    print(f"These are the stacks:\n{game.stacks}")
    print("\n")
    print(f"You have {game.clues} clues")
    print("\n")
    print(f"And this is the trash:\n{game.trash}")
    input("Press enter to continue...")

def get_valid_clue_target(game: Game) -> Player:
    names: list[str] = get_name_list(game.current.others)
    print("Type in who do you want to clue.")
    valid_target: bool = False
    while not valid_target:
        target_name = input(f"Choose between {names}: ").lower().capitalize()
        for npc in game.current.others:
            if target_name == npc.name:
                valid_target = True
                target = npc
        if not valid_target:
            print("Not a valid target")
    return target

def get_a_clue(target_player: Player, possible_clues: dict[str, set[str]]) -> str:
    print(f"Those are the clues you can give to {target_player.name}: {possible_clues["ranks"]},{possible_clues["suits"]}")
    print("What clue do you want to give? " \
    "(Type numbers with their digit. " \
    "'Red', 'red', 'R', 'r' are all accepted. ")
    clue = input("Type in your clue: ")
    clue = clue.strip().lower()
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

def ask_move(game: Game) -> Move:
    while True:
        try:
            return determine_move(game)
        except Exception as e:
            print(e)

def determine_move(game: Game) ->Move:
    move_type = input("What do you want to do? (Play: P, Clue: C, Discard: D): ")
    move_type = move_type.strip().lower()
    if len(move_type) != 1:
        raise Exception("Insert one letter")
    elif move_type == "p":
        slot: int = get_valid_slot(game.current.player, "play")
        return Play(game.current.player, slot, "") #"" is deafault
    elif move_type == "d":
        if game.clues < MAX_CLUES:
            slot: int = get_valid_slot(game.current.player, "discard")
            return Discard(game.current.player, slot, "")
        else:
            raise Exception("You cannot discard: you have too many clues")
    elif move_type == "c":
        if game.clues > 0:
            target_player: Player = get_valid_clue_target(game)
            possible_clues: dict[str, set[str]] = target_player.get_possible_clues()
            valid_clue = False
            while not valid_clue:
                try:
                    rank_or_suit = get_a_clue(target_player, possible_clues)
                    valid_clue = True
                except Exception as e:
                    print(e)
            return Clue(target_player, -1, rank_or_suit)
        else:
            raise Exception("You cannot clue: you have no clue token left")
    else:
        raise Exception("Invalid input")

def get_valid_slot(player: Player, move_type: str) -> int:
    valid_slot_input = False
    while not valid_slot_input:
        try:
            slot: int = int(input(f"What slot do you want to {move_type}? Insert a number between 1 and {len(player.hand)}: "))
            if slot < 1 or slot > len(player.hand):
                print(f"There is no slot {slot}")
                continue
            valid_slot_input = True
        except Exception:
            print("Not a valid input")
    return slot

def string_on_terminal(card: Card, show: bool) -> str:
    if show:
        return prepare_to_show(card)
    else:
        return prepare_to_hide(card)

def prepare_to_show(card: Card) -> str:
    return f"({card.suit} {card.rank})"

def prepare_to_hide(card: Card) -> str:
    positive, negative = get_info(card)
    return f"(pos: {positive} | neg: {negative})"

def get_info(card: Card) -> tuple[str, str]:
    positive = ""
    for item in card.positive_rank_clues:
        positive += f"{item}, "
    for item in card.positive_suit_clues:
        positive += f"{item}, "
    positive = positive.rstrip(", ")

    negative = ""
    for item in card.negative_rank_clues:
        negative += f"{item}, "
    for item in card.negative_suit_clues:
        negative += f"{item}, "
    negative = negative.rstrip(", ")
    return positive, negative

def get_name_list(others: list[Player]) -> list[str]:
    names: list[str] = []
    for npc in others:
        names.append(npc.name)
    return names