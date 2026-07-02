from graphic_modules.graphic_settings import TwoPlayers, ThreePlayers, FourPlayers, FivePlayers, CommonSettings

from graphic_modules.graphic_settings import WINDOW_WIDTH, WINDOW_HEIGHT

import pygame
from pygame import Surface, Rect
from pygame.math import Vector2 as Vect

coordinate = Vect
taglia = Vect

class Geometry():
    def __init__(self, players_number: int, screen_size: taglia):
        self.players_number: int = players_number
        self.screen_size: taglia = screen_size
        match players_number:
            case 2:
                PlayersNumber = TwoPlayers
            case 3:
                PlayersNumber = ThreePlayers
            case 4:
                PlayersNumber = FourPlayers
            case 5:
                PlayersNumber = FivePlayers

        self.card_size: taglia = rescaled(CommonSettings.CARD_SIZE.value, screen_size)
        self.card_spacing: int = round(CommonSettings.CARD_SPACING.value *(WINDOW_WIDTH/1920))

        self.name_label_size: taglia = rescaled(CommonSettings.NAME_LABEL_SIZE.value, screen_size)
        self.hands_coos: list[coordinate] =  list(map(lambda x: rescaled(x, screen_size), PlayersNumber.HANDS_COOS.value))
        self.name_label_coos: list[coordinate] = list(map(lambda x: rescaled(x, screen_size), PlayersNumber.NAME_LABEL_COOS.value))
        self.name_label_rects: list[Rect] = []
        for coo in self.name_label_coos:
            self.name_label_rects.append(pygame.Rect(coo, self.name_label_size))

        self.trash_coos: list[coordinate] = list(map(lambda x: rescaled(x, screen_size), CommonSettings.TRASH_COOS.value))
        self.trash_box_coo: coordinate = rescaled(CommonSettings.TRASH_BOX_COO.value, screen_size)
        self.trash_box_size: taglia = rescaled(CommonSettings.TRASH_BOX_SIZE.value, screen_size)
        self.trash_box_rect: Rect = pygame.Rect(self.trash_box_coo, self.trash_box_size)

        self.deck_coo: coordinate = rescaled(CommonSettings.DECK_COOS.value, screen_size)

        self.stacks_coo: coordinate = rescaled(CommonSettings.STACKS_COO.value, screen_size)
        self.stacks_box_coo: coordinate = rescaled(CommonSettings.STACKS_BOX_COO.value, screen_size)
        self.stacks_box_size: taglia = rescaled(CommonSettings.STACKS_BOX_SIZE.value, screen_size)
        self.stacks_box_rect: Rect = pygame.Rect(self.stacks_box_coo, self.stacks_box_size)

        self.clue_token_coo: coordinate = rescaled(CommonSettings.CLUE_TOKEN_COO.value, screen_size)
        self.pace_coo: coordinate = rescaled(CommonSettings.PACE_COO.value, screen_size)
        self.efficiency_coo: coordinate = rescaled(CommonSettings.EFFICIENCY_COO.value, screen_size)

        self.clue_window_coo: coordinate = rescaled(CommonSettings.CLUE_WINDOW_COO.value, screen_size)
        self.clue_window_size: taglia = rescaled(CommonSettings.CLUE_WINDOW_SIZE.value, screen_size)
        self.clue_arrow_size: taglia = rescaled(CommonSettings.CLUE_ARROW_SIZE.value, screen_size)
        self.x_button_coo: coordinate = rescaled(CommonSettings.X_BUTTON_COO.value, screen_size)
        self.x_button_size: taglia = rescaled(CommonSettings.X_BUTTON_SIZE.value, screen_size)
        self.giveclue_button_coo: coordinate = rescaled(CommonSettings.GIVECLUE_BUTTON_COO.value, screen_size)
        self.giveclue_button_size: taglia = rescaled(CommonSettings.GIVECLUE_BUTTON_SIZE.value, screen_size)

        self.warning_message_coo: coordinate = rescaled(CommonSettings.WARNING_MESSAGE_COO.value, screen_size)
        

def center_rectangles(size1: taglia, size2: taglia) -> coordinate:
    #Input: 2 pairs of rectangle coordinate
    #Output: How much you need to translate (x and y) the first rectangle to center it with respect to the second
    #Assuming they share the same top left corner
    return round_vect((size2 - size1)/2)

def rescaled(obj_size: taglia, screen_size: taglia) -> taglia:
    screen_size_copy = screen_size.copy()
    obj_size_copy = obj_size.copy()
    full_screen_size: taglia = Vect(1920, 1080)
    obj_size_copy[0] = obj_size_copy[0]*(screen_size_copy[0]/full_screen_size[0])
    obj_size_copy[1] = obj_size_copy[1]*(screen_size_copy[1]/full_screen_size[1])
    return round_vect(obj_size_copy)

def round_vect(vect: Vect) -> Vect:
    vect[0] = round(vect[0])
    vect[1] = round(vect[1])
    return vect

