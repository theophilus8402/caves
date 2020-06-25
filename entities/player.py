
import color

from coords import destination_coords
from entities.aspects.attacker import Attacker
from entities.aspects.destructible import is_destructible
from entities.aspects.digger import Digger
from entities.aspects.mobile import Mobile
from entities.core import Entity, get_entity
from tile import TileKind, get_tile, set_tile, floor
from world import get_entity_at


class Player(Entity, Mobile, Digger, Attacker):

    def __init__(self, id, glyph, location, entity_color):
        self.id = id
        self.glyph = glyph
        self.location = location
        self.color = entity_color

    def tick(self, world):
        return world

    def dig(self, world, dest):
        if self.can_dig(world, dest):
            world.tiles = set_tile(world.tiles, dest, floor)
        return world

    def can_dig(self, world, dest):
        return check_tile(world, dest, TileKind.wall)

    def attack(self, world, target):
        if is_destructible(target):
            dmg = 1
            target.take_damage(world, dmg)


def make_player(location):
    return Player("player", "@", location, color.red)


def check_tile(world, dest, tile_kind):
    # check that the tile at the destination passes the given predicate
    return get_tile(world.tiles, dest).kind == tile_kind


def move_player(world, direction):
    player = get_entity(world, "player")
    dest = destination_coords(player.location, direction)
    target = get_entity_at(world, dest)

    if target:
        player.attack(world, target)
    elif player.can_move(world, dest):
        world = player.move(world, dest)
    elif player.can_dig(world, dest):
        world = player.dig(world, dest)
    return world
