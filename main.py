from game import Game
from move import Move

from move import get_the_move

def main():
    game = Game()
    while game.running:
        move: Move = get_the_move(game)
        move.execute()
            
        game.update_exit_conditions()
        game.next_turn()
        print(game)

main()