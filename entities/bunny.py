
import color

from entities.aspects.mobile import Mobile
from entities.aspects.destructible import Destructible
from entities.core import Entity, get_id
from world import find_empty_neighbor


class Bunny(Entity, Mobile, Destructible):

    def __init__(self, id, name, glyph, location, entity_color, hp, max_hp):
        self.id = id
        self.name = name
        self.glyph = glyph
        self.location = location
        self.color = entity_color
        self.hp = hp
        self.max_hp = max_hp

    def tick(self, world):
        dest = find_empty_neighbor(world, self.location)
        world = self.move(dest, world)
        return world


def make_bunny(location):
    return Bunny(id=get_id(),
                 name="bunny",
                 glyph="v",
                 location=location,
                 entity_color=color.yellow,
                 hp=4,
                 max_hp=4)
