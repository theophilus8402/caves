
import abc


class Entity(abc.ABC):

    @abc.abstractmethod
    def tick(self, world):
        # Update the world to handle the passing of a tick for this entity
        pass


def _id_generator():
    next_id = 1
    while True:
        yield next_id
        next_id += 1
id_generator = _id_generator()


def get_id():
    return next(id_generator)


def add_entity(world, entity_id, entity):
    world.entities[entity_id] = entity


def get_entity(world, entity_id):
    return world.entities[entity_id]
