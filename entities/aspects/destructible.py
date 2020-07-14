
from entities.core import remove_entity


class Destructible():

    def take_damage(self, damage, world):
        # take the given amount of damage and update the world appropriately
        self.hp = self.hp - damage
        if self.hp <= 0:
            remove_entity(world, self.id)

    @property
    def defense_value(self):
        return getattr(self, "_defense_value", 0)


def is_destructible(obj):
    return issubclass(type(obj), Destructible)
