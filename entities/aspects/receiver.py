
from coords import get_entities_around


class Receiver():

    @property
    def messages(self):
        try:
            return self._messages
        except AttributeError:
            self._messages = []
            return self._messages

    def receive_message(self, message, world):
        self.messages.append(message)

def send_message(entity, message, args, world):
    if issubclass(type(entity), Receiver):
        entity.receive_message(message.format(**args), world)


def send_message_nearby(coords, message, world):
    entities = get_entities_around(world, coords, radius=7)
    for entity in entities:
        send_message(entity, message, {}, world)
