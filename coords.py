
def offset_coords(coords, delta):
    # offset the coords by the given amt, returning the result
    x, y = coords
    dx, dy = delta
    return (x + dx, y + dy)


def dir_to_offset(direction):
    # convert a direction to the offset for moving 1 in that direction
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
    return dir_map[direction]


def destination_coords(origin, direction):
    return offset_coords(origin, dir_to_offset(direction))
