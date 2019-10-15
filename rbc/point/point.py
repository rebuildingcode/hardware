from math import sqrt
from collections import namedtuple

TempPoint = namedtuple('TempPoint', ['x', 'y', 'z'])

class Point():
    def __init__(self, x, y, z):
        """"""
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def distance_from(self, other_point):
        """Calculates the distance from this point to other_point"""
        dist = sqrt(
            (other_point.x - self.x) ** 2 
            + (other_point.y - self.y) ** 2
            + (other_point.z - self.z) ** 2
        )

        return dist

    @classmethod
    def relative_to(cls, origin_point, offset):
        """"""
        offset = cls.temp_point(*offset)
        if offset:
            x = origin_point.x + offset.x
            y = origin_point.y + offset.y
            z = origin_point.z + offset.z
            return cls(x, y, z)
        
    def move(self, *distance):
        """"""
        distance = self.temp_point(*distance)
        if distance:
            self.x += distance[0]
            self.y += distance[1]
            self.z += distance[2]

    @staticmethod
    def temp_point(*args):
        """"""
        if len(args) == 2:
            return TempPoint(args[0], args[1], 0)
        elif len(args) == 3:
            return TempPoint(args[0], args[1], args[2])
        else:
            raise ValueError(
                f"Attempted to create temporary point with {len(args)} arguments. "
                "Temporary points require 2 or 3 arguments."
            )