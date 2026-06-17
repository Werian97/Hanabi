from game_engine.game import Game
from game_engine.move import Move

import terminal_interface
import graphic_interface.graphic_interface as graphic_interface
import pygame

def main():
    pygame.init()
    players_number, running = graphic_interface.get_number_of_players()
    running = True
    if running:
        players_number = terminal_interface.get_number_of_players()
        game = Game(players_number)
        while game.running:
            terminal_interface.print_player_hand(game.current.player, game.current.others)
            move: Move = terminal_interface.ask_move(game)
            move.execute(game)
                
            game.update_exit_conditions()
            game.next_turn()
            terminal_interface.print_game_state(game)
        terminal_interface.print_end_message(game)

main()