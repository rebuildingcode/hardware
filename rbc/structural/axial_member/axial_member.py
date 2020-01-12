import logging
from abc import ABC, abstractmethod

from shapely.geometry import LineString

from .utils import plot_axial_member

log = logging.getLogger()


class AxialMember(LineString, ABC):
    """AxialMembers are defined by 2 points and can

    Parameters
    ----------
    points : list of ``Point``s
        This class only accepts lists of two points, one for each end

    loads : dict of ``Load``s and their location
    """
    def __init__(self, points, loads=None):

        if len(points) != 2:
            raise Exception

        # all points need a z-coordinate
        for p in points:
            if not p.has_z:
                raise Exception

        self.points = points
        self.coordinates = [(p.x, p.y, p.z) for p in self.points]

        super().__init__(coordinates=self.coordinates)

        self.load_data = []
        if loads:
            for l in loads:
                load = l['load']
                location = l['location']
                self.apply_load(load, location)

    def __repr__(self):
        return f'AxialMember({self.coordinates})'

    def __str__(self):
        return self.__repr__()

    @property
    def startpoint(self):
        # convenient way to return the rbc.Point object
        return self.points[0]

    @property
    def endpoint(self):
        # convenient way to return the rbc.Point object
        return self.points[1]

    @property
    def length(self):
        # rbc.Point objects can return distances in the Z axis
        return self.startpoint.distance(self.endpoint)

    def apply_load(self, load, location=100):
        """
        Parameters
        ----------
        loads : list of ``Load``s

        location : int from 0 to 100
            Represents the percentage of length from the base_point
        """
        self.load_data.append({
            'load': load,
            'location': location
        })

    @property
    def fbd_data(self):
        """JSON data for creating the free-body-diagram for the column"""
        fbd = {}

        # add reaction to fbd
        fbd[0] = self.base_reaction

        for load_obj in self.load_data:
            fbd[load_obj['location']] = load_obj['load'].magnitude

        return fbd

    @property
    def internal_loads(self):
        il = {}

        for loc, magnitude in self.fbd_data.items():
            log.info(il)
            if il:
                il[loc] = magnitude + list(il.values())[-1]
            else:
                il[loc] = magnitude

        return il

    def internal_load_at(self, loc):
        il = self.internal_loads

        key = max([k for k in il.keys() if k < loc])

        return il[key]

    def plot(self, include_loads=False):
        plot_axial_member(self, include_loads=include_loads)