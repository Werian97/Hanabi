import pygame

from pygame import Surface
from graphic_interface.graphic_settings import FULL_SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH
from graphic_interface.buttons import Button, create_num_players_buttons

def get_number_of_players(full_screen: bool) -> tuple[int, bool]:
    pygame.init()

    number_gotten = False
    running = True
    players_number: int

    buttons = pygame.sprite.Group()
    Button.containers = (buttons,)

    if full_screen:
        sizes = pygame.display.get_desktop_sizes()
        size = sizes[0]
    else:
        size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    window_width, window_height = size
    create_num_players_buttons(window_width, window_height)
    pygame.display.set_mode(size = (window_width, window_height))
    pygame.display.set_caption("Hanabi E.-Version")
    screen: Surface = pygame.display.get_surface()
    screen.fill("darkgreen")
    pygame.display.flip()

    clock = pygame.time.Clock()

    while (not number_gotten) and running:
        screen.fill("darkgreen")
        for event in pygame.event.get(): #if you remove this loop the window will freeze because the event qeue fills in and no one clear it
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 0, False  #exit the function. return False => in the main module the program exit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    return get_number_of_players(not full_screen)
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
    return players_number, running