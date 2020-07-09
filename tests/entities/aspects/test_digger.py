
from entities.player import make_player
from tile import get_tile, set_tile, floor, wall
from world import World


class TestDigger():

    def test_can_dig(self):
        player = make_player((1, 1))

        w = World("new world")
        w.tiles = set_tile(w.tiles, (1, 1), floor)
        w.tiles = set_tile(w.tiles, (1, 2), wall)

        assert player.can_dig((1, 1), w) == False
        assert player.can_dig((1, 2), w) == True

    def test_dig(self):
        player = make_player((1, 1))

        w = World("new world")
        w.tiles = set_tile(w.tiles, (1, 1), floor)
        w.tiles = set_tile(w.tiles, (1, 2), wall)

        assert get_tile(w.tiles, (1, 2)) == wall
        player.dig((1, 2), w)
        assert get_tile(w.tiles, (1, 2)) == floor
