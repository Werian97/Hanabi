from game_engine_modules.player import Player
from game_engine_modules.card import Card
from game_engine_modules.deck import Deck
from game_engine_modules.game import Game

from graphic_modules.geometry import Geometry

import pygame

coordinate = tuple[int, int]

def update_card_positions(game: Game, geometry: Geometry) -> None:
     for i in range(len(game.players)):
        player: Player = game.players[i]
        for j in range(len(player.hand)):
            card: Card = player.hand[j]
            card.button.position = (geometry.hands_coos[i][0] + j*(geometry.card_size[0]+geometry.card_spacing), geometry.hands_coos[i][1])
            card.button.rect = pygame.Rect(card.button.position, geometry.card_size)

        for j in range(5):
            card: Card = game.stacks[j]
            card.button.position = (geometry.stacks_coo[0] + j*(geometry.card_size[0]+geometry.card_spacing), geometry.stacks_coo[1])

def drag_card(game: Game) -> None:
    mouse_is_busy = False
    for card in game.current.player.hand:
        if card.button.is_pressed:
            mouse_is_busy = True
            movement = pygame.mouse.get_rel()
            card.button.update_position(movement)
            card.button.rect.move_ip(movement)
    if not mouse_is_busy:
        for card in game.current.player.hand:
            if card.button.rect.collidepoint(pygame.mouse.get_pos()):
                card.button.is_pressed = True
                pygame.mouse.get_rel()