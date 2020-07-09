
from entities.core import add_entity
from entities.lichen import make_lichen, should_grow
from world import World

import color


class TestLichen():

    def test_make_lichen(self):
        lichen = make_lichen((1, 1))
        assert lichen.id is not None
        assert lichen.glyph == "F"
        assert lichen.location == (1, 1)
        assert lichen.color == color.red
        assert lichen.hp == 1

    def test_take_damage(self):
        lichen = make_lichen((1, 1))
        assert lichen.hp == 1
        w = World("main")
        w = add_entity(w, lichen.id, lichen)
        lichen.take_damage(1, w)
        assert lichen.hp == 0
        assert len(w.entities) == 0

    def test_should_grow(self):
        results = {should_grow() for _ in range(400)}
        assert results == {True, False}
