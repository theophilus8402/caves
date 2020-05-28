
import abc

class Mobile(abc.ABC):

    @abc.abstractmethod
    def move(self, world, dest):
        # move this entity to a new location
        pass

    @abc.abstractmethod
    def can_move(self, world, dest):
        # return whether the entity can move to the new location
        pass
