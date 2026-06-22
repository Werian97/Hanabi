from game_engine_modules.game import Game
from game_engine_modules.move import Move

from memory_modules.history import History

import terminal_interface
import graphic_modules.graphic_interface as graphic_interface

def main():
    players_number, exit_game = graphic_interface.get_number_of_players()
    if exit_game:
        return
    
    game = Game(players_number)
    geometry = graphic_interface.start_window(players_number, game)
    history = History(players_number, game.deck)
    game.deal_cards()

    while game.running:
        graphic_interface.ask_move(geometry, game, history)
        terminal_interface.print_player_hand(game.current.player, game.current.others)
        move: Move = terminal_interface.ask_move(game, history)
        move.execute(game)
                
        game.update_exit_conditions()
        game.next_turn()
        terminal_interface.print_game_state(game)
    terminal_interface.print_end_message(game)
    history.record_history()

main()