from game_engine_modules.game import Game
from game_engine_modules.card import Card
from game_engine_modules.player import Player

from game_engine_modules.deck import add_to_trash
from game_engine_modules.constants import SUITS

class Move():
    def execute(self, game: Game):
        pass #MUST OVERRIDE

    def __str__(self):
        pass #MUST OVERRIDE

class Play(Move):
    def __init__(self, slot: int):
        self.slot = slot
    
    def execute(self, game: Game) -> None:
        card_to_play: Card = game.current.player.hand.pop(self.slot-1)
        card_to_play.is_clued = False
        suit_index: int = SUITS.index(card_to_play.suit)
        if game.stacks[suit_index] == card_to_play.precedent():
            game.stacks[suit_index] = card_to_play
            if card_to_play.rank == "5":
                game.clues = min(8, game.clues + 1)
        else:
            add_to_trash(game.trash, card_to_play)
            game.strikes += 1
        if len(game.deck) > 0:
            game.current.player.draw_a_card(game.deck)
    
    def __str__(self):
        return f"plays slot {self.slot}"

class Clue(Move):
    def __init__(self, target_player: Player, rank_or_suit: str):
        self.target_player = target_player
        self.rank_or_suit = rank_or_suit

    def execute(self, game: Game):
        self.target_player.recieve_the_clue(self.rank_or_suit)
        game.clues -= 1
    
    def __str__(self):
        return f"clues {self.rank_or_suit} to {self.target_player.name}"


class Discard(Move):
    def __init__(self, slot: int):
        self.slot = slot

    def execute(self, game: Game):
        discarded_card = game.current.player.hand.pop(self.slot-1)
        discarded_card.is_clued = False
        add_to_trash(game.trash, discarded_card)
        game.clues += 1
        if len(game.deck) > 0:
            game.current.player.draw_a_card(game.deck)
    
    def __str__(self):
        return f"discards slot {self.slot}"