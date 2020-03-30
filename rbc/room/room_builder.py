from .room import Room
from ..point import Point

class RoomBuilder:
    """"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = None
        self.y = None
        self.points = None
        self.name = None
        self.room_type = None

    def room(self):
        room = self.create_room()
        self.reset()
        return room

    def set_dimensions(self, x, y):
        self.x = x
        self.y = y

    def set_name(self, name):
        self.name = name

    def set_room_type(self, room_type):
        self.room_type = room_type

    def generate_points(self, x, y):
        points = [
            Point(0, 0, 0),
            Point(0, y, 0),
            Point(x, y, 0),
            Point(x, 0, 0),
        ]

        return points

    def create_room(self):
        if self.x and self.y:
            self.points = self.generate_points(self.x, self.y)

        optional_param_names = [
            'name',
            'room_type',
        ]
        optional_params = {}

        for param in optional_param_names:
            optional_params[param] = getattr(self, param)

        print(optional_params)

        return Room(points=self.points, **optional_params)
