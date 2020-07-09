
from tile import TileKind, get_tile, set_tile, floor


class Digger():

    def dig(self, dest, world):
        if self.can_dig(dest, world):
            world.tiles = set_tile(world.tiles, dest, floor)
        return world

    def can_dig(self, dest, world):
        return check_tile(world, dest, TileKind.wall)


def check_tile(world, dest, tile_kind):
    # check that the tile at the destination passes the given predicate
    return get_tile(world.tiles, dest).kind == tile_kind
