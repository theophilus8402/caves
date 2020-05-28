
import curses

def initialize_colors():

    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    global red
    red = curses.color_pair(1)

red = None
#red = curses.A_REVERSE
