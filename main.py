from deck import get_new_deck, get_hand_capacity
from deck import Deck
from player import Player
from constants import PLAYERS, INITIAL_CLUES

def main():
    condition = True
    players_number: int = 0
    while condition:
        try:
            players_number = int(input("How many players?"))
            hand_capacity = get_hand_capacity(players_number)
            condition = False
        except ValueError:
            print("Only digits allowed")
        except Exception as e:
            print(e)

    deck: Deck = get_new_deck()
    clues = INITIAL_CLUES

    players: list[Player] = []
    for i in range(0, players_number):
        players.append(Player(PLAYERS[i]))
        for j in range(0, hand_capacity):
            players[i].draw_a_card(deck)
    
    


main()