from game_engine_modules.player import Player
from game_engine_modules.card import Card
from game_engine_modules.deck import Deck
from game_engine_modules.game import Game

from graphic_modules.geometry import Geometry

import pygame

coordinate = tuple[int, int]

def print_game(game: Game, screen: pygame.Surface) -> None:
    for i in range(len(game.players)):#stampa le mani dei giocatori
        player: Player = game.players[i]
        for j in range(len(player.hand)):
            card: Card = player.hand[j]
            card.button.draw_card(screen)
    
    for i in range(5):
        card: Card = game.stacks[i]
        card.button.draw_card(screen)

def update_card_positions(game: Game, geometry: Geometry) -> None:
     for i in range(len(game.players)):
        player: Player = game.players[i]
        for j in range(len(player.hand)):
            card: Card = player.hand[j]
            card.button.position = (geometry.hands_coos[i][0] + j*(geometry.card_size[0]+geometry.card_spacing), geometry.hands_coos[i][1])

        for j in range(5):
            card: Card = game.stacks[j]
            card.button.position = (geometry.stacks_coo[0] + j*(geometry.card_size[0]+geometry.card_spacing), geometry.stacks_coo[1])