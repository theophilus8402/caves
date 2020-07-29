
from coords import get_entities_around, radial_distance
from entities.core import add_entity, get_entity
from entities.lichen import make_lichen
from entities.player import make_player, move_player
from world import World


class TestCoords():

    def test_radial_distance(self):
        assert radial_distance((0, 0), (0, 0)) == 0
        assert radial_distance((2, 1), (0, 0)) == 2
        assert radial_distance((2, 1), (1, 1)) == 1

    def test_get_entities_around(self):
        lichen = make_lichen((1, 1))
        player = make_player((1, 2))
        w = World("main")

        w = add_entity(w, lichen.id, lichen)
        w = add_entity(w, "player", player)

        assert len(get_entities_around(w, player.location, radius=3)) == 2
        assert len(get_entities_around(w, (-5, -5), radius=3)) == 0
        assert len(get_entities_around(w, (0, 0), radius=1)) == 1
