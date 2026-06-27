import pygame

from pygame.math import Vector2 as Vect
from enum import Enum

FULL_SCREEN: bool = True
WINDOW_WIDTH: int = 1000
WINDOW_HEIGHT: int = 600
DEFAULT_FONT: str = 'Calibri'

#constants in case the game is at full screen.
#need to rescale them otherwise
pygame.init()
desktop_size = pygame.display.get_desktop_sizes()[0]
CARD_WIDTH: int = round(desktop_size[0]/18)
CARD_HEIGHT: int = round(1.4 * CARD_WIDTH)
CARD_SPACING: int = round(desktop_size[0]/100)
NAME_LABEL_WIDTH: int = round(desktop_size[0]/10)
NAME_LABEL_HEIGHT: int = round(0.25 * NAME_LABEL_WIDTH)

#2 players
class TwoPlayers(Enum):
    CARD_SIZE = Vect(85, 119)
    CARD_SPACING = 15
    NAME_LABEL_SIZE = Vect(180, 38)
    HANDS_COOS = [Vect(526, 8), Vect(526, 181)]
    NAME_LABEL_COOS = [Vect(678, 135), Vect(678, 308)]
    TRASH_CARD_SIZE = Vect(85, 119)
    TRASH_COOS = [Vect(1066, 185), Vect(1066, 323), Vect(1066, 461), Vect(1066, 599), Vect(1066, 737)]
    TRASH_BOX_COO = Vect(1051, 170)
    TRASH_BOX_SIZE = Vect(512, 691)
    DECK_COOS = Vect(214, 632)
    STACKS_COO = Vect(14, 373)
    STACKS_BOX_COO = Vect(0, 358)
    STACKS_BOX_SIZE = Vect(514, 149)
    META_DATA_SIZE = Vect(170, 119)
    META_DATA_COO = Vect(1100, 27)


#3 players
class ThreePlayers(Enum):
    CARD_SIZE = Vect(85, 119)
    CARD_SPACING = 15
    NAME_LABEL_SIZE = Vect(180, 38)
    HANDS_COOS = [Vect(526, 8), Vect(526, 181), Vect(526, 354)]
    NAME_LABEL_COOS = [Vect(678, 135), Vect(678, 308), Vect(678, 481)]
    TRASH_CARD_SIZE = Vect(85, 119)
    TRASH_COOS = [Vect(1066, 185), Vect(1066, 323), Vect(1066, 461), Vect(1066, 599), Vect(1066, 737)]
    TRASH_BOX_COO = Vect(1051, 170)
    TRASH_BOX_SIZE = Vect(512, 691)
    DECK_COOS = Vect(214, 632)
    STACKS_COO = Vect(14, 373)
    STACKS_BOX_COO = Vect(0, 358)
    STACKS_BOX_SIZE = Vect(514, 149)
    META_DATA_SIZE = Vect(170, 119)
    META_DATA_COO = Vect(1100, 27)

#4 players
class FourPlayers(Enum):
    CARD_SIZE = Vect(85, 119)
    CARD_SPACING = 15
    NAME_LABEL_SIZE = Vect(180, 38)
    HANDS_COOS = [Vect(576, 8), Vect(576, 181), Vect(576, 354), Vect(576, 527)]
    NAME_LABEL_COOS = [Vect(678, 135), Vect(678, 308), Vect(678, 481), Vect(678, 654)]
    TRASH_CARD_SIZE = Vect(85, 119)
    TRASH_COOS = [Vect(1066, 185), Vect(1066, 323), Vect(1066, 461), Vect(1066, 599), Vect(1066, 737)]
    TRASH_BOX_COO = Vect(1051, 170)
    TRASH_BOX_SIZE = Vect(512, 691)
    DECK_COOS = Vect(214, 632)
    STACKS_COO = Vect(14, 373)
    STACKS_BOX_COO = Vect(0, 358)
    STACKS_BOX_SIZE = Vect(514, 149)
    META_DATA_SIZE = Vect(170, 119)
    META_DATA_COO = Vect(1100, 27)

#5 players
class FivePlayers(Enum):
    CARD_SIZE = Vect(85, 119)
    CARD_SPACING = 15
    NAME_LABEL_SIZE = Vect(200, 38)
    HANDS_COOS = [Vect(576, 8), Vect(576, 181), Vect(576, 354), Vect(576, 527), Vect(576, 700)]
    NAME_LABEL_COOS = [Vect(678, 135), Vect(678, 308), Vect(678, 481), Vect(678, 654), Vect(678, 827)]
    TRASH_CARD_SIZE = Vect(85, 119)
    TRASH_COOS = [Vect(1066, 185), Vect(1066, 323), Vect(1066, 461), Vect(1066, 599), Vect(1066, 737)]
    TRASH_BOX_COO = Vect(1051, 170)
    TRASH_BOX_SIZE = Vect(512, 691)
    DECK_COOS = Vect(214, 632)
    STACKS_COO = Vect(14, 373)
    STACKS_BOX_COO = Vect(0, 358)
    STACKS_BOX_SIZE = Vect(514, 149)
    META_DATA_SIZE = Vect(170, 119)
    META_DATA_COO = Vect(1100, 27)