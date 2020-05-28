
from entities.core import get_entity, add_entity
from entities.player import make_player, move_player
from world import smooth_world, World, find_empty_tile
from ui.core import UIKind, UI


def move(location, delta):
    x, y = location
    dx, dy = delta
    return (x + dx, y + dy)


def process_input_start(game, user_input):
    game.world = World(game.world.name)
    empty_location = find_empty_tile(game.world)
    add_entity(game.world, "player", make_player(empty_location))
    game.uis = [UI(UIKind.play)]


def process_input_play(game, user_input):

    if user_input == "e":
        game.uis.append(UI(UIKind.win))
    elif user_input == "s":
        game.world.tiles = smooth_world(game.world.tiles)
        game.uis = [UI(UIKind.play)]

    elif user_input == "h":
        game.world = move_player(game.world, "w")
        game.uis = [UI(UIKind.play)]
    elif user_input == "j":
        game.world = move_player(game.world, "s")
        game.uis = [UI(UIKind.play)]
    elif user_input == "k":
        game.world = move_player(game.world, "n")
        game.uis = [UI(UIKind.play)]
    elif user_input == "l":
        game.world = move_player(game.world, "e")
        game.uis = [UI(UIKind.play)]
    elif user_input == "y":
        game.world = move_player(game.world, "nw")
        game.uis = [UI(UIKind.play)]
    elif user_input == "u":
        game.world = move_player(game.world, "ne")
        game.uis = [UI(UIKind.play)]
    elif user_input == "b":
        game.world = move_player(game.world, "sw")
        game.uis = [UI(UIKind.play)]
    elif user_input == "n":
        game.world = move_player(game.world, "se")
        game.uis = [UI(UIKind.play)]

    else:
        game.uis.append(UI(UIKind.lose))


def process_input_win(game, user_input):
    if user_input == "q":
        game.uis.clear()
    else:
        game.uis.append(UI(UIKind.start))


def process_input_lose(game, user_input):
    if user_input == "q":
        game.uis.clear()
    else:
        game.uis.append(UI(UIKind.start))


process_input_map = {
                        UIKind.start : process_input_start,
                        UIKind.play : process_input_play,
                        UIKind.win : process_input_win,
                        UIKind.lose : process_input_lose,
                    }


def process_input(game, user_input):
    ui = game.uis.pop()
    process_input_map[ui.kind](game, user_input)


def get_input(stdscr, game):
    k = stdscr.getkey()
    game.input.append(k)
