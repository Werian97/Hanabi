from game_engine_modules.player import Player
from game_engine_modules.card import Card
from game_engine_modules.game import Game

from graphic_modules.graphic_settings import DEFAULT_FONT

from graphic_modules.geometry import Geometry
from graphic_modules.buttons import NameLabelButton

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

def update_trash_positions(game: Game, geometry: Geometry) -> None:
    horizontal_space = geometry.trash_box_size[0] - (geometry.trash_coos[0][0] - geometry.trash_box_coo[0]) - geometry.trash_card_size[0]
    for i in range(5):
        suit = game.trash[i]
        n = len(suit)
        if n > 0:
            horizontal_step = Vect(round(horizontal_space / n), 0)
            for j in range(n):
                card = suit[j]
                card.button.position = geometry.trash_coos[i] + j*horizontal_step

def update_namelabel_positions(game: Game, geometry: Geometry) -> None:
    for player in game.players:
        player.label_button.rect = pygame.Rect(geometry.name_label_coos[player.label_button.player_index], geometry.name_label_size)

def set_up_match(game: Game, geometry: Geometry) -> None:
    game.deal_cards()
    for i in range(len(game.players)):
        player = game.players[i]
        player.label_button = NameLabelButton(player.name, geometry, i)

def print_game(game: Game, geometry: Geometry) -> None:
    for i in range(len(game.players)):
        player = game.players[i]
        pygame.draw.rect(geometry.screen, "teal", player.label_button.rect)
        geometry.screen.blit(player.label_button.text, geometry.name_label_coos[player.label_button.player_index])


        if player.name != game.current.player.name:
            for card in player.hand:
                card.button.draw_card(geometry.screen)
    
    for i in range(5):
        card: Card = game.stacks[i]
        card.button.draw_card(geometry.screen)
    
    for i in range(5):
        for card in game.trash[i]:
            card.button.draw_card(geometry.screen)
    
    
    random_card = game.current.player.hand[0]
    geometry.screen.blit(random_card.button.back_image, geometry.deck_coo)
    remaining_cards = pygame.font.SysFont(name = DEFAULT_FONT, size = 55)
    geometry.screen.blit(remaining_cards.render(f"{len(game.deck)}", True, "black"), geometry.deck_coo)

    clues = pygame.font.SysFont(name = DEFAULT_FONT, size = 30)
    geometry.screen.blit(clues.render(f"Clue tokens: {game.clues}", True, "black"), geometry.meta_data_coo)
    
    for card in game.current.player.hand:
        card.button.draw_card(geometry.screen)