
from entities.aspects.attacker import get_damage
from entities.core import add_entity
from entities.lichen import make_lichen
from entities.player import make_player
from world import World

class TestAttacker():

    def test_attack(self):
        lichen = make_lichen((1, 1))
        player = make_player((1, 2))

        w = World("world")
        add_entity(w, lichen.id, lichen)

        assert lichen.hp == lichen.max_hp
        player.attack(lichen, w)
        assert len(player.messages) == 1
        assert lichen.hp < lichen.max_hp

    def test_attack_value(self):
        player = make_player((1, 2))

        assert player.attack_value == 10
        player._attack_value = 3
        assert player.attack_value == 3

    def test_get_damage(self):
        lichen = make_lichen((1, 1))
        player = make_player((1, 2))

        w = World("world")
        add_entity(w, lichen.id, lichen)

        damage =  get_damage(player, lichen, w)
        assert damage <= player.attack_value
        assert damage >= 1
