import logging

from shapely.geometry import Polygon

from ...point import Point

log = logging.getLogger()


class Section(Polygon):
    """

    If defining a polygon, some handling should be done to move the centroid
    of the polygon to (0, 0)

    """
    def __init__(self, points=None, rect_dim=None, radius=None):
        if rect_dim:
            if len(rect_dim) != 2:
                raise Exception
            x, y = rect_dim
            pt_list = [
                (-x/2, -y/2),
                (-x/2, y/2),
                (x/2, y/2),
                (x/2, -y/2),
            ]
        elif radius:
            if not isinstance(radius, int) and not isinstance(radius, float):
                raise Exception

            circle_center = Point(0, 0)
            circle_poly = circle_center.buffer(radius)
            pt_list = circle_poly.exterior.coords

        elif points:
            pt_list = [(pt.x, pt.y) for pt in points]
        else:
            raise Exception

        super().__init__(shell=pt_list)

        if self.centroid_coords != (0.0, 0.0):
            self.center_sxn_at_origin()

    def __repr__(self):
        return f'Section: AREA={self.area}, BOUNDS={self.bounds}'

    def __str__(self):
        return self.__repr__()

    @property
    def centroid_coords(self):
        """Convenient way to quickly retrive the centroid coordinates"""
        return list(self.centroid.coords)[0]

    @property
    def exterior_coords(self):
        """Convenient way to retrieve a list of the exterior coordinates"""
        # the last coord is excluded because it is the same as the first
        return list(self.exterior.coords)[:-1]

    def center_sxn_at_origin(self):
        c_x, c_y = self.centroid_coords
        centered_pt_list = [(x - c_x, y - c_y)
                            for x, y in self.exterior_coords]
        super().__init__(shell=centered_pt_list)

    def plot(self):  # pragma: no cover
        pass