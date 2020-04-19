import logging
import random
import matplotlib.pyplot as plt
from math import floor, ceil


from shapely.geometry import Polygon

from ..point import Point
from .utils import get_polygon_label, plot_space

log = logging.getLogger()


class Space(Polygon):
    """Space are 2-dimensional polygons that are containers for polygons or
    other Space-type objects (e.g. Rooms).

    Parameters
    ----------
    points: Point
        List of ``Point`` objects

    name: string
        Human-readable name of space

    contents: Polygons or subclasses of Polygons
        List of objects that should be located within the Space

    exist_sp: Space object
        For recreating a space with new points
    """
    def __init__(self, points=None, name=None, contents=None, exist_sp=None):
        self.max_retries = 15
        self.name = name
        self.points = points

        super().__init__(shell=[(pt.x, pt.y) for pt in points])

        # plan includes contents but with location modified to fit in Space
        if not exist_sp:
            self.plan = {}
            if contents:
                log.info(f'Contents found: {contents}')
                self.place_contents(contents)
        else:  # copy existing plan's contents over to newly created Space
            self.plan = self.recreate_plan(exist_sp)

    def __str__(self):
        return f'Space: {self.name}, AREA: {self.area}'

    def __repr__(self):
        return self.__str__()

    @property
    def contents(self):
        """Return objects in self.plan as a list"""
        return list(self.plan.keys())

    def place_contents(self, contents):
        """Iterate through each content to place_content()"""

        for content in contents:
            self.place_content(content)

    def place_content(self, content, retries=0):
        """Places content in a valid location"""
        plan_label = get_polygon_label(content)

        log.debug(f"Placing {plan_label}...")

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
                # handle input for shapely Polygon class because parameters
                # are expected to be different
                place = Polygon(shell=potential_location)
            else:  # handle input for RBC Polygon subclass objects
                respective_points = [Point(x, y)
                                     for (x, y) in potential_location]

                # TODO Creating a new object shuffles the contents. This
                # behavior should be prevented so that child polygons are not
                # shuffled by default.
                place = content.__class__(points=respective_points,
                                          name=content.name,
                                          contents=content.contents,
                                          exist_sp=content)

                # Make sure room_type is preserved if it exists
                if hasattr(content, 'room_type'):
                    place.room_type = content.room_type

            if self.validate_place(place):
                # object's location is valid; add object to self.plan dict
                self.plan[plan_label] = place
                return
            else:  # location is not valid; retry
                log.info(f"Failed to place {plan_label}. Retrying...")
                retries += 1

        log.info(f"Reached max retries for {plan_label}. Skipping...")
        # max retries reached; continue finishing up Space construction
        # without content
        return

    def place_content_at(self, content, x_offset=0, y_offset=0):
        """Determine points from given offsets and place content in space"""
        loc_points = [
            (x+x_offset, y+y_offset) for x, y in content.exterior.coords[:-1]
        ]

        respective_points = [Point(x, y)
                             for (x, y) in loc_points]

        place = content.__class__(points=respective_points,
                                  name=content.name,
                                  contents=content.contents,
                                  exist_sp=content)

        # Make sure room_type is preserved if it exists
        if hasattr(content, 'room_type'):
            place.room_type = content.room_type

        if self.validate_place(place):
            # object's location is valid; add object to self.plan dict
            log.info(f"Successfully placed {content.name}.")
            self.plan[content.name] = place
        else:  # location is not valid
            log.info(f"Failed to place {content.name}.")
            raise Exception
        return


    def validate_place(self, place):
        """A place is valid if it is not in conflict with any other object in
        self.plan and if the place is within the Space.
        """
        # TODO This method could use a better name
        if not place.within(self):
            return False

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

    def recreate_plan(self, sp):
        """Creates new Space with same contents as an existing Space at a new
        location defined by the points parameter.
        """
        old_origin_x, old_origin_y = sp.bounds[:2]
        new_origin_x, new_origin_y = self.bounds[:2]

        log.debug(f'old coords: ({old_origin_x}, {old_origin_y})')
        log.debug(f'new coords: ({new_origin_x}, {new_origin_y})')

        translate_x = new_origin_x - old_origin_x
        translate_y = new_origin_y - old_origin_y

        log.debug(f'translate: ({translate_x}, {translate_y})')

        # store relative location from relative origin
        relative_loc = {}
        new_plan = {}

        for name, poly in sp.plan.items():
            # lower left coordinates
            poly_x, poly_y = poly.bounds[:2]
            relative_loc[name] = (poly_x - old_origin_x,
                                  poly_y - old_origin_y)

            old_coords = poly.exterior.coords[:4]
            new_points = [Point(old_x + translate_x, old_y + translate_y)
                          for (old_x, old_y) in old_coords]

            new_poly = poly.__class__(points=new_points, name=name)
            new_plan[name] = new_poly

        return new_plan

    def corner_locate(self, content):
        """Return a set of points for a random corner"""
        b_x_min, b_y_min, b_x_max, b_y_max = self.bounds
        c_x_min, c_y_min, c_x_max, c_y_max = content.bounds
        x_min = min(b_x_min, c_x_min)
        x_max = b_x_max - c_x_max
        y_min = min(b_y_min, c_y_min)
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
            rand_y = random.randint(ceil(y_min), floor(y_max))
        else:  # pragma: no cover
            rand_y = random.choice([y_min, y_max])
            rand_x = random.randint(ceil(x_min), floor(x_max))

        loc_points = [
            (x+rand_x, y+rand_y) for x, y in content.exterior.coords[:-1]
        ]

        return loc_points

    def plot(self, figsize=(12, 12)):
        plot_space(self)
