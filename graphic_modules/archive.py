import pygame
from pygame import Surface
from pygame.font import Font

from graphic_modules.geometry import Geometry

from graphic_modules.graphic_settings import DEFAULT_FONT, WHITE, SALMON

from game_engine_modules.constants import SUITS, RANKS


class Archive():
    def __init__(self, geometry: Geometry):
        self.back_card: Surface = pygame.transform.scale(pygame.image.load("assets/images/basic/back.png"), geometry.card_size)
        self.remaining_cards: Font = pygame.font.SysFont(name = DEFAULT_FONT, size = 55)#font size to be resized

        self.cards: dict[str, Surface] = {}
        self.clued_cards: dict[str, Surface] = {}
        self.cmed_cards: dict[str, Surface] = {}
        self.finessed_cards: dict[str, Surface] = {}

        self.background: Surface = pygame.transform.scale(pygame.image.load(f"assets/images/background/{geometry.players_number}_players_background.png"), geometry.screen_size)
        self.clue_arrows: dict[str, Surface] = {
            "new": pygame.transform.scale(pygame.image.load("assets/images/clue_material/new.png"), geometry.clue_arrow_size),
            "old": pygame.transform.scale(pygame.image.load("assets/images/clue_material/new.png"), geometry.clue_arrow_size)
        }
        self.clue_window: Surface = pygame.transform.scale(pygame.image.load("assets/images/clue_material/clue_window.png"), geometry.clue_window_size)
        
        self.clues: Font = pygame.font.SysFont(name = DEFAULT_FONT, size = 30)
        self.efficiency: Font = pygame.font.SysFont(name = DEFAULT_FONT, size = 30)
        self.pace: Font = pygame.font.SysFont(name = DEFAULT_FONT, size = 30)
        
        self.load_all(geometry)
        self.clear_background()
    
    def load_all(self, geometry: Geometry):
        load_basic_cards(self, geometry)
        load_clued_cards(self, geometry)
        load_cmed_cards(self, geometry)
        load_finessed_cards(self, geometry)
    
    def clear_background(self):
        self.back_card.set_colorkey(WHITE)
        all_card_images = [self.cards, self.clued_cards, self.cmed_cards, self.finessed_cards]
        for d in all_card_images:
            for value in d.values():
                value.set_colorkey(WHITE)

        self.clue_arrows["new"].set_colorkey(SALMON)
        self.clue_arrows["old"].set_colorkey(SALMON)
        
        self.clue_window.set_colorkey(WHITE)
        


def load_basic_cards(archive: Archive, geometry: Geometry):
    for suit in SUITS:
        archive.cards[f"{suit}0"] = pygame.transform.scale(pygame.image.load(f"assets/images/basic/{suit}0.png"), geometry.card_size)
        for rank in RANKS:
            archive.cards[f"{suit}{rank}"] = pygame.transform.scale(pygame.image.load(f"assets/images/basic/{suit}{rank}.png"), geometry.card_size)

def load_clued_cards(archive: Archive, geometry: Geometry):
    for suit in SUITS:
        for rank in RANKS:
            archive.clued_cards[f"{suit}{rank}"] = pygame.transform.scale(pygame.image.load(f"assets/images/clued/{suit}{rank}.png"), geometry.card_size)

def load_cmed_cards(archive: Archive, geometry: Geometry):
    for suit in SUITS:
        for rank in RANKS:
            archive.cmed_cards[f"{suit}{rank}"] = pygame.transform.scale(pygame.image.load(f"assets/images/cmed/{suit}{rank}.png"), geometry.card_size)

def load_finessed_cards(archive: Archive, geometry: Geometry):
    for suit in SUITS:
        for rank in RANKS:
            archive.finessed_cards[f"{suit}{rank}"] = pygame.transform.scale(pygame.image.load(f"assets/images/finessed/{suit}{rank}.png"), geometry.card_size)