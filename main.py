from deck import get_new_deck, get_hand_capacity, calculate_points
from deck import Deck
from player import Player
from constants import PLAYERS, INITIAL_CLUES
from constants import Card
from moves import determine_move
from clues import clue_someone
from functools import reduce

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
    clock: int = 0
    stacks: Deck =[
        Card("0", "red"),
        Card("0", "yellow"),
        Card("0", "green"),
        Card("0", "blue"),
        Card("0", "purple"),
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
            others: list[Player] = []
            print("\n\n")
            print(f"{player.name} it's your turn. This is your hand:")
            print(player.hand)
            print("\n\n")
            print("These are other players' hands:")
            for npc in players:
                if npc is not player:
                    others.append(npc)
                    print(f"{npc.name}'s hand is \n{npc.hand}\n")
            while valid_input == False:
                try:
                    move: str = determine_move(clues, input("What do you want to do? (Play: P, Clue: C, Discard: D): "))
                    valid_input = True
                except Exception as e:
                    print(e)
            if move == "clue":
                clue_someone(others)
                clues -= 1
            else:
                if move == "play":
                    (success, just_played_five) = player.play(stacks, trash)
                    if not success:
                        print("STRIKE")
                        strikes += 1
                    if just_played_five:
                        clues = min(8, clues + 1)
                elif move == "discard":
                    player.discard(trash)
                    clues += 1
                
                #after the play or discard
                if len(deck) > 0:
                        player.draw_a_card(deck)
            if len(deck) == 0:
                clock += 1

            loss_condition = strikes >= 3
            win_condition = reduce(lambda check, card: check and card.rank == 5, stacks, True)
            end_game = clock >= players_number
            
            if win_condition or end_game:
                running = False
                points = calculate_points(stacks)
                print(f"CONGRATULATIONS! You totalized {points} points")
            elif loss_condition:
                running = False
                print("Oh no! That was strike 3. The game is over. You totalized 0 points")
            else:
                print(f"These are the stacks:\n{stacks}")
                print("\n")
                print(f"You have {clues} clues")
                print("\n")
                print(f"And this is the trash:\n{trash}")
                input("Press enter to continue...")

    


main()