import random

from ..point import Point
from ..space import Space
from ..wall.door import Door, DoorInstalled
from .utils import random_rectangle


# TODO Add rules for minimum area
MIN_AREA = 70

MIN_WIDTH = 7
MAX_WIDTH = 15

class Room(Space):
    """Rooms are Spaces with walls and at least one door.

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
        self.door = None

        super().__init__(**kwargs)

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

    def add_door(self, door=None, corner=None, offset=0.5):
        """Add a door to the room"""
        if not corner:
            # choose bottom-left corner
            corner = self.points[0]
            hinge_coords = (corner.x + offset, corner.y)
            hinge_point = Point(*hinge_coords)
            wall_direction = 'X'

            # TODO: implement random door location
            # choose a random corner
            # rand_idx = random.randint(0, 3)
            # corner = self.points[rand_idx]
            # rand_direction =
            # hinge_point =

        if not door:
            door = Door()  # get default Door

        self.door = DoorInstalled(hinge_point=hinge_point, wall_direction=wall_direction,
                                  door=door)
