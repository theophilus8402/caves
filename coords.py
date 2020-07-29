
def offset_coords(coords, delta):
    # offset the coords by the given amt, returning the result
    x, y = coords
    dx, dy = delta
    return (x + dx, y + dy)


dir_map = {
    "n": (0, -1),
    "e": (1, 0),
    "s": (0, 1),
    "w": (-1, 0),
    "ne": (1, -1),
    "se": (1, 1),
    "sw": (-1, 1),
    "nw": (-1, -1),
}
def dir_to_offset(direction):
    # convert a direction to the offset for moving 1 in that direction
    return dir_map[direction]


def destination_coords(origin, direction):
    return offset_coords(origin, dir_to_offset(direction))


def neighbors(origin):
    for delta in dir_map.values():
        yield offset_coords(origin, delta)


def get_entities_around(world, coords, radius=1):
    return [ent for ent in world.entities.values()
                if radial_distance(coords, ent.location) <= radius]


def radial_distance(coords1, coords2):
    """
    The radial distance should look like this:
    3333333
    3222223
    3211123
    3210123
    3211123
    3222223
    3333333
    """
    x1, y1 = coords1
    x2, y2 = coords2
    return max(abs(x1 - x2), abs(y1 - y2))
