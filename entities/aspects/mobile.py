
from entities.core import get_entity
from world import is_empty


class Mobile():

    def move(self, world, dest):
        # move this entity to a new location
        if self.can_move(world, dest):
            player = get_entity(world, "player")
            player.location = dest
        return world

    def can_move(self, world, dest):
        # return whether the entity can move to the new location
        return is_empty(world, dest)
