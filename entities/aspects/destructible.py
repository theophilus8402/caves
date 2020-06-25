
import abc

class Destructible(abc.ABC):

    @abc.abstractmethod
    def take_damage(self, world, damage):
        # take the given amount of damage and update the world appropriately
        pass

def is_destructible(obj):
    return issubclass(type(obj), Destructible)
