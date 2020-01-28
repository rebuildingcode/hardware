
from shapely.geometry import Polygon

from ..point import Point


class Opening(Polygon):
    """
    Openings are rectangular only.
    """
    def __init__(self, width, height):

        self.width = width
        self.height = height

        points = [
            Point(0, 0), Point(0, height), Point(width, height), Point(width, 0)
        ]

        super().__init__(shell=[(pt.x, pt.y) for pt in points])

    def plot(self):
        """
        - [ ] plot plan view
        - [ ] plot elevation view
        """
        pass  # pragma: no cover