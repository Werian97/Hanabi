from deck import get_new_deck, get_hand_capacity
from deck import Deck
from player import Player
from constants import PLAYERS, INITIAL_CLUES
from moves import determine_move

def main():
    condition = True
    players_number: int = 0
    while condition:
        try:
            players_number = int(input("How many players? "))
            hand_capacity = get_hand_capacity(players_number)
            condition = False
        except ValueError:
            print("Only digits allowed")
        except Exception as e:
            print(e)

    deck: Deck = get_new_deck()
    clues: int = INITIAL_CLUES
    strikes: int = 0
    stacks: Deck =[
        (0, "red"),
        (0, "yellow"),
        (0, "green"),
        (0, "blue"),
        (0, "purple"),
    ]
    trash: list[Deck] = [[], [], [], [], []]
    running = True

    players: list[Player] = []
    for i in range(0, players_number):
        players.append(Player(PLAYERS[i]))
        for j in range(0, hand_capacity):
            players[i].draw_a_card(deck)
    
    
    while running:
        for i in range(0,players_number):
            valid_input = False
            print(players[i].hand)
            while valid_input == False:
                try:
                    move: str = determine_move(input(f"{players[i].name} it's your turn. What do you want to do? (Play: P, Clue: C, Discard: D) "))
                    valid_input = True
                except Exception as e:
                    print(e)
            if move == "play":
                success: bool = players[i].play(stacks)
                if not success:
                    print("STRIKE")
                    strikes += 1
                if len(deck) > 0:
                    players[i].draw_a_card(deck)
            elif move == "discard":
                players[i].discard(trash)
                if len(deck) > 0:
                    players[i].draw_a_card(deck)
    


main()