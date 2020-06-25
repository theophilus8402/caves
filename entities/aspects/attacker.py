
import abc

class Attacker(abc.ABC):

    @abc.abstractmethod
    def attack(self, world, target):
        # attack the target
        pass
