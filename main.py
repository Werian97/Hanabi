from deck import get_new_deck, get_hand_capacity
from deck import Deck
from player import Player, clue_someone
from constants import PLAYERS, INITIAL_CLUES
from constants import Card
from moves import determine_move

def main():
    condition = True
    players_number: int = 0
    while condition:
        try:
            players_number = int(input("How many players?: "))
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
        Card(0, "red"),
        Card(0, "yellow"),
        Card(0, "green"),
        Card(0, "blue"),
        Card(0, "purple"),
    ]
    trash: list[Deck] = [[], [], [], [], []]
    running = True

    players: list[Player] = []
    for i in range(0, players_number):
        players.append(Player(PLAYERS[i]))
        for j in range(0, hand_capacity):
            players[i].draw_a_card(deck)
    
    
    while running:
        for player in players:
            valid_input = False
            print("\n\n")
            print(f"{player.name} it's your turn. This is your hand:")
            print(player.hand)
            print("\n\n")
            print("These are other players' hands:")
            for npc in players:
                if npc is not player:
                    print(f"{npc.name}'s hand is \n{npc.hand}")
                    print("\n")
            while valid_input == False:
                try:
                    move: str = determine_move(clues, input("What do you want to do? (Play: P, Clue: C, Discard: D): "))
                    valid_input = True
                except Exception as e:
                    print(e)
            if move == "play":
                success: bool = player.play(stacks)
                if not success:
                    print("STRIKE")
                    strikes += 1
                if len(deck) > 0:
                    player.draw_a_card(deck)
            elif move == "discard":
                player.discard(trash)
                clues += 1
                if len(deck) > 0:
                    player.draw_a_card(deck)
            else: #move == clue
                clue_someone(players)
                clues -= 1
            print(f"These is the stacks:\n{stacks}")
            print("\n")
            print(f"You have {clues} clues")
            print("\n")
            print(f"And this is the trash:\n{trash}")

    


main()