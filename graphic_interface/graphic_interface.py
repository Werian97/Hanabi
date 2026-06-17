import pygame

from pygame import Surface
from graphic_interface.graphic_settings import FULL_SCREEN, WINDOW_HEIGHT, WINDOW_WIDTH

def get_number_of_players() -> tuple[int, bool]:
    number_gotten = False
    running = True

    two_player_button = pygame.Rect((400, 300), (50, 50))

    pygame.display.set_mode(size = (WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Hanabi E.-Version")
    screen: Surface = pygame.display.get_surface()
    screen.fill("darkgreen")
    pygame.draw.rect(screen, "white", two_player_button)
    pygame.display.flip()

    clock = pygame.time.Clock()

    while (not number_gotten) and running:
        screen.fill("darkgreen")
        pygame.draw.rect(screen, "white", two_player_button)
        for event in pygame.event.get(): #if you remove this loop the window will freeze because the event qeue fills in and no one clear it
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return 0, False  #exit the function. return False => in the main module the program exit
            elif event.type == pygame.MOUSEMOTION:
                screen.fill("red")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill("blue")
        
        pygame.display.flip()
        clock.tick(60) #end of loop. restart

    pygame.display.quit()
    return 0, running