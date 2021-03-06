
import curses
import logging
import math

import color

from entities.core import get_entity
from entities.lichen import Lichen
from ui.core import UIKind


screen_size = (80, 24)


def draw_hud(stdscr, game, start_x, start_y):
    screen_width, screen_height = screen_size
    hud_row = screen_height - 1
    player = get_entity(game.world, "player")
    hp, max_hp = player.hp, player.max_hp
    x, y = player.location
    num_lichen = len([ent for ent in game.world.entities.values()
                        if isinstance(ent, Lichen)])
    hud_line = f"HP: {hp}/{max_hp} Loc: [{x}-{y}] start: [{start_x}-{start_y}], #: {num_lichen}, Ticks: {game.world.ticks}"
    stdscr.addstr(hud_row, 0, hud_line)


def draw_ui_start(stdscr, ui, game):
    stdscr.addstr(0, 0, "Welcome to the Caves!")
    stdscr.addstr(1, 0, "Press e to win, anything else to lose.")

def draw_ui_play(stdscr, ui, game):
    stdscr.addstr(0, 0, f"Press e to win, s to smooth, anything else to lose.")

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
    for entity in game.world.entities.values():
        x, y = entity.location
        if ((start_x <= x) and (x <= end_x - 1) and
            (start_y <= y) and (y <= end_y - 1)):
            try:
                draw_entity(stdscr, (start_x, start_y), entity)
            except curses.error:
                logging.critical(f"({start_x}, {start_y}) => ({end_x}, {end_y}), {entity.location}, {entity.glyph}, {entity.color}, {entity.id}")
            except TypeError:
                logging.critical(f"({start_x}, {start_y}) => ({end_x}, {end_y}), {entity.location}, {entity.glyph}, {entity.color}, {entity.id}")
    highlight_player(stdscr, (start_x, start_y), player)

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


def draw_entity(stdscr, start_coords, entity):
    start_x, start_y = start_coords
    entity_x, entity_y = entity.location
    x = entity_x - start_x
    y = entity_y - start_y + 1
    stdscr.addstr(y, x, entity.glyph, entity.color)


def highlight_player(stdscr, start_coords, entity):
    start_x, start_y = start_coords
    entity_x, entity_y = entity.location
    x = entity_x - start_x
    y = entity_y - start_y + 1
    stdscr.move(y, x)


def draw_world(stdscr, vrows, vcols, start_x, start_y, end_x, end_y, tiles):
    for vrow_idx, y in zip(range(1, vrows+1), range(start_y, end_y)):
        row_glyphs = []
        for vcol_idx, x in zip(range(vcols), range(start_x, end_x)):
            row_glyphs.append(tiles[y][x].glyph)
        stdscr.addstr(vrow_idx, 0, "".join(row_glyphs))
