import pygame
from enum import Enum

FULL_SCREEN: bool = True
WINDOW_WIDTH: int = 1000
WINDOW_HEIGHT: int = 600

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
    CARD_SIZE = (85, 119)
    CARD_SPACING = 15
    NAME_LABEL_SIZE = (154, 38)
    HANDS_COOS = [(526, 8), (526, 181)]
    NAME_LABEL_COOS = [(691, 135), (691, 308)]
    TRASH_CARD_SIZE = (85, 119)
    TRASH_COOS = [(1066, 185), (1066, 323), (1066, 461), (1066, 599), (1066, 737)]
    TRASH_BOX_COO = (1051, 170)
    TRASH_BOX_SIZE = (512, 691)
    DECK_COOS = (214, 632)
    STACKS_COO = (14, 373)
    STACKS_BOX_COO = (0, 358)
    STACKS_BOX_SIZE = (514, 149)
    META_DATA_SIZE = (170, 119)
    META_DATA_COO = (1195, 27)


#3 players
class ThreePlayers(Enum):
    CARD_SIZE = (85, 119)
    CARD_SPACING = 15
    NAME_LABEL_SIZE = (154, 38)
    HANDS_COOS = [(526, 8), (526, 181), (526, 354)]
    NAME_LABEL_COOS = [(691, 135), (691, 308), (691, 481)]
    TRASH_CARD_SIZE = (85, 119)
    TRASH_COOS = [(1066, 185), (1066, 323), (1066, 461), (1066, 599), (1066, 737)]
    TRASH_BOX_COO = (1051, 170)
    TRASH_BOX_SIZE = (512, 691)
    DECK_COOS = (214, 632)
    STACKS_COO = (14, 373)
    STACKS_BOX_COO = (0, 358)
    STACKS_BOX_SIZE = (514, 149)
    META_DATA_SIZE = (170, 119)
    META_DATA_COO = (1195, 27)

#4 players
class FourPlayers(Enum):
    CARD_SIZE = (85, 119)
    CARD_SPACING = 15
    NAME_LABEL_SIZE = (154, 38)
    HANDS_COOS = [(576, 8), (576, 181), (576, 354), (576, 527)]
    NAME_LABEL_COOS = [(691, 135), (691, 308), (691, 481), (691, 654)]
    TRASH_CARD_SIZE = (85, 119)
    TRASH_COOS = [(1066, 185), (1066, 323), (1066, 461), (1066, 599), (1066, 737)]
    TRASH_BOX_COO = (1051, 170)
    TRASH_BOX_SIZE = (512, 691)
    DECK_COOS = (214, 632)
    STACKS_COO = (14, 373)
    STACKS_BOX_COO = (0, 358)
    STACKS_BOX_SIZE = (514, 149)
    META_DATA_SIZE = (170, 119)
    META_DATA_COO = (1195, 27)

#5 players
class FivePlayers(Enum):
    CARD_SIZE = (85, 119)
    CARD_SPACING = 15
    NAME_LABEL_SIZE = (154, 38)
    HANDS_COOS = [(576, 8), (576, 181), (576, 354), (576, 527), (576, 700)]
    NAME_LABEL_COOS = [(691, 135), (691, 308), (691, 481), (691, 654), (691, 827)]
    TRASH_CARD_SIZE = (85, 119)
    TRASH_COOS = [(1066, 185), (1066, 323), (1066, 461), (1066, 599), (1066, 737)]
    TRASH_BOX_COO = (1051, 170)
    TRASH_BOX_SIZE = (512, 691)
    DECK_COOS = (214, 632)
    STACKS_COO = (14, 373)
    STACKS_BOX_COO = (0, 358)
    STACKS_BOX_SIZE = (514, 149)
    META_DATA_SIZE = (170, 119)
    META_DATA_COO = (1195, 27)