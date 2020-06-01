
import color

from entities.core import Entity, get_id


class Lichen(Entity):

    def __init__(self, id, glyph, location, entity_color):
        self.id = id
        self.glyph = glyph
        self.location = location
        self.color = entity_color

    def tick(self, world):
        if self.should_grow():
            return world
        else:
            return world

    def should_grow(self):
        return True


def make_lichen(location):
    return Lichen(get_id(), "F", location, color.red)
