
import color

from coords import destination_coords
from entities.aspects.mobile import Mobile
from entities.aspects.digger import Digger
from entities.core import Entity, get_entity
from tile import TileKind, get_tile, set_tile, floor


class Player(Entity, Mobile, Digger):

    def __init__(self, id, glyph, location, entity_color):
        self.id = id
        self.glyph = glyph
        self.location = location
        self.color = entity_color

    def tick(self, world):
        return world

    def move(self, world, dest):
        if self.can_move(world, dest):
            player = get_entity(world, "player")
            player.location = dest
        return world

    def can_move(self, world, dest):
        return check_tile(world, dest, TileKind.floor)

    def dig(self, world, dest):
        if self.can_dig(world, dest):
            world.tiles = set_tile(world.tiles, dest, floor)
        return world

    def can_dig(self, world, dest):
        return check_tile(world, dest, TileKind.wall)


def make_player(location):
    return Player("player", "@", location, color.red)


def check_tile(world, dest, tile_kind):
    # check that the tile at the destination passes the given predicate
    return get_tile(world.tiles, dest).kind == tile_kind


def move_player(world, direction):
    player = get_entity(world, "player")
    dest = destination_coords(player.location, direction)
    if player.can_move(world, dest):
        world = player.move(world, dest)
    elif player.can_dig(world, dest):
        world = player.dig(world, dest)
    return world
