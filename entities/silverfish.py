
from random import choice

import color

from coords import neighbors
from entities.aspects.mobile import Mobile
from entities.aspects.destructible import Destructible
from entities.core import Entity, get_id
from world import find_empty_neighbor, get_entity_at


class Silverfish(Entity, Mobile, Destructible):

    def __init__(self, id, glyph, location, entity_color, hp, max_hp):
        self.id = id
        self.glyph = glyph
        self.location = location
        self.color = entity_color
        self.hp = hp
        self.max_hp = max_hp

    def can_move(self, dest, world):
        return not get_entity_at(world, dest)

    def tick(self, world):
        dest = choice(tuple(neighbors(self.location)))
        if get_entity_at(world, dest):
            return world
        else:
            return self.move(dest, world)


def make_silverfish(location):
    return Silverfish(id=get_id(),
                      glyph="~",
                      location=location,
                      entity_color=color.white,
                      hp=15,
                      max_hp=15)
