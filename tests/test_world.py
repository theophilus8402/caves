
from entities.core import get_id, add_entity

import entities.lichen
import tile
import world

class TestWorld():

    def test_get_entity_at(self):
        new_world = world.World("new world")

        coords = (1, 1)
        lichen = entities.lichen.make_lichen(coords)
        new_world = add_entity(new_world, lichen.id, lichen)
        assert world.get_entity_at(new_world, coords) == lichen

        other_lichen = entities.lichen.make_lichen((1, 2))
        new_world = add_entity(new_world, other_lichen.id, other_lichen)
        assert world.get_entity_at(new_world, (1, 2)) == other_lichen

        assert world.get_entity_at(new_world, (1, 3)) == None


    def test_is_empty(self):
        new_world = world.World("new world")
        
        # pass: floor and no entity
        new_world.tiles = tile.set_tile(new_world.tiles, (1, 1), tile.floor)
        assert world.is_empty(new_world, (1, 1)) == True
        
        # fail: wall and no entity
        new_world.tiles = tile.set_tile(new_world.tiles, (1, 2), tile.wall)
        assert world.is_empty(new_world, (1, 2)) == False

        # fail: floor and entity
        new_world.tiles = tile.set_tile(new_world.tiles, (1, 3), tile.floor)
        lichen = entities.lichen.make_lichen((1, 3))
        new_world = add_entity(new_world, lichen.id, lichen)
        assert world.is_empty(new_world, (1, 3)) == False

        # fail: wall and entity
        new_world.tiles = tile.set_tile(new_world.tiles, (1, 4), tile.wall)
        other_lichen = entities.lichen.make_lichen((1, 4))
        new_world = add_entity(new_world, other_lichen.id, other_lichen)
        assert world.is_empty(new_world, (1, 4)) == False
