from game import Game
from card import Card

from player import get_valid_slot
from deck import add_to_trash
from card import precedent
from clues import get_valid_clue_target, get_possible_clues, check_the_clue
from constants import MAX_CLUES, SUITS

class Move():
    def __init__(self, game: Game):
            self.game = game
    
    def execute(self):
        pass #MUST OVERRIDE

class Play(Move):
    def __init__(self, game: Game):
        super().__init__(game)
    
    def execute(self) -> None:
        slot: int = get_valid_slot(self.game.current.player, "play")
        card_to_play: Card = self.game.current.player.hand.pop(slot-1)
        suit_index: int = SUITS.index(card_to_play.suit)
        if self.game.stacks[suit_index] == precedent(card_to_play):
            self.game.stacks[suit_index] = card_to_play
            if card_to_play.rank == "5":
                self.game.clues = min(8, self.game.clues + 1)
        else:
            add_to_trash(self.game.trash, card_to_play)
            self.game.strikes += 1
        if len(self.game.deck) > 0:
            self.game.current.player.draw_a_card(self.game.deck)

class Clue(Move):
    def __init__(self, game: Game):
        super().__init__(game)

    def execute(self):
        names: list[str] = []
        for player in self.game.current.others:
            names.append(player.name)
        print("Type in who do you want to clue.")
        target: str = get_valid_clue_target(names)
        target_player = list(filter(lambda player: player.name == target, self.game.current.others))[0]
        possible_clues: dict[str, set] = get_possible_clues(target_player)
        valid_clue = False
        while not valid_clue:
            try:
                print(f"Those are the clues you can give to {target_player.name}: {possible_clues["ranks"]},{possible_clues["suits"]}")
                print("What clue do you want to give? " \
                "(Type numbers with their digit. " \
                "'Red', 'red', 'R', 'r' are all accepted. ")
                clue = check_the_clue(input("Type in your clue: "), possible_clues)                    
                valid_clue = True
            except Exception as e:
                print(e)
        target_player.recieve_the_clue(clue)
        self.game.clues -= 1


class Discard(Move):
    def __init__(self, game: Game):
        super().__init__(game)

    def execute(self):
        slot: int = get_valid_slot(self.game.current.player, "discard")
        discarded_card = self.game.current.player.hand.pop(slot-1)
        add_to_trash(self.game.trash, discarded_card)
        self.game.clues += 1
        if len(self.game.deck) > 0:
            self.game.current.player.draw_a_card(self.game.deck)

def determine_move(game: Game) ->Move:
    move_type = input("What do you want to do? (Play: P, Clue: C, Discard: D): ")
    move_type = move_type.strip().lower()
    if len(move_type) != 1:
        raise Exception("Insert one letter")
    elif move_type == "p":
        return Play(game)
    elif move_type == "d":
        if game.clues < MAX_CLUES:
            return Discard(game)
        else:
            raise Exception("You cannot discard: you have too many clues")
    elif move_type == "c":
        if game.clues > 0:
            return Clue(game)
        else:
            raise Exception("You cannot clue: you have no clue token left")
    else:
        raise Exception("Invalid input")

def get_the_move(game):
    while True:
        try:
            return determine_move(game)
        except Exception as e:
            print(e)