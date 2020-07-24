
#from world import get_entities_around


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
