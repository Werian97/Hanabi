from graphic_modules.graphic_settings import CARD_WIDTH, CARD_HEIGHT, CARD_SPACING, NAME_LABEL_WIDTH, NAME_LABEL_HEIGHT
from graphic_modules.graphic_settings import TwoPlayers, ThreePlayers, FourPlayers, FivePlayers

import pygame
from pygame import Surface
from pygame.math import Vector2 as Vect

coordinate = Vect
taglia = Vect

class Geometry():
    def __init__(self, players_number: int, screen: Surface):
        self.screen: Surface = screen
        self.players_number: int = players_number
        self.window_size: coordinate = Vect(screen.get_size())
        match players_number:
            case 2:
                PlayersNumber = TwoPlayers
            case 3:
                PlayersNumber = ThreePlayers
            case 4:
                PlayersNumber = FourPlayers
            case 5:
                PlayersNumber = FivePlayers

        self.card_size: taglia = rescaled(PlayersNumber.CARD_SIZE.value, self.window_size)
        self.card_spacing, _ = rescaled(Vect(PlayersNumber.CARD_SPACING.value, 0), self.window_size)
        self.name_label_size: taglia = rescaled(PlayersNumber.NAME_LABEL_SIZE.value, self.window_size)
        self.hands_coos: list[coordinate] = list(map(lambda x: rescaled(x, self.window_size), PlayersNumber.HANDS_COOS.value))
        self.name_label_coos: list[coordinate] = list(map(lambda x: rescaled(x, self.window_size), PlayersNumber.NAME_LABEL_COOS.value))

        self.trash_card_size = rescaled(PlayersNumber.TRASH_CARD_SIZE.value, self.window_size)
        self.trash_coos: list[coordinate] = list(map(lambda x: rescaled(x, self.window_size), PlayersNumber.TRASH_COOS.value))
        self.trash_box_coo: coordinate = rescaled(PlayersNumber.TRASH_BOX_COO.value, self.window_size)
        self.trash_box_size: taglia = rescaled(PlayersNumber.TRASH_BOX_SIZE.value, self.window_size)

        self.deck_coo: coordinate = rescaled(PlayersNumber.DECK_COOS.value, self.window_size)

        self.stacks_coo: coordinate = rescaled(PlayersNumber.STACKS_COO.value, self.window_size)
        self.stacks_box_coo: coordinate = rescaled(PlayersNumber.STACKS_BOX_COO.value, self.window_size)
        self.stacks_box_size: taglia = rescaled(PlayersNumber.STACKS_BOX_SIZE.value, self.window_size)
        
        self.meta_data_size: taglia = rescaled(PlayersNumber.META_DATA_SIZE.value, self.window_size) #turn, efficiency, pace, clues
        self.meta_data_coo: coordinate = rescaled(PlayersNumber.META_DATA_COO.value, self.window_size)

        self.clue_window_coo = Vect(10,10)
        self.clue_window_size = Vect(300, 220)
        self.text_on_x_button_coo = Vect(260, 10)
        self.x_button_coo = Vect(250, 10)
        self.x_button_size = Vect(40, 40)
        self.text_on_giveclue_button_coo = Vect(110, 190)
        self.giveclue_button_coo = Vect(110, 190)
        self.giveclue_button_size = Vect(100, 40)
        self.warning_message_coo = Vect(10, 240)

def center_rectangles(size1: taglia, size2: taglia) -> coordinate:
    #Input: 2 pairs of rectangle coordinate
    #Output: How much you need to translate (x and y) the first rectangle to center it with respect to the second
    #Assuming they share the same top left corner
    return round_vect((size2 - size1)/2)

def rescaled(obj_size: taglia, window_size: taglia) -> taglia:
    window_size_copy = window_size.copy()
    obj_size_copy = obj_size.copy()
    full_screen_size: taglia = Vect(pygame.display.get_desktop_sizes()[0])
    obj_size_copy[0] = obj_size_copy[0]*(window_size_copy[0]/full_screen_size[0])
    obj_size_copy[1] = obj_size_copy[1]*(window_size_copy[1]/full_screen_size[1])
    return round_vect(obj_size_copy)

def round_vect(vect: Vect) -> Vect:
    vect[0] = round(vect[0])
    vect[1] = round(vect[1])
    return vect

