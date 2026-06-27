import pygame
import sys

from pygame import Surface
from graphic_modules.graphic_settings import FULL_SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH, DEFAULT_FONT
from graphic_modules.buttons import ClueButton, ClueRankButton, ClueSuitButton, NumPlayerButton, create_num_players_buttons, create_clue_buttons
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
    card_positions_updated: bool = False
    trying_to_give_clue: list = [False, -1]
    need_to_warn = False
    warning_message = pygame.font.SysFont(DEFAULT_FONT, 40)
    full_screen: bool = kwargs.get("full_screen", FULL_SCREEN)
    clock = pygame.time.Clock()
    answered = False
    move: Move
    while not answered:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(game.players_number):
                    if game.players[i].name != game.current.player.name:
                        if pygame.Rect(geometry.name_label_coos[i], geometry.name_label_size).collidepoint(pygame.mouse.get_pos()):
                            if game.clues > 0:
                                trying_to_give_clue = [True, i]
                            else:
                                need_to_warn = True
            elif event.type == pygame.MOUSEBUTTONUP:
                for i in range(len(game.current.player.hand)):
                    card = game.current.player.hand[i]
                    if pygame.Rect(geometry.stacks_box_coo, geometry.stacks_box_size).collidepoint(card.button.rect.center):
                        answered = True
                        move = Play(i + 1)
                    elif pygame.Rect(geometry.trash_box_coo, geometry.trash_box_size).collidepoint(card.button.rect.center):
                        if game.clues < 8:
                            answered = True
                            move = Discard(game.current.player.hand.index(card) +1)
                if trying_to_give_clue[0]:
                    i = trying_to_give_clue[1]
                    if pygame.Rect(geometry.name_label_coos[i], geometry.name_label_size).collidepoint(pygame.mouse.get_pos()):
                        answered, move = what_clue(geometry, game.players[i])
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
        if need_to_warn:
            geometry.screen.blit(warning_message.render("No clue token left", True, "black"), geometry.warning_message_coo)
        print_game(game, geometry)
        pygame.display.flip()

        clock.tick(60)
    history.add_move(move)
    return move











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
    remaining_cards = pygame.font.SysFont(name = DEFAULT_FONT, size = 55)
    geometry.screen.blit(remaining_cards.render(f"{len(game.deck)}", True, "black"), geometry.deck_coo)

    clues = pygame.font.SysFont(name = DEFAULT_FONT, size = 55)
    geometry.screen.blit(clues.render(f"{game.clues}", True, "black"), geometry.meta_data_coo)
    
    for card in game.current.player.hand:
        card.button.draw_card(geometry.screen)

def what_clue(geometry: Geometry, target_player: Player) -> tuple[bool, Move]:
    rank_or_suit: str
    possible_clues = target_player.get_possible_clues()
    pygame.draw.rect(geometry.screen, "gray", pygame.Rect(geometry.clue_window_coo, geometry.clue_window_size))
    clue_buttons: list[ClueButton] = create_clue_buttons(geometry.screen)

    x_on_exit_button = pygame.font.SysFont(DEFAULT_FONT, 40)
    geometry.screen.blit(x_on_exit_button.render("X", True, "black"), geometry.text_on_x_button_coo)
    exit_button = pygame.Rect(geometry.x_button_coo, geometry.x_button_size)

    text_on_giveclue_button = pygame.font.SysFont(DEFAULT_FONT, 30)
    geometry.screen.blit(text_on_giveclue_button.render("give clue", True, "black"), geometry.text_on_giveclue_button_coo)
    giveclue_button = pygame.Rect(geometry.giveclue_button_coo, geometry.giveclue_button_size)

    clue_given = False
    clock = pygame.time.Clock()
    while not clue_given:
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for button in clue_buttons:
                        if button.rect.collidepoint(mouse_pos):
                            for other in clue_buttons:
                                other.is_clicked = False
                                other.update_border_color()
                            button.is_clicked = True
                            button.update_border_color()
                    if exit_button.collidepoint(mouse_pos):
                        return False, Move()
                    if giveclue_button.collidepoint(mouse_pos):
                        for button in clue_buttons:
                            if button.is_clicked:
                                if isinstance(button, ClueRankButton):
                                    if button.rank in possible_clues["ranks"]:
                                        rank_or_suit = button.rank
                                        clue_given = True
                                    else:
                                        warning_message = pygame.font.SysFont(DEFAULT_FONT, 40)
                                        geometry.screen.blit(warning_message.render("No empty clue allowed", True, "black"), geometry.warning_message_coo)
                                elif isinstance(button, ClueSuitButton):
                                    if button.suit in possible_clues["suits"]:
                                        rank_or_suit = button.suit
                                        clue_given = True
                                    else:
                                        warning_message = pygame.font.SysFont(DEFAULT_FONT, 40)
                                        geometry.screen.blit(warning_message.render("No empty clue allowed", True, "black"), geometry.warning_message_coo)
        pygame.display.flip()
        clock.tick(60)
    return True, Clue(target_player, rank_or_suit)

