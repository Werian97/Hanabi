import pygame

from pygame import Surface
from pygame.math import Vector2 as Vect

from game_engine_modules.card import Card
from game_engine_modules.game import Game
from graphic_modules.archive import Archive, Geometry
from graphic_modules.graphic_settings import DEFAULT_FONT, FULL_SCREEN

Archives = tuple[Archive, Archive]
Geometries = tuple[Geometry, Geometry]

class Painter():
    def __init__(self, screen: Surface, geometries: Geometries, archives: Archives):
        self.screen: Surface = screen
        self.full_screen: bool = FULL_SCREEN
        self.geometries: Geometries = geometries
        self.archives: Archives = archives
        self.current_geometry: Geometry = geometries[FULL_SCREEN]
        self.current_archive: Archive = archives[FULL_SCREEN]
        
        #ask_move tools:
        self.card_positions_updated: bool = False

        #warning messages:
        self.clue_token_warning_message: Surface = pygame.font.SysFont(DEFAULT_FONT, 40).render("No clue token left", True, "Black")
        self.empty_clue_warning_message: Surface = pygame.font.SysFont(DEFAULT_FONT, 40).render("No empty clue allowed", True, "black")
    
    def switch_FS_WND(self) -> None:
        pygame.display.quit()
        pygame.display.init()
        self.full_screen = not self.full_screen
        self.current_geometry: Geometry = self.geometries[self.full_screen]
        self.current_archive: Archive = self.archives[self.full_screen]
        self.screen = pygame.display.set_mode(self.current_geometry.screen_size)
        self.card_positions_updated = False
    
    def display_warning_message(self, message: Surface):
        geometry = self.current_geometry
        self.screen.blit(message, geometry.warning_message_coo)
    
    def draw(self, obj: Card | list) -> None:
        archive = self.current_archive
        geometry = self.current_geometry
        if isinstance(obj, Card):
            if obj.is_clued:
                self.screen.blit(archive.clued_cards.get(f"{obj.suit}{obj.rank}"), obj.button.position + Vect(0,-5)) # type: ignore
            else:
                self.screen.blit(archive.cards.get(f"{obj.suit}{obj.rank}"), obj.button.position) # type: ignore
        else:
            if obj[0] == "Deck":
                self.screen.blit(archive.back_card, geometry.deck_coo)
                self.screen.blit(archive.remaining_cards.render(f"{obj[1]}", True, "black"), geometry.deck_coo)
            elif obj[0] == "Metadata":
                self.screen.blit(archive.remaining_cards.render(f"{obj[1]}", True, "black"), geometry.clue_token_coo)
                self.screen.blit(archive.remaining_cards.render(f"{obj[2]}", True, "black"), geometry.pace_coo)
                self.screen.blit(archive.remaining_cards.render(f"{obj[3]}", True, "black"), geometry.efficiency_coo)
            elif obj[0] == "Background":
                self.screen.blit(archive.background, (0,0))

    def draw_game(self, game: Game):
        self.draw(["Background"])
        for player in game.current.others:
            for card in player.hand:
                self.draw(card)
        
        for i in range(5):
            card: Card = game.stacks[i]
            self.draw(card)
        
        for i in range(5):
            for card in game.trash[i]:
                self.draw(card)
        
        self.draw(["Deck", len(game.deck)])
        self.draw(["Metadata", game.clues, game.pace, game.efficiency])

        for card in game.current.player.hand:
            self.draw(card)
        
        pygame.display.flip()