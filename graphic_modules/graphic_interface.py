import pygame

from pygame import Surface
from graphic_modules.graphic_settings import FULL_SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH
from graphic_modules.buttons import NumPlayerButton, create_num_players_buttons
from graphic_modules.geometry import Geometry
from graphic_modules.print_functions import print_game, update_card_positions

from game_engine_modules.game import Game
from game_engine_modules.move import Move

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
        card.button.image = pygame.transform.scale(pygame.image.load(f'assets/cards/{card.suit}{card.rank}.png'), geometry.card_size)
    for card in game.stacks:
        if card.rank == "0":
            card.button.image = pygame.transform.scale(pygame.image.load(f'assets/cards/{card.suit}{card.rank}.png'), geometry.card_size)
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    full_screen = not full_screen
                    geometry = start_window(len(game.players), game, full_screen = full_screen)
                    card_positions_updated = False
        if not card_positions_updated:
            update_card_positions(game, geometry)
        geometry.screen.fill("darkgreen")
        print_game(game, geometry.screen)
        pygame.display.flip()

        clock.tick(60)
    return Move()
