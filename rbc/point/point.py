import logging
from math import sqrt
from collections import namedtuple

log = logging.getLogger()

TempPoint = namedtuple('TempPoint', ['x', 'y', 'z'])


class Point():
    """Points are coordinates in 3-dimensional space.

    Parameters
    ----------
    x : float
        Coordinate associated with east/west direction
    y : float
        Coordinate associated with north/south direction
    z : float
        Coordinate associated with elevation

    """
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """Outputs ``Point(x, y, z)`` when inspecting the object"""
        return f"Point({self.x}, {self.y}, {self.z})"

    def distance_from(self, other_point):
        """Calculates the distance from this point to ``other_point``.

        Parameters
        ----------
        other_point : ``Point`` object or tuple (x, y, z)

        Returns
        -------
        dist : float
            distance between this point and ``other_point``

        Examples
        --------
        >>> p1 = Point(0, 0)
        >>> p2 = Point(3, 4)
        >>> p2.distance_from(p1)
        5

        """
        if not isinstance(other_point, self.__class__):
            other_point = self.temp_point(*other_point)

        dist = sqrt(
            (other_point.x - self.x) ** 2
            + (other_point.y - self.y) ** 2
            + (other_point.z - self.z) ** 2
        )

        return dist

    def move(self, *distance):
        """Move a point by ``distance``.

        Parameters
        ----------
        *distance : iterable of floats
            Two or three arguments are acceptable.

        Returns
        -------
        None

        Examples
        --------
        >>> p1 = Point(0, 0)
        >>> p1.move(2, 4)
        >>> p1
        Point(2, 4, 0)

        """
        distance = self.temp_point(*distance)
        if distance:
            self.x += distance[0]
            self.y += distance[1]
            self.z += distance[2]
            log.info(self.__repr__())

    @classmethod
    def relative_to(cls, origin_point, offset):
        """Creates a new point relative to an existing ``Point``.

        Parameters
        ----------
        origin_point : Point
            ``Point`` from which new ``Point`` will be created relative to
        offset : tuple (x, y) or (x, y, z)
            coordinates for new point, relative to ``origin_point``

        Returns
        -------
        Point object

        Examples
        --------
        >>> p1 = Point(1, 1)
        >>> p2 = Point.relative_to(p1, (4, 4))
        >>> p2
        Point(5, 5, 0)

        """
        offset = cls.temp_point(*offset)
        if offset:
            x = origin_point.x + offset.x
            y = origin_point.y + offset.y
            z = origin_point.z + offset.z
            return cls(x, y, z)

    @staticmethod
    def temp_point(*args):
        """Returns a namedtuple where keys x, y, and z

        Parameters
        ----------
        *args : iterable of floats
            If only two floats are given, return (x, y).
            If three floats are given, return (x, y, z).
            IF one or more than three floats are given, raise ValueError

        Returns
        -------
        TempPoint : (x: float, y: float, z: float)

        """

        if len(args) == 2:
            return TempPoint(args[0], args[1], 0)
        elif len(args) == 3:
            return TempPoint(args[0], args[1], args[2])
        else:
            raise ValueError(
                f"Attempted to create temporary point with {len(args)} arguments. "
                "Temporary points require 2 or 3 arguments."
            )
