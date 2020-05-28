
import curses

import color

from ui.core import UI, UIKind
from ui.drawing import draw_game
from ui.input import get_input, process_input
from world import World
from game import Game


def run_game(stdscr, game):
    while len(game.uis) > 0:

        draw_game(stdscr, game)

        if len(game.input) > 0:
            user_input = game.input.pop()
            process_input(game, user_input)
        else:
            get_input(stdscr, game)


def main(stdscr):

    color.initialize_colors()

    world = World("wally's world")
    game = Game(world)
    game.location = (40, 20)
    start_ui = UI(UIKind.start)
    game.uis.append(start_ui)

    run_game(stdscr, game)


if __name__ == "__main__":

    curses.wrapper(main)
