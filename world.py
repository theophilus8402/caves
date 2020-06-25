
import collections
import random

import tile

from coords import neighbors

class World():

    def __init__(self, name, world_size=(160, 160), tiles=[]):
        self.ticks = 0
        self.name = name
        self.world_width, self.world_height = world_size
        self.entities = {}

        if tiles:
            self.tiles = tiles
        else:
            self.tiles = tile.random_tiles(self.world_width, self.world_height)


def smooth_world(tiles, num_smooths=3):
    for i in range(num_smooths):
        smoothed_tiles = [smooth_row(tiles, row_idx)
                            for row_idx in range(len(tiles))]
        tiles = smoothed_tiles
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


def get_entity_at(world, coords):
    for entity in world.entities.values():
        if entity.location == coords:
            return entity


def is_empty(world, coords):
    return (tile.get_tile(world.tiles, coords).kind == tile.TileKind.floor and
            not get_entity_at(world, coords))


def find_empty_neighbor(world, coords):
    empty_neighbors = [dest for dest in neighbors(coords)
                                if is_empty(world, dest)]
    if empty_neighbors:
        return random.choice(empty_neighbors)
    else:
        return None
