from pygame.math import Vector2 as Vect
from enum import Enum

FULL_SCREEN: bool = True
WINDOW_WIDTH: int = 1000
WINDOW_HEIGHT: int = 600
DEFAULT_FONT: str = 'Calibri'
WHITE: tuple[int, int, int] = (255, 255, 255)
SALMON: tuple[int, int, int] = (255, 117, 31)

#per schermo intero
class CommonSettings(Enum):
    CARD_SIZE = Vect(85, 119)
    CARD_SPACING = 20
    NAME_LABEL_SIZE = Vect(200, 38)
    TRASH_COOS = [Vect(1300, 417), Vect(1300, 497), Vect(1300, 577), Vect(1300, 657), Vect(1300, 737)]
    TRASH_BOX_COO = Vect(1280, 410)
    TRASH_BOX_SIZE = Vect(640, 670)
    DECK_COOS = Vect(214, 759)
    STACKS_COO = Vect(14, 373)
    STACKS_BOX_COO = Vect(0, 358)
    STACKS_BOX_SIZE = Vect(514, 149)
    CLUE_TOKEN_COO = Vect(1680, 0)
    PACE_COO = Vect(1434, 90)
    EFFICIENCY_COO = Vect(1553, 181)
    CLUE_WINDOW_COO = Vect(10,10)
    CLUE_WINDOW_SIZE = Vect(300, 220)
    CLUE_ARROW_SIZE = Vect(50, 90)
    X_BUTTON_COO = Vect(250, 10)
    X_BUTTON_SIZE= Vect(40, 40)
    GIVECLUE_BUTTON_COO = Vect(110, 190)
    GIVECLUE_BUTTON_SIZE = Vect(100, 40)
    WARNING_MESSAGE_COO = Vect(10, 240)

#2 players
class TwoPlayers(Enum):
    HANDS_COOS = [Vect(647, 128), Vect(647, 301)]
    NAME_LABEL_COOS = [Vect(796, 255), Vect(796, 428)]


#3 players
class ThreePlayers(Enum):
    HANDS_COOS = [Vect(647, 128), Vect(647, 301), Vect(647, 474)]
    NAME_LABEL_COOS = [Vect(796, 255), Vect(796, 428), Vect(796, 601)]

#4 players
class FourPlayers(Enum):
    HANDS_COOS = [Vect(697, 128), Vect(697, 301), Vect(697, 474), Vect(697, 647)]
    NAME_LABEL_COOS = [Vect(796, 255), Vect(796, 428), Vect(796, 601), Vect(796, 774)]

#5 players
class FivePlayers(Enum):
    HANDS_COOS = [Vect(697, 128), Vect(697, 301), Vect(697, 474), Vect(697, 647), Vect(697, 820)]
    NAME_LABEL_COOS = [Vect(796, 255), Vect(796, 428), Vect(796, 601), Vect(796, 774), Vect(796, 947)]