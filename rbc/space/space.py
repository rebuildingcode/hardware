import random
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

from ..point import Point


class Space:
    """Space are 2-dimensional polygons.

    Parameters
    ----------
    points: Point
        List of ``Point`` objects

    name: string
        Human-readable name of space

    contents: Polygons or subclasses of Polygons
        List of

    """

    def __init__(self, points=None, name=None, contents=None):
        self.name = name
        self.contents = contents
        self.polygon = Polygon(shell=[(pt.x, pt.y) for pt in points])

        # plan is like contents but with location modified to fit in space
        self.plan = {}
        if self.contents:
            self.place_contents(self.contents)

    @property
    def area(self):
        return self.polygon.area

    def place_contents(self, contents):
        for content in contents:
            self.place_content(content)

    def place_content(self, content):
        b_x_min, b_y_min, b_x_max, b_y_max = self.polygon.bounds
        c_x_min, c_y_min, c_x_max, c_y_max = content.bounds
        x_min = b_x_min + c_x_min
        x_max = b_x_max - c_x_max
        y_min = b_y_min - c_y_min
        y_max = b_y_max - c_y_max

        rand_x = random.randint(x_min, x_max)
        rand_y = random.randint(y_min, y_max)

        new_points = [
            (x+rand_x, y+rand_y) for x, y in content.exterior.coords[:-1]
        ]

        k = content.name

        self.plan[k] = Polygon(shell=new_points)


    def plot(self, figsize=(12, 12)):
        """Plots a list of rooms"""
        fig, ax = plt.subplots(figsize=figsize)

        # plot boundary
        x, y = self.polygon.exterior.xy
        ax.plot(x, y)

        # plot contents
        for label, poly in self.plan.items():
            x, y = poly.exterior.xy
            ax.plot(x, y)
            ax.text(poly.centroid.x, poly.centroid.y, s=label,
                    horizontalalignment='center', verticalalignment='center')
        plt.axis('scaled')
        plt.show()
