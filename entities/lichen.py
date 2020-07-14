
import random

import color

from entities.aspects.destructible import Destructible
from entities.core import Entity, get_id, remove_entity, add_entity
from world import find_empty_neighbor

class Lichen(Entity, Destructible):

    def __init__(self, id, glyph, location, entity_color, hp, max_hp):
        self.id = id
        self.glyph = glyph
        self.location = location
        self.color = entity_color
        self.hp = hp
        self.max_hp = max_hp

    def tick(self, world):
        if should_grow():
            return grow(self, world)
        else:
            return world


def should_grow():
    return random.random() < 0.01


def grow(lichen, world):
    dest = find_empty_neighbor(world, lichen.location)
    if dest:
        new_lichen = make_lichen(dest)
        world = add_entity(world, new_lichen.id, new_lichen)
    return world


def make_lichen(location):
    return Lichen(id=get_id(),
                  glyph="F",
                  location=location,
                  entity_color=color.red,
                  hp=6,
                  max_hp=6)
