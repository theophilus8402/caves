
import color

from coords import destination_coords
from entities.aspects.attacker import Attacker
from entities.aspects.digger import Digger
from entities.aspects.mobile import Mobile
from entities.core import Entity, get_entity
from world import get_entity_at


class Player(Entity, Mobile, Digger, Attacker):

    def __init__(self, id, glyph, location, entity_color, hp, max_hp, attack_value):
        self.id = id
        self.glyph = glyph
        self.location = location
        self.color = entity_color
        self.hp = hp
        self.max_hp = max_hp
        self._attack_value = attack_value

    def tick(self, world):
        return world


def make_player(location):
    return Player(id="player",
                  glyph="@",
                  location=location,
                  entity_color=color.red,
                  hp=40,
                  max_hp=40,
                  attack_value=10)


def move_player(direction, world):
    player = get_entity(world, "player")
    dest = destination_coords(player.location, direction)
    target = get_entity_at(world, dest)

    if target:
        player.attack(target, world)
    elif player.can_move(dest, world):
        world = player.move(dest, world)
    elif player.can_dig(dest, world):
        world = player.dig(dest, world)
    return world
