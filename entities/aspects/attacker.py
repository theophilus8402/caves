
import logging
import random

from entities.aspects.destructible import is_destructible
from entities.aspects.receiver import send_message

class Attacker():

    def attack(self, target, world):
        if is_destructible(target):
            dmg = get_damage(self, target, world)
            target.take_damage(dmg, world)
            send_message(self, "You strike the {target} for {dmg} damage!",
                            {"target": target.name, "dmg": dmg}, world)
            send_message(target, "The {attacker} strikes you for {dmg} damage!",
                            {"attacker": self.name, "dmg": dmg}, world)

    @property
    def attack_value(self):
        return getattr(self, "_attack_value", 1)


def get_damage(attacker, target, world):
    attack = attacker.attack_value
    defense = target.defense_value
    max_damage = max(1, attack - defense)
    min_damage = 1
    damage = random.randint(min_damage, max_damage)
    return damage
