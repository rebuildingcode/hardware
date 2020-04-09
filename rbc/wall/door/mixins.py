from shapely.geometry import LineString

from ...point import Point


class SnapToWallMixin:
    """Mixin for objects attached to Wall"""

    @property
    def start_coord(self):
        return (self.wall_start_point.x, self.wall_start_point.y)

    @property
    def end_coord(self):
        if self.wall_direction == 'X':
            wall_end_coord = (
                self.start_coord[0] + self.width, self.start_coord[1])
        elif self.wall_direction == '-X':
            wall_end_coord = (
                self.start_coord[0] - self.width, self.start_coord[1])
        elif self.wall_direction == 'Y':
            wall_end_coord = (
                self.start_coord[0], self.start_coord[1] + self.width)
        elif self.wall_direction == '-Y':
            wall_end_coord = (
                self.start_coord[0], self.start_coord[1] - self.width)

        return wall_end_coord


    @property
    def wall_end_point(self):
        return Point(*self.end_coord)

    @property
    def xy(self):
        return LineString([self.start_coord, self.end_coord])
