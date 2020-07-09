
import logging

from entities.aspects.destructible import is_destructible


class Attacker():

    def attack(self, target, world):
        #logging.debug(f"{self} attacking {target}")
        if is_destructible(target):
            dmg = 1
            target.take_damage(dmg, world)
        #else:
        #    logging.debug(f"{target} is not destructible")

