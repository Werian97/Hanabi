from player import Player
from card import Card
from deck import Deck

from deck import get_hand_capacity, get_new_deck, calculate_points
from constants import INITIAL_CLUES, PLAYERS

class Game():
    def __init__(self):
        self.running = True
        self.turn: int = 0
        valid_player_count = False
        while not valid_player_count:
            try:
                self.players_number: int = int(input("How many players?: "))
                self.hand_capacity = get_hand_capacity(self.players_number)
                valid_player_count = True
            except ValueError:
                print("Only digits allowed")
            except Exception as e:
                print(e)

        self.deck: Deck = get_new_deck()
        self.clues: int = INITIAL_CLUES
        self.strikes: int = 0
        self.clock: int = 0
        self.stacks: Deck =[
            Card("0", "red"),
            Card("0", "yellow"),
            Card("0", "green"),
            Card("0", "blue"),
            Card("0", "purple"),
        ]
        self.trash: list[Deck] = [[], [], [], [], []]

        self.players: list[Player] = []
        self.current: PlayerAndOthers = PlayerAndOthers(self.players[0], self.players[1:])
        for i in range(0, self.players_number):
            self.players.append(Player(PLAYERS[i]))
            for j in range(0, self.hand_capacity):
                self.players[i].draw_a_card(self.deck)
        
        self.exit_conditions: ExitConditions = ExitConditions()
    
    def get_others_than(self, player: Player) -> list[Player]:
        others: list[Player] = []
        print("\n\n")
        print(f"{player.name} it's your turn. This is your hand:")
        print(player.hand)
        print("\n\n")
        print("These are other players' hands:")
        for npc in self.players:
            if npc is not player:
                others.append(npc)
                print(f"{npc.name}'s hand is \n{npc.hand}\n")
        return others
    
    def update_exit_conditions(self) -> None:
        if len(self.deck) == 0:
            self.clock += 1
        self.exit_conditions.striked = self.strikes >= 3
        self.exit_conditions.win = all(card.rank == 5 for card in self.stacks)
        self.exit_conditions.end = self.clock >= self.players_number
    
    def next_turn(self) -> None:
        if self.exit_conditions.win or self.exit_conditions.striked or self.exit_conditions.end:
            self.running = False
        else:
            self.next_player()
            self.turn += 1
    
    def next_player(self) -> None:
        j = self.players.index(self.current.player)
        if j == len(self.players)-1:
            self.current.player = self.players[0]
        else:
            self.current.player = self.players[j+1]
        self.current.others = self.get_others_than(self.current.player)

        
    
    def print_end_message(self):
        if self.exit_conditions.win or self.exit_conditions.end:
            points = calculate_points(self.stacks)
            print(f"CONGRATULATIONS! You totalized {points} points")
        else:
            print("Oh no! That was strike 3. The game is over. You totalized 0 points")
    
    def __str__(self):
        print(f"These are the stacks:\n{self.stacks}")
        print("\n")
        print(f"You have {self.clues} clues")
        print("\n")
        print(f"And this is the trash:\n{self.trash}")
        input("Press enter to continue...")
        return ""

class PlayerAndOthers():
    def __init__(self, player: Player, others: list[Player]):
        self.player: Player = player
        self.others: list[Player] = others

class ExitConditions():
    def __init__(self):
        self.win: bool = False
        self.striked: bool = False
        self.end: bool = False