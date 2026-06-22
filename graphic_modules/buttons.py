import pygame

from graphic_modules.screen_geometry import center_rectangles

from collections.abc import Callable

class Button(pygame.sprite.Sprite):
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
        self.font_object = pygame.font.SysFont(name = 'calibri', size = 20)
        self.function: Callable = function


    def draw_button(self, screen: pygame.Surface) -> None:
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            color = self.button_mouse_is_over_color
        else:
            color = self.button_default_color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, "black", self.rect, 2)
        rendered_text: pygame.Surface = self.font_object.render(self.text_inside, True, self.text_color)
        delta_x, delta_y = center_rectangles(*rendered_text.get_size(), *self.rect.size)
        screen.blit(rendered_text, (self.rect.left + delta_x, self.rect.top + delta_y))

def create_num_players_buttons(window_width: int, window_height: int):
    button_width, button_height, button_height_separation = 80, 50, 80
    left = round((window_width - button_width)/2)
    top = round((window_height - (3 * button_height_separation + button_height))/2)
    Button((left, top), (button_width, button_height), "2 players", lambda: 2)
    Button((left, top + button_height_separation), (button_width, button_height), "3 players", lambda: 3)
    Button((left, top + 2*button_height_separation), (button_width, button_height), "4 players", lambda: 4)
    Button((left, top + 3*button_height_separation), (button_width, button_height), "5 players", lambda: 5)