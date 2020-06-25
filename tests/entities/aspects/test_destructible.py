
from entities.aspects.destructible import is_destructible
from entities.lichen import make_lichen
from entities.player import make_player

class TestDestructible():

    def test_is_destructible(self):
        lichen = make_lichen((1, 1))
        assert is_destructible(lichen) == True

        player = make_player((1, 2))
        assert is_destructible(player) == False
