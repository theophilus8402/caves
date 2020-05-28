
import random

from enum import Enum, auto

class TileKind(Enum):
    floor = auto()
    wall = auto()
    bound = auto()


class Tile():

    def __init__(self, kind, glyph, color):
        self.kind = kind
        self.glyph = glyph
        self.color = color

    def __repr__(self):
        return f"<{self.kind.name} '{self.glyph}'>"


floor = Tile(TileKind.floor, ".", "white")
wall = Tile(TileKind.wall, "#", "white")
bound = Tile(TileKind.bound, "X", "black")


def get_tile(tiles, coords):
    x, y = coords
    try:
        return tiles[y][x]
    except IndexError:
        return bound


def set_tile(tiles, coords, new_tile):
    x, y = coords
    tiles[y][x] = new_tile
    return tiles


def random_tiles(width, height):
    tiles = []
    tile_choices = [floor, wall]
    for i in range(height):
        tiles.append([random.choice(tile_choices) for i in range(width)])
    return tiles


def get_block_coords(coords):
    x, y = coords
    return [(x+dx, y+dy) for dy in [-1, 0, 1]
                            for dx in [-1, 0, 1]]


def get_block(tiles, block_coords):
    block = [get_tile(tiles, (x, y)) for (x, y) in block_coords]
    return block


def random_coordinate(tiles):
    y = random.choice(range(len(tiles)))
    x = random.choice(range(len(tiles[y])))
    return (x, y)
