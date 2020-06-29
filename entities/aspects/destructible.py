
from entities.core import remove_entity


class Destructible():

    def take_damage(self, world, damage):
        # take the given amount of damage and update the world appropriately
        self.hp = self.hp - damage
        if self.hp <= 0:
            remove_entity(world, self.id)


def is_destructible(obj):
    return issubclass(type(obj), Destructible)
