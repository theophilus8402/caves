
import math

import color

from entities.core import get_entity
from ui.core import UIKind


screen_size = (80, 24)


def draw_hud(stdscr, game, start_x, start_y):
    screen_width, screen_height = screen_size
    hud_row = screen_height - 1
    player = get_entity(game.world, "player")
    x, y = player.location
    hud_line = f"Loc: [{x}-{y}] start: [{start_x}-{start_y}]"
    stdscr.addstr(hud_row, 0, hud_line)


def draw_ui_start(stdscr, ui, game):
    stdscr.addstr(0, 0, "Welcome to the Caves!")
    stdscr.addstr(1, 0, "Press e to win, anything else to lose.")

def draw_ui_play(stdscr, ui, game):
    stdscr.addstr(0, 0, f"Press e to win, s to smooth, anything else to lose. {game.location}")

    cols, rows = screen_size
    vcols = cols
    vrows = rows - 2
    player = get_entity(game.world, "player")
    start_x, start_y, end_x, end_y = get_viewport_coords(game,
                                                         player.location,
                                                         vcols,
                                                         vrows)

    tiles = game.world.tiles
    draw_world(stdscr, vrows, vcols, start_x, start_y, end_x, end_y, tiles)
    draw_hud(stdscr, game, start_x, start_y)
    draw_player(stdscr, (start_x, start_y), player)

def draw_ui_win(stdscr, ui, game):
    stdscr.addstr(0, 0, "Congratulations, you win!")
    stdscr.addstr(1, 0, "Press q to exit, anything else to restart.")

def draw_ui_lose(stdscr, ui, game):
    stdscr.addstr(0, 0, "Sorry, better luck next time.")
    stdscr.addstr(1, 0, "Press q to exit, anything else to go.")

draw_ui_map =  {
                UIKind.start : draw_ui_start,
                UIKind.win : draw_ui_win,
                UIKind.lose : draw_ui_lose,
                UIKind.play : draw_ui_play,
            }

def draw_game(stdscr, game):
    stdscr.clear()
    for ui in game.uis:
        draw_ui_map[ui.kind](stdscr, ui, game)
    stdscr.refresh()


def get_viewport_coords(game, center_coords, vcols, vrows):

    center_x, center_y = center_coords

    map_rows = len(game.world.tiles)
    map_cols = len(game.world.tiles[0])

    start_x = center_x - math.ceil(vcols/2)
    start_x = max(0, start_x)
    start_y = center_y - math.ceil(vrows/2)
    start_y = max(0, start_y)

    end_x = start_x + vcols
    end_x = min(end_x, map_cols)

    end_y = start_y + vrows
    end_y = min(end_y, map_rows)

    start_x = end_x - vcols
    start_y = end_y - vrows

    return (start_x, start_y, end_x, end_y)


def draw_player(stdscr, start_coords, player):
    start_x, start_y = start_coords
    player_x, player_y = player.location
    x = player_x - start_x
    y = player_y - start_y + 1
    stdscr.addstr(y, x, "@", color.red)
    stdscr.move(y, x)


def draw_world(stdscr, vrows, vcols, start_x, start_y, end_x, end_y, tiles):
    for vrow_idx, y in zip(range(1, vrows+1), range(start_y, end_y)):
        row_glyphs = []
        for vcol_idx, x in zip(range(vcols), range(start_x, end_x)):
            row_glyphs.append(tiles[y][x].glyph)
        stdscr.addstr(vrow_idx, 0, "".join(row_glyphs))
