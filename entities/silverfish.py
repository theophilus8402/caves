
from random import choice

import color

from coords import neighbors
from entities.aspects.mobile import Mobile
from entities.aspects.destructible import Destructible
from entities.core import Entity, get_id
from world import find_empty_neighbor, get_entity_at


class Silverfish(Entity, Mobile, Destructible):

    def __init__(self, id, glyph, location, entity_color, hp):
        self.id = id
        self.glyph = glyph
        self.location = location
        self.color = entity_color
        self.hp = hp

    def can_move(self, world, dest):
        return not get_entity_at(world, dest)

    def tick(self, world):
        dest = choice(tuple(neighbors(self.location)))
        if get_entity_at(world, dest):
            return world
        else:
            return self.move(world, dest)


def make_silverfish(location):
    return Silverfish(get_id(), "~", location, color.white, 1)
