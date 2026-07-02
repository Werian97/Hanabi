import pygame

from game_engine_modules.game import Game
from game_engine_modules.move import Move, Play, Clue, Discard
from game_engine_modules.player import Player

from graphic_modules.buttons import ClueButton, ClueRankButton, ClueSuitButton
from graphic_modules.geometry import Geometry
from graphic_modules.painter import Painter

from graphic_modules.buttons import create_clue_buttons


class Watcher():
    def __init__(self):
        self.trying_to_give_clue: bool = False
        self.target_player_for_clue: int
        self.clue_token_need_warn: bool = False
        self.dragged_card_index: int | None = None
        self.valid_clue_given: bool = False
        self.need_redraw: bool = True
    
    def check_name_labels(self, game: Game, geometry: Geometry) -> None:
        for player in game.current.others:
            if geometry.name_label_rects[player.index].collidepoint(pygame.mouse.get_pos()):
                if game.clues > 0:
                    self.trying_to_give_clue = True
                    self.target_player_for_clue = player.index
                else:
                    self.clue_token_need_warn = True
    
    def check_cards_to_drag(self, game: Game):
        for i in range(len(game.current.player.hand)):
            card = game.current.player.hand[i]
            if card.button.rect.collidepoint(pygame.mouse.get_pos()):
                card.button.is_pressed = True
                self.dragged_card_index = i
                pygame.mouse.get_rel()

    def check_move_inputs(self, game: Game, painter: Painter) -> Move | None:
        geometry = painter.current_geometry
        move: Move | None = None
        if isinstance(self.dragged_card_index, int):
            card = game.current.player.hand[self.dragged_card_index]
            if geometry.stacks_box_rect.collidepoint(card.button.rect.center):
                move = Play(self.dragged_card_index + 1)
            elif geometry.trash_box_rect.collidepoint(card.button.rect.center):
                if game.clues < 8:
                    move = Discard(self.dragged_card_index +1)
            card.button.is_pressed = False
        if self.trying_to_give_clue:
            player: Player = game.players[self.target_player_for_clue]
            if geometry.name_label_rects[player.index].collidepoint(pygame.mouse.get_pos()):
                move = self.what_clue(painter, player)

        self.dragged_card_index = None
        return move


    def what_clue(self, painter: Painter, target_player: Player) -> Move | None:
        geometry = painter.current_geometry
        archive = painter.current_archive
        rank_or_suit: str | None = None
        possible_clues = target_player.get_possible_clues()
        painter.screen.blit(archive.clue_window, geometry.clue_window_coo)
        clue_buttons: list[ClueButton] = create_clue_buttons(painter.screen)

        exit_button = pygame.Rect(geometry.x_button_coo, geometry.x_button_size)
        giveclue_button = pygame.Rect(geometry.giveclue_button_coo, geometry.giveclue_button_size)

        clock = pygame.time.Clock()
        while not isinstance(rank_or_suit, str):
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        update_button_states(clue_buttons, mouse_pos)
                        if exit_button.collidepoint(mouse_pos):
                            self.trying_to_give_clue = False
                            return
                        if giveclue_button.collidepoint(mouse_pos):
                            rank_or_suit = self.try_to_give_clue(clue_buttons, possible_clues, painter)
            
            pygame.display.flip()
            clock.tick(60)
        return Clue(target_player, rank_or_suit)

    def try_to_give_clue(self, clue_buttons: list[ClueButton], possible_clues: dict[str, set[str]], painter: Painter) -> str | None:
        for button in clue_buttons:
            if button.is_clicked:
                if isinstance(button, ClueRankButton):
                    if button.rank in possible_clues["ranks"]:
                        self.trying_to_give_clue = False
                        return button.rank
                    else:
                        painter.display_warning_message(painter.empty_clue_warning_message)
                        return
                elif isinstance(button, ClueSuitButton):
                    if button.suit in possible_clues["suits"]:
                        self.trying_to_give_clue = False
                        return button.suit
                    else:
                        painter.display_warning_message(painter.empty_clue_warning_message)
                        return

def update_button_states(clue_buttons: list[ClueButton], mouse_pos: tuple[int, int]) -> None:
    for button in clue_buttons:
        if button.rect.collidepoint(mouse_pos):
            for other in clue_buttons:
                other.is_clicked = False
                other.update_border_color()
            button.is_clicked = True
            button.update_border_color()

