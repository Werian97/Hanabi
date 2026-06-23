from graphic_modules.graphic_settings import CARD_WIDTH, CARD_HEIGHT, CARD_SPACING, NAME_LABEL_WIDTH, NAME_LABEL_HEIGHT
from graphic_modules.graphic_settings import TwoPlayers, ThreePlayers, FourPlayers, FivePlayers

import pygame
from pygame import Surface

coordinate = tuple[int, int]
taglia = tuple[int, int]

class Geometry():
    def __init__(self, players_number: int, screen: Surface):
        self.screen: Surface = screen
        self.players_number: int = players_number
        self.window_size: coordinate = screen.get_size()
        match players_number:
            case 2:
                PlayersNumber = TwoPlayers
            case 3:
                PlayersNumber = ThreePlayers
            case 4:
                PlayersNumber = FourPlayers
            case 5:
                PlayersNumber = FivePlayers

        self.card_size: taglia = rescaled((CARD_WIDTH, CARD_HEIGHT), self.window_size)
        self.card_spacing, _ = rescaled((CARD_SPACING, 0), self.window_size)
        self.name_label_size: taglia = rescaled((NAME_LABEL_WIDTH, NAME_LABEL_HEIGHT), self.window_size)
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

def center_rectangles(width_1: int, height_1: int, width_2: int, height_2: int) -> coordinate:
    #Input: 2 pairs of rectangle coordinate
    #Output: How much you need to translate (x and y) the first rectangle to center it with respect to the second
    #Assuming they share the same top left corner
    return round((width_2 - width_1)/2), round((height_2 - height_1)/2)

def rescaled(obj_size: taglia, window_size: taglia) -> taglia:
    full_screen_size: taglia = pygame.display.get_desktop_sizes()[0]
    return round(obj_size[0]*(window_size[0]/full_screen_size[0])), round(obj_size[1]*(window_size[1]/full_screen_size[1]))
