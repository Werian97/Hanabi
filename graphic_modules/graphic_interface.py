import pygame
import sys

from pygame import Surface
from pygame.math import Vector2 as Vect

from graphic_modules.graphic_settings import FULL_SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH

from graphic_modules.buttons import NumPlayerButton
from graphic_modules.geometry import Geometry
from graphic_modules.archive import Archive
from graphic_modules.painter import Painter

from graphic_modules.buttons import create_num_players_buttons
from graphic_modules.updating_functions import drag_card, update_card_positions

from game_engine_modules.game import Game
from game_engine_modules.move import Move

from graphic_modules.watcher import Watcher
from memory_modules.history import History

Geometries = tuple[Geometry, Geometry]
Archives = tuple[Archive, Archive]
taglia = Vect
coordinate = Vect

def get_number_of_players(**kwargs) -> int | None:
    full_screen: bool = kwargs.get("full_screen", FULL_SCREEN)
    pygame.init()

    players_number: int | None = None

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

    while players_number == None:
        screen.fill("darkgreen")
        for event in pygame.event.get(): #if you remove this loop the window will freeze because the event qeue fills in and no one clear it
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    return get_number_of_players(full_screen = not full_screen)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        players_number = button.function()
        
        for button in buttons:
            button.draw_button(screen)
        
        
        pygame.display.flip()
        clock.tick(60) #end of loop. restart

    pygame.display.quit()
    return players_number

def start_window(**kwargs) -> Painter:
    pygame.init()
    players_number: int = kwargs.get("players_number") # type: ignore
    
    full_screen_size: taglia = Vect(pygame.display.get_desktop_sizes()[0])
    window_size: taglia = Vect(WINDOW_WIDTH, WINDOW_HEIGHT)

    FS_geometry: Geometry = Geometry(players_number, full_screen_size)
    FS_archive: Archive = Archive(FS_geometry)

    WND_geometry: Geometry = Geometry(players_number, Vect(WINDOW_WIDTH, WINDOW_HEIGHT))
    WND_archive: Archive = Archive(WND_geometry)

    geometries = (WND_geometry, FS_geometry)
    archives = (WND_archive, FS_archive)

    full_screen: bool = FULL_SCREEN
    if full_screen:
        screen: Surface = pygame.display.set_mode(full_screen_size)
        painter = Painter(screen, geometries, archives)
    else:
        screen: Surface = pygame.display.set_mode(window_size)
        painter = Painter(screen, geometries, archives)
    pygame.display.set_caption("Hanabi E.-Version")
    return painter

def ask_move(painter: Painter, game: Game, history: History) -> Move:
    watcher = Watcher()
    clock = pygame.time.Clock()
    move: Move | None = None
    while move == None:
        for event in pygame.event.get(): #if you remove this loop the window will freeze because the event queue fills in and no one clear it
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit(1)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    painter.switch_FS_WND()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                watcher.check_name_labels(game, painter.current_geometry)
                watcher.check_cards_to_drag(game)
            elif event.type == pygame.MOUSEBUTTONUP:
                move: Move | None = watcher.check_move_inputs(game, painter)
                painter.card_positions_updated = False
                if move != None:
                    return move

        mouse_button_one: bool = pygame.mouse.get_pressed(num_buttons=3)[0]
        if mouse_button_one:
            drag_card(game, watcher)
        
        if not painter.card_positions_updated:
            update_card_positions(game, painter.current_geometry)
            painter.card_positions_updated = True
            watcher.need_redraw = True
        if watcher.clue_token_need_warn:
            painter.display_warning_message(painter.clue_token_warning_message)
        if watcher.need_redraw:
            painter.draw_game(game)
            watcher.need_redraw = False

        clock.tick(60)
    history.add_move(move)