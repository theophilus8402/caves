
import abc


class Digger(abc.ABC):

    @abc.abstractmethod
    def dig(self, world, target):
        # dig a location
        pass

    @abc.abstractmethod
    def can_dig(self, world, target):
        # return whether the entity can dig the new location
        pass
