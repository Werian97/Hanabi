import pygame
import sys

from pygame import Surface
from graphic_modules.graphic_settings import FULL_SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH
from graphic_modules.buttons import NumPlayerButton, create_num_players_buttons
from graphic_modules.geometry import Geometry
from graphic_modules.updating_functions import drag_card, update_card_positions

from game_engine_modules.game import Game
from game_engine_modules.move import Move, Play, Discard, Clue
from game_engine_modules.player import Player
from game_engine_modules.card import Card

from memory_modules.history import History

def get_number_of_players(**kwargs) -> tuple[int, bool]:
    full_screen: bool = kwargs.get("full_screen", FULL_SCREEN)
    pygame.init()

    number_gotten = False
    exit_game = False
    players_number: int

    buttons = pygame.sprite.Group()
    NumPlayerButton.containers = (buttons,)

    if full_screen:
        sizes = pygame.display.get_desktop_sizes()
        size = sizes[0]
    else:
        size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    window_width, window_height = size
    create_num_players_buttons(window_width, window_height)
    screen: Surface = pygame.display.set_mode(size = (window_width, window_height))
    pygame.display.set_caption("Hanabi E.-Version")
    screen.fill("darkgreen")
    pygame.display.flip()

    clock = pygame.time.Clock()

    while not (number_gotten or exit_game):
        screen.fill("darkgreen")
        for event in pygame.event.get(): #if you remove this loop the window will freeze because the event qeue fills in and no one clear it
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 0, True  #exit the function. return False => in the main module the program exit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    return get_number_of_players(full_screen = not full_screen)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        players_number = button.function()
                        number_gotten = True
        
        for button in buttons:
            button.draw_button(screen)
        
        
        pygame.display.flip()
        clock.tick(60) #end of loop. restart

    pygame.display.quit()
    return players_number, exit_game

def start_window(players_number, game: Game, **kwargs) -> Geometry:
    pygame.init()
    full_screen = kwargs.get("full_screen", FULL_SCREEN)
    if full_screen:
        size = pygame.display.get_desktop_sizes()[0]
    else:
        size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    geometry = Geometry(players_number, screen)
    for card in game.all_cards:
        card.button.front_image = pygame.transform.scale(pygame.image.load(f'assets/cards/{card.suit}{card.rank}.png'), geometry.card_size)
        card.button.back_image = pygame.transform.scale(pygame.image.load(f'assets/cards/back.png'), geometry.card_size)
    for card in game.stacks:
        if card.rank == "0":
            card.button.front_image = pygame.transform.scale(pygame.image.load(f'assets/cards/{card.suit}{card.rank}.png'), geometry.card_size)
    pygame.display.set_caption("Hanabi E.-Version")
    return geometry

def ask_move(geometry: Geometry, game: Game, history: History, **kwargs) -> Move:
    card_positions_updated = False
    full_screen = kwargs.get("full_screen", FULL_SCREEN)
    clock = pygame.time.Clock()
    while game.running:
        for event in pygame.event.get(): #if you remove this loop the window will freeze because the event queue fills in and no one clear it
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit(1)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    full_screen = not full_screen
                    geometry = start_window(len(game.players), game, full_screen = full_screen)
                    card_positions_updated = False
            elif event.type == pygame.MOUSEBUTTONUP:
                for card in game.current.player.hand:
                    if pygame.Rect(geometry.stacks_box_coo, geometry.stacks_box_size).collidepoint(card.button.rect.center):
                        return Play(game.current.player.hand.index(card) +1)
                    elif pygame.Rect(geometry.trash_box_coo, geometry.trash_box_size).collidepoint(card.button.rect.center):
                        if game.clues < 8:
                            return Discard(game.current.player.hand.index(card) +1)
                card_positions_updated = False

        
        mouse_button_one = pygame.mouse.get_pressed(num_buttons=3)[0]
        if mouse_button_one:
            drag_card(game)
        else:
            for card in game.current.player.hand:
                card.button.is_pressed = False
        if not card_positions_updated:
            update_card_positions(game, geometry)
            card_positions_updated = True
        geometry.screen.fill("darkgreen")
        print_game(game, geometry)
        pygame.display.flip()

        clock.tick(60)
    return Move()








##########################  AUXILLARY FUNCTIONS  ###########################

def print_game(game: Game, geometry: Geometry) -> None:
    for player in game.current.others:#stampa le mani degli altri giocatori
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
    remaining_cards = pygame.font.SysFont(name = 'calibri', size = 55)
    geometry.screen.blit(remaining_cards.render(f"{len(game.deck)}", True, "black"), geometry.deck_coo)

    clues = pygame.font.SysFont(name = 'calibri', size = 55)
    geometry.screen.blit(clues.render(f"{game.clues}", True, "black"), geometry.meta_data_coo)
    
    for card in game.current.player.hand:
        card.button.draw_card(geometry.screen)