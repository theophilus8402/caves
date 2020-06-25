
from entities.aspects.destructible import is_destructible
from entities.core import add_entity, get_entity
from entities.lichen import make_lichen
from entities.player import make_player
from world import World

class TestPlayer():

    def test_attack(self):
        lichen = make_lichen((1, 1))
        player = make_player((1, 2))
        w = World("main")

        add_entity(w, lichen.id, lichen)
        add_entity(w, "player", player)

        player.attack(w, lichen)

        assert lichen.hp == 0
        assert get_entity(w, lichen.id) == None
