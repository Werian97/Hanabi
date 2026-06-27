from game_engine_modules.game import Game
from game_engine_modules.move import Move, Discard

from memory_modules.history import History

import terminal_interface
import graphic_modules.graphic_interface as graphic_interface
from graphic_modules.updating_functions import update_trash_positions

def main():
    players_number, exit_game = graphic_interface.get_number_of_players()
    if exit_game:
        return
    
    game = Game(players_number)
    geometry = graphic_interface.start_window(players_number, game)
    history = History(players_number, game.deck)
    game.deal_cards()

    while game.running:
        move: Move = graphic_interface.ask_move(geometry, game, history)
        move.execute(game)
        if isinstance(move, Discard):
            update_trash_positions(geometry, game)
        game.update_exit_conditions()
        game.next_turn()
        terminal_interface.print_game_state(game)
    terminal_interface.print_end_message(game)
    history.record_history()

main()