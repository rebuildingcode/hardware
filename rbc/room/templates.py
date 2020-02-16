from .room import Room
from ..point import Point


# TODO: Add fixtures such as toilet, sink, and shower
SMALL_BATHROOM = Room(
    points=[Point(0, 0), Point(0, 5), Point(9, 5), Point(9, 0)],
    name='bathroom',
    room_type='bathroom')
