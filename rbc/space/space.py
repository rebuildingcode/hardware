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
        self.max_retries = 15
        self.name = name
        self.contents = contents
        self.polygon = Polygon(shell=[(pt.x, pt.y) for pt in points])

        # plan is like contents but with location modified to fit in space
        self.plan = {}
        if self.contents:
            self.place_contents(self.contents)

    @property
    def area(self):
        """"""
        return self.polygon.area

    def place_contents(self, contents):
        """"""
        for content in contents:
            self.place_content(content)

    def place_content(self, content, retries=0):
        """Places content in a valid location"""
        if hasattr(content, 'name'):
            # get label for polygon-type objects with name attribute
            plan_label = content.name
        else:
            # otherwise default to using the area value as the label
            # this supports shapely's Polygon object
            plan_label = f"AREA: {content.area}"

        if isinstance(content, Space):
            content_poly = content.polygon
        else:
            content_poly = content

        # TODO: add capability for Space to remember failed attempts to reduce
        # amount of tries needed; possibly keep a list of failed locations
        retries = 0
        while retries < self.max_retries:
            if retries < self.max_retries // 2:
                # attempt to locate object at the corners with the first half
                # of tries
                potential_location = self.corner_locate(content_poly)
            else:
                # attempt to locate object at the edge with the rest of the
                # tries
                potential_location = self.edge_locate(content_poly)

            # create a polygon with the potential_location points to define
            # the content's place
            place = Polygon(shell=potential_location)

            if self.validate_place(place):
                # object's location is valid; add object to self.plan dict
                self.plan[plan_label] = place
                return
            else:  # location is not valid; retry
                print(f"Failed to place {plan_label}. Retrying...")
                retries += 1

        print(f"Reached max retries for {plan_label}. Skipping...")
        # max retries reached; continue finishing up Space construction
        # without content
        return

    def validate_place(self, place):
        """A place is valid if it is not in conflict with any other object in
        self.plan
        """
        if len(self.plan) > 0:
            checks = []
            for thing in self.plan.values():
                checks.append(not place.overlaps(thing) and
                              not place.within(thing) and
                              not thing.within(place))
            if all(checks) == True:
                return True
            else:  # retry place
                return False
        else:
            return True

    def corner_locate(self, content):
        """Return a set of points for a random corner"""
        b_x_min, b_y_min, b_x_max, b_y_max = self.polygon.bounds
        c_x_min, c_y_min, c_x_max, c_y_max = content.bounds
        x_min = b_x_min + c_x_min
        x_max = b_x_max - c_x_max
        y_min = b_y_min + c_y_min
        y_max = b_y_max - c_y_max

        rand_x = random.choice([x_min, x_max])
        rand_y = random.choice([y_min, y_max])

        loc_points = [
            (x+rand_x, y+rand_y) for x, y in content.exterior.coords[:-1]
        ]

        return loc_points


    def edge_locate(self, content):
        """Return a set of points for a random location at the edge"""
        b_x_min, b_y_min, b_x_max, b_y_max = self.polygon.bounds
        c_x_min, c_y_min, c_x_max, c_y_max = content.bounds
        x_min = b_x_min + c_x_min
        x_max = b_x_max - c_x_max
        y_min = b_y_min + c_y_min
        y_max = b_y_max - c_y_max

        first_axis = random.choice(['x', 'y'])

        if first_axis is 'x':
            rand_x = random.choice([x_min, x_max])
            rand_y = random.randint(y_min, y_max)
        else:
            rand_y = random.choice([y_min, y_max])
            rand_x = random.randint(x_min, x_max)

        loc_points = [
            (x+rand_x, y+rand_y) for x, y in content.exterior.coords[:-1]
        ]

        return loc_points


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
