import pygame
from pygame.math import Vector2 as Vect

from graphic_modules.geometry import Geometry, center_rectangles
from graphic_modules.graphic_settings import DEFAULT_FONT

from collections.abc import Callable

class NumPlayerButton(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, left_top: tuple[int, int], width_height: tuple[int, int], text_inside: str, function: Callable):
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        
        self.rect = pygame.Rect(left_top, width_height)
        self.button_default_color = "white"
        self.button_mouse_is_over_color = "lightgray"
        self.text_color = "black"        
        self.text_inside = text_inside
        self.font_object = pygame.font.SysFont(name = DEFAULT_FONT, size = 20)
        self.function: Callable[[], int] = function


    def draw_button(self, screen: pygame.Surface) -> None:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            color = self.button_mouse_is_over_color
        else:
            color = self.button_default_color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, 2)
        rendered_text: pygame.Surface = self.font_object.render(self.text_inside, True, self.text_color)
        delta_x, delta_y = center_rectangles(Vect(rendered_text.get_size()), Vect(self.rect.size))
        screen.blit(rendered_text, (self.rect.left + delta_x, self.rect.top + delta_y))

def create_num_players_buttons(window_width: int, window_height: int):
    button_width, button_height, button_height_separation = 80, 50, 80
    left = round((window_width - button_width)/2)
    top = round((window_height - (3 * button_height_separation + button_height))/2)
    NumPlayerButton((left, top), (button_width, button_height), "2 players", lambda: 2)
    NumPlayerButton((left, top + button_height_separation), (button_width, button_height), "3 players", lambda: 3)
    NumPlayerButton((left, top + 2*button_height_separation), (button_width, button_height), "4 players", lambda: 4)
    NumPlayerButton((left, top + 3*button_height_separation), (button_width, button_height), "5 players", lambda: 5)


class CardButton(pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.position: Vect
        self.rect: pygame.Rect
        self.is_pressed: bool = False
    
    def update_position(self, movement: Vect) -> None:
        self.position = self.position + movement
        self.rect.move_ip(movement)

class ClueButton():
    def __init__(self, position: Vect, screen: pygame.Surface):
        self.position: Vect = position
        self.size: tuple[int, int] = (40, 40)
        self.rect: pygame.Rect = pygame.Rect(self.position, self.size)
        self.screen: pygame.Surface = screen
        self.rect: pygame.Rect = pygame.Rect(self.position, self.size)
        self.is_clicked = False
    
    def update_border_color(self):
        if self.is_clicked:
            pygame.draw.rect(self.screen, "black", self.rect, 2)
        else:
            pygame.draw.rect(self.screen, "white", self.rect, 2)


class ClueSuitButton(ClueButton):
    def __init__(self, position: Vect, suit: str, screen: pygame.Surface):
        super().__init__(position, screen)
        self.suit = suit
        pygame.draw.rect(self.screen, self.suit, self.rect)
        pygame.draw.rect(self.screen, "white", self.rect, 2)
        pygame.display.flip()

class ClueRankButton(ClueButton):
    def __init__(self, position: Vect, rank: str, screen: pygame.Surface):
        super().__init__(position, screen)
        self.rank = rank
        pygame.draw.rect(self.screen, "white", self.rect)
        font_obj = pygame.font.SysFont(DEFAULT_FONT, 40)
        self.image: pygame.Surface = font_obj.render(self.rank, True, 'black', 'white')
        delta_x, delta_y = center_rectangles(Vect(self.image.get_rect().size), Vect(self.rect.size))
        text_position = (self.position[0] + delta_x, self.position[1] + delta_y)
        screen.blit(self.image, text_position)
        pygame.display.flip()

def create_clue_buttons(screen: pygame.Surface) -> list:
    buttons = []

    buttons.append(ClueSuitButton(Vect(20, 80), "red", screen))
    buttons.append(ClueSuitButton(Vect(80, 80), "yellow", screen))
    buttons.append(ClueSuitButton(Vect(140, 80), "green", screen))
    buttons.append(ClueSuitButton(Vect(200, 80), "blue", screen))
    buttons.append(ClueSuitButton(Vect(260, 80), "purple", screen))

    buttons.append(ClueRankButton(Vect(20, 140), "1", screen))
    buttons.append(ClueRankButton(Vect(80, 140), "2", screen))
    buttons.append(ClueRankButton(Vect(140, 140), "3", screen))
    buttons.append(ClueRankButton(Vect(200, 140), "4", screen))
    buttons.append(ClueRankButton(Vect(260, 140), "5", screen))

    return buttons