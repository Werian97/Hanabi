from game_engine_modules.player import Player
from game_engine_modules.card import Card
from game_engine_modules.deck import Deck
from game_engine_modules.constants import HandCapacity

from game_engine_modules.deck import get_new_deck, calculate_points
from game_engine_modules.constants import INITIAL_CLUES, PLAYERS

class Game():
    def __init__(self, players_number):
        self.running: bool = True
        self.players_number: int = players_number
        match players_number:
            case 2:
                self.hand_capacity: int = HandCapacity.TWO.value
            case 3:
                self.hand_capacity: int = HandCapacity.THREE.value
            case 4:
                self.hand_capacity: int = HandCapacity.FOUR.value
            case 5:
                self.hand_capacity: int = HandCapacity.FIVE.value
        self.turn: int = 1 #number of turns
        self.deck: Deck = get_new_deck() #shuffled deck
        self.all_cards: Deck = self.deck.copy()
        self.clues: int = INITIAL_CLUES #initial clue tokens (8)
        self.strikes: int = 0 #strikes
        self.clock: int = 0 #it ticks the last round of the game
        self.stacks: Deck =[ #initialized stacks
            Card("0", "red"),
            Card("0", "yellow"),
            Card("0", "green"),
            Card("0", "blue"),
            Card("0", "purple"),
        ]
        self.trash: list[Deck] = [[], [], [], [], []] #initialized trash
        self.players: list[Player] = [] #empty list of players. populated by the next for-cycle
        self.current: PlayerAndOthers
        self.exit_conditions: ExitConditions = ExitConditions() #[stack_completed, strike_exceeded, clock's_over]
        self.final_score: int = 0

    def update_others_than(self, player: Player) -> None:
        self.current.others = []
        for npc in self.players:
            if npc is not player:
                self.current.others.append(npc)
    
    def update_exit_conditions(self) -> None:
        if len(self.deck) == 0:
            self.clock += 1
        self.exit_conditions.striked = self.strikes >= 3
        self.exit_conditions.win = all(card.rank == 5 for card in self.stacks)
        self.exit_conditions.end = self.clock >= self.players_number
    
    def next_turn(self) -> None:
        if self.exit_conditions.win or self.exit_conditions.striked or self.exit_conditions.end:
            self.running = False
            if not self.exit_conditions.end:
                self.final_score = calculate_points(self.stacks)
        else:
            self.next_player()
            self.turn += 1
    
    def next_player(self) -> None:
        j = self.players.index(self.current.player)
        if j == len(self.players)-1:
            self.current.player = self.players[0]
        else:
            self.current.player = self.players[j+1]
        self.update_others_than(self.current.player)
    
    def deal_cards(self) -> None:
        for i in range(0, self.players_number):
            self.players.append(Player(PLAYERS[i]))
            for _ in range(0, self.hand_capacity):
                self.players[i].draw_a_card(self.deck)
        self.current: PlayerAndOthers = PlayerAndOthers(self.players[0], self.players[1:]) #it store in each turn who's playing and who's watching

class PlayerAndOthers():
    def __init__(self, player: Player, others: list[Player]):
        self.player: Player = player
        self.others: list[Player] = others

class ExitConditions():
    def __init__(self):
        self.win: bool = False
        self.striked: bool = False
        self.end: bool = False