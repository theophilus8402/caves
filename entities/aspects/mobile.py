
from entities.core import get_entity
from world import is_empty


class Mobile():

    def move(self, dest, world):
        # move this entity to a new location
        if self.can_move(dest, world):
            self.location = dest
        return world

    def can_move(self, dest, world):
        # return whether the entity can move to the new location
        return is_empty(world, dest)
