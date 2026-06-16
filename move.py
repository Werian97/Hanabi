from game import Game
from card import Card
from player import Player

from deck import add_to_trash
from card import precedent
from constants import SUITS

class Move():
    def __init__(self, target_player: Player, slot: int, rank_or_suit: str):
        self.target_player = target_player
        self.slot = slot
        self.rank_or_suit = rank_or_suit
    
    def execute(self, game: Game):
        pass #MUST OVERRIDE

class Play(Move):
    def __init__(self, target_player: Player, slot: int, rank_or_suit: str):
        super().__init__(target_player, slot, rank_or_suit)
    
    def execute(self, game: Game) -> None:
        card_to_play: Card = self.target_player.hand.pop(self.slot-1)
        suit_index: int = SUITS.index(card_to_play.suit)
        if game.stacks[suit_index] == precedent(card_to_play):
            game.stacks[suit_index] = card_to_play
            if card_to_play.rank == "5":
                game.clues = min(8, game.clues + 1)
        else:
            add_to_trash(game.trash, card_to_play)
            game.strikes += 1
        if len(game.deck) > 0:
            game.current.player.draw_a_card(game.deck)

class Clue(Move):
    def __init__(self, target_player: Player, slot: int, rank_or_suit: str):
        super().__init__(target_player, slot, rank_or_suit)

    def execute(self, game: Game):
        self.target_player.recieve_the_clue(self.rank_or_suit)
        game.clues -= 1


class Discard(Move):
    def __init__(self, target_player: Player, slot: int, rank_or_suit: str):
        super().__init__(target_player, slot, rank_or_suit)

    def execute(self, game: Game):
        discarded_card = self.target_player.hand.pop(self.slot-1)
        add_to_trash(game.trash, discarded_card)
        game.clues += 1
        if len(game.deck) > 0:
            game.current.player.draw_a_card(game.deck)