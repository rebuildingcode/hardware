import random

from ..point import Point
from ..space import Space
from .utils import random_rectangle


# TODO Add rules for minimum area
MIN_AREA = 70

MIN_WIDTH = 7
MAX_WIDTH = 15

class Room(Space):
    """Rooms are 2-dimensional polygons.

    Parameters
    ----------
    room_type: string
        Type of room (e.g. bedroom, bathroom, kitchen, living room, etc.)

    TODO Add rules to Room class for minimum area
    min_area : float
        This value will be used to determine the minimum random value when
        generating rooms
    """
    def __init__(self, room_type=None, **kwargs):
        self.room_type = room_type

        super().__init__(**kwargs)

    # TODO: Add a method to create doors
    # prerequisite: Door class object
    # def create_door(self, corner, offset=1):
    #     """
    #     """
    #     pass

    @classmethod
    def random(cls, room_type="random", bounds=None, min_area=MIN_AREA,
               min_width=MIN_WIDTH):
        """Creates a random room (4-sided) that meets the minimum requirements
        """

        if bounds is None:
            min_x = min_width
            min_y = min_width
            max_x = MAX_WIDTH
            max_y = MAX_WIDTH
        else:
            max_x = bounds[2] - bounds[0]
            max_y = bounds[3] - bounds[1]
            min_x = min_width
            min_y = min_width

        pts = random_rectangle(max_x=max_x, max_y=max_y,
                               min_x=min_x, min_y=min_y,
                               min_area=min_area)

        if bounds:
            # set pts in bounds
            pts_in_bounds = []
            for pt in pts:
                pts_in_bounds.append(Point(pt.x + bounds[0], pt.y + bounds[1]))

            pts = pts_in_bounds

        return cls(points=pts, room_type=room_type)
