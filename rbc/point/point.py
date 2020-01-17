import logging
from math import sqrt
from collections import namedtuple

from shapely.geometry import Point as sp

log = logging.getLogger()

TempPoint = namedtuple('TempPoint', ['x', 'y', 'z'])


class Point(sp):
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
    def __repr__(self):
        if self._ndim == 3:
            return f'Point({self.x}, {self.y}, {self.z})'
        else:
            return f'Point({self.x}, {self.y})'

    def __str__(self):
        return self.__repr__()

    def distance(self, other_point):
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
        >>> p2.distance(p1)
        5

        """
        if not isinstance(other_point, self.__class__):
            other_point = sp(*other_point)

        dist = super().distance(other_point)

        if self.has_z or other_point.has_z:
            if not self.has_z:
                z1 = 0
            else:
                z1 = self.z

            if not other_point.has_z:
                z2 = 0
            else:
                z2 = other_point.z

            dist = sqrt(
                dist ** 2 +
                (z2 - z1) ** 2
            )

        return dist

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

    def nearest(self, points):
        """Returns the nearest point to self from a list of points

        Parameters
        ----------
        points : list of Points

        Returns
        -------
        nearest_pt : Point

        """
        # initialize the values for comparison
        thresh = self.distance(points[0])
        nearest_pt = points.pop(0)

        for pt in points:
            d = self.distance(pt)
            if d < thresh:
                nearest_pt = pt

        return nearest_pt
