from game_engine_modules.player import Player
from game_engine_modules.card import Card
from game_engine_modules.game import Game

from graphic_modules.graphic_settings import DEFAULT_FONT

from graphic_modules.geometry import Geometry
from graphic_modules.painter import Painter
from graphic_modules.watcher import Watcher

import pygame
from pygame.math import Vector2 as Vect

coordinate = tuple[int, int]

def update_card_positions(game: Game, geometry: Geometry) -> None:
    horizontal_spacing = Vect(geometry.card_size[0]+geometry.card_spacing, 0)
    for i in range(len(game.players)):
        player: Player = game.players[i]
        for j in range(len(player.hand)):
            card: Card = player.hand[j]
            card.button.position = geometry.hands_coos[i] + j* horizontal_spacing
            card.button.rect = pygame.Rect(card.button.position, geometry.card_size)

    for i in range(5):
        card = game.stacks[i]
        card.button.position = geometry.stacks_coo + i*horizontal_spacing
    
    horizontal_space = geometry.trash_box_size[0] - (geometry.trash_coos[0][0] - geometry.trash_box_coo[0]) - geometry.card_size[0]
    for i in range(5):
        suit = game.trash[i]
        n = len(suit)
        if n > 0:
            horizontal_step = Vect(round(horizontal_space / n), 0)
            for j in range(n):
                card = suit[j]
                card.button.position = geometry.trash_coos[i] + j*horizontal_step

def drag_card(game: Game, watcher: Watcher) -> None:
    if watcher.dragged_card_index != None:
        card = game.current.player.hand[watcher.dragged_card_index]
        movement = Vect(pygame.mouse.get_rel())
        card.button.update_position(movement)
        watcher.need_redraw = True

def set_up_match(game: Game, geometry: Geometry) -> None:
    game.deal_cards()
    for i in range(len(game.players)):
        player = game.players[i]
        player.index = i

