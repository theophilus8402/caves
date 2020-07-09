
import color

from entities.aspects.mobile import Mobile
from entities.aspects.destructible import Destructible
from entities.core import Entity, get_id
from world import find_empty_neighbor


class Bunny(Entity, Mobile, Destructible):

    def __init__(self, id, glyph, location, entity_color, hp):
        self.id = id
        self.glyph = glyph
        self.location = location
        self.color = entity_color
        self.hp = hp

    def tick(self, world):
        dest = find_empty_neighbor(world, self.location)
        world = self.move(world, dest)
        return world


def make_bunny(location):
    return Bunny(get_id(), "v", location, color.yellow, 1)
