
from entities.aspects.receiver import send_message
from entities.core import add_entity
from entities.lichen import make_lichen
from entities.player import make_player
from world import World


class TestReceiver():

    def test_receive_message(self):
        lichen = make_lichen((1, 1))
        player = make_player((1, 2))

        w = World("world")
        add_entity(w, lichen.id, lichen)
        add_entity(w, "player", player)

        assert len(player.messages) == 0
        send_message(player, "The Lichen grows at {coord}.", {"coord":"(1, 1)"}, w)
        assert len(player.messages) == 1
