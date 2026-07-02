from game_engine_modules.game import Game
from game_engine_modules.move import Move

from graphic_modules.painter import Painter

from memory_modules.history import History

import terminal_interface
import graphic_modules.graphic_interface as graphic_interface
from graphic_modules.updating_functions import set_up_match

def main():
    players_number = graphic_interface.get_number_of_players()
    if players_number == None:
        return
    
    game = Game(players_number)
    painter: Painter = graphic_interface.start_window(players_number=players_number)
    history = History(players_number, game.deck)
    set_up_match(game, painter.current_geometry)

    while game.running:
        move: Move = graphic_interface.ask_move(painter, game, history)
        move.execute(game)
        game.update_exit_conditions()
        game.next_turn()
        terminal_interface.print_game_state(game)
    terminal_interface.print_end_message(game)
    history.record_history()

main()