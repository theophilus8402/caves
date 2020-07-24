
from entities.aspects.destructible import is_destructible
from entities.core import add_entity, get_entity
from entities.lichen import make_lichen
from entities.player import make_player, move_player
from tile import get_tile, set_tile, floor, wall
from world import World

class TestPlayer():

    def test_attack(self):
        lichen = make_lichen((1, 1))
        player = make_player((1, 2))
        w = World("main")

        w = add_entity(w, lichen.id, lichen)
        w = add_entity(w, "player", player)

        player.attack(lichen, w)

        assert lichen.hp < lichen.max_hp
        if lichen.hp <= 0:
            assert get_entity(w, lichen.id) == None
        else:
            assert get_entity(w, lichen.id) == lichen

    def test_move_player(self):
        player = make_player((1, 1))
        lichen = make_lichen((1, 0))

        w = World("main")
        add_entity(w, lichen.id, lichen)
        add_entity(w, "player", player)

        w.tiles = set_tile(w.tiles, (1, 1), floor)
        w.tiles = set_tile(w.tiles, (1, 0), floor)
        w.tiles = set_tile(w.tiles, (1, 2), wall)
        w.tiles = set_tile(w.tiles, (2, 1), floor)

        # check to see if it attacks the lichen
        assert lichen.hp == lichen.max_hp
        move_player("n", w)
        assert lichen.hp < lichen.max_hp

        # check to see if it digs
        assert get_tile(w.tiles, (1, 2)) == wall
        move_player("s", w)
        assert get_tile(w.tiles, (1, 2)) == floor

        # check to see if it just moves
        assert player.location == (1, 1)
        move_player("s", w)
        assert player.location == (1, 2)
