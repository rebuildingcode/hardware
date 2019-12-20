import random
import matplotlib.pyplot as plt

from shapely.geometry import Polygon

from ..point import Point


class Space(Polygon):
    """Space are 2-dimensional polygons.

    Parameters
    ----------
    points: Point
        List of ``Point`` objects

    name: string
        Human-readable name of space

    contents: Polygons or subclasses of Polygons
        List of objects that should be located within the Space
    """
    def __init__(self, points=None, name=None, contents=None):
        self.max_retries = 15
        self.name = name
        self.contents = contents

        super().__init__(shell=[(pt.x, pt.y) for pt in points])

        # plan iscludes contents but with location modified to fit in Space
        self.plan = {}
        if self.contents:
            self.place_contents(self.contents)

    def place_contents(self, contents):
        """Iterate through each content to place_content()"""
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

        # TODO: add capability for Space to remember failed attempts to reduce
        # amount of tries needed; possibly keep a list of failed locations
        retries = 0
        while retries < self.max_retries:
            if retries < self.max_retries // 2:
                # attempt to locate object at the corners with the first half
                # of tries
                potential_location = self.corner_locate(content)
            else:
                # attempt to locate object at the edge with the rest of the
                # tries
                potential_location = self.edge_locate(content)

            # create a new Polygon-class object at the potential_location
            # this new object will be used to represent the original content
            if content.__class__ == Polygon:
                # handle input for shapely Polygon class
                place = Polygon(shell=potential_location)
            else:  # handle input for RBC Polygon subclass objects
                respective_points = [Point(x, y)
                                     for (x, y) in potential_location]
                place = content.__class__(points=respective_points)

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

        # TODO This method could use a better name
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
        b_x_min, b_y_min, b_x_max, b_y_max = self.bounds
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
        b_x_min, b_y_min, b_x_max, b_y_max = self.bounds
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
        """Plots a list of rooms

        TODO: This method should probably make use of a more general function
        plot any type of Polygon class object.
        """
        fig, ax = plt.subplots(figsize=figsize)

        # plot boundary
        x, y = self.exterior.xy
        ax.plot(x, y)

        # plot contents
        for label, poly in self.plan.items():
            x, y = poly.exterior.xy
            ax.plot(x, y)
            ax.text(poly.centroid.x, poly.centroid.y, s=label,
                    horizontalalignment='center', verticalalignment='center')
        plt.axis('scaled')
        plt.show()
