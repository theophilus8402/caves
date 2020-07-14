
from entities.aspects.destructible import is_destructible
from entities.core import add_entity
from entities.bunny import make_bunny
from entities.lichen import make_lichen
from entities.player import make_player
from world import World

class TestDestructible():

    def test_is_destructible(self):
        lichen = make_lichen((1, 1))
        assert is_destructible(lichen) == True

        player = make_player((1, 2))
        assert is_destructible(player) == False

    def test_take_damage(self):
        lichen = make_lichen((1, 1))
        assert lichen.hp == lichen.max_hp

        w = World("main")
        w = add_entity(w, lichen.id, lichen)

        lichen.take_damage(1, w)
        assert lichen.hp < lichen.max_hp

    def test_defense_value(self):
        bunny = make_bunny((1, 2))

        assert bunny.defense_value == 0
        bunny._defense_value = 3
        assert bunny.defense_value == 3
