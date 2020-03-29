from ...opening import Opening
from .mixins import SnapToWallMixin


class Door(Opening):
    """Base class for doors

    Parameters
    ----------
    thickness : float
        Thickness of the door (unit: inches)
    jamb_width : float
        Width of the framing in the wall that encases the door (unit: inches)
    unit_price : float
        Cost per door

    """
    def __init__(self, thickness=1.375, jamb_width=4.5625, unit_price=0,
                 width=32, height=80, **kwargs):  # Opening params
        self.thickness = thickness
        self.jamb_width = jamb_width
        self.unit_price = unit_price

        super().__init__(width, height)

    def plot(self):
        """
        TODO:
        - [ ] Plot plan view
        - [ ] Plot elevation view
        """
        pass  # pragma: no cover


class DoorInstalled(SnapToWallMixin, Door):
    """Class for doors that are added to a room or wall

    Parameters
    ----------
    hinge_point : Point
        Plan location (x, y) of the door hinge
    wall_direction : str
        direction from hinge to latch (one of [X, -X, Y, -Y])
    door : Door
        existing Door object

    """
    def __init__(self, hinge_point, wall_direction, door=None, **kwargs):
        self.hinge_point = hinge_point
        self.wall_start_point = hinge_point  # mixin assignment
        self.wall_direction = wall_direction

        if door:  # create instance with existing door params
            door_vars = vars(door)
            door_params = {
                # Opening params
                'width': door_vars.get('width'),
                'height': door_vars.get('height'),
                # Door params
                'thickness': door_vars.get('thickness'),
                'jamb_width': door_vars.get('jamb_width'),
                'unit_price': door_vars.get('unit_price'),
            }
        else:
            door_params = kwargs

        stw_params = {  # mixin params
            'wall_start_point': self.wall_start_point,
            'wall_direction': self.wall_direction
        }

        super().__init__(**door_params, **stw_params)

    @property
    def latch_point(self):
        """Same as wall_end_point property, opposite of hinge_point"""
        return self.wall_end_point

    @property
    def closed_xy(self):
        """Plan representation of door when closed"""

        return self.xy
