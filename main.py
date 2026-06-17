from game_engine.game import Game
from game_engine.move import Move
from graphic_interface.graphic_settings import FULL_SCREEN
from game_engine.memory import History

import terminal_interface
import graphic_interface.graphic_interface as graphic_interface

def main():
    players_number, running = graphic_interface.get_number_of_players(FULL_SCREEN)
    if running:
        game = Game(players_number)
        history = History(players_number, game.deck)
        game.deal_cards()
        while game.running:
            terminal_interface.print_player_hand(game.current.player, game.current.others)
            move: Move = terminal_interface.ask_move(game, history)
            move.execute(game)
                
            game.update_exit_conditions()
            game.next_turn()
            terminal_interface.print_game_state(game)
        terminal_interface.print_end_message(game)
    history.record_history()

main()