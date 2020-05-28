
import collections

import tile

class World():

    def __init__(self, name, world_size=(160, 160), tiles=[]):
        self.name = name
        self.world_width, self.world_height = world_size
        self.entities = {}

        if tiles:
            self.tiles = tiles
        else:
            self.tiles = tile.random_tiles(self.world_width, self.world_height)


def smooth_world(tiles):
    smoothed_tiles = [smooth_row(tiles, row_idx)
                        for row_idx in range(len(tiles))]
    return smoothed_tiles


def smooth_row(tiles, y):
    smoothed_row = []
    for x in range(len(tiles[y])):
        block_coords = tile.get_block_coords((x, y))
        smoothed_tile = get_smoothed_tile(tile.get_block(tiles, block_coords))
        smoothed_row.append(smoothed_tile)
    return smoothed_row


def get_smoothed_tile(block):
    floor_threshold = 5
    c = collections.Counter(block)
    if c[tile.floor] >= floor_threshold:
        return tile.floor
    else:
        return tile.wall


def find_empty_tile(world):
    while True:
        coords = tile.random_coordinate(world.tiles)
        if tile.get_tile(world.tiles, coords) == tile.floor:
            return coords
