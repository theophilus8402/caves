
import curses

def initialize_colors():

    curses.start_color()
    curses.use_default_colors()

    global red
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    red = curses.color_pair(1)

    global green
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    green = curses.color_pair(2)

    global yellow
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    yellow = curses.color_pair(3)

    global white
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
    white = curses.color_pair(4)

red = None
green = None
yellow = None
white = None
#red = curses.A_REVERSE
