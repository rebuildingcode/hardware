import logging

from .load import PointLoad, UniformLoad
from .utils import sum_loads

log = logging.getLogger(__name__)


class LoadManager:
    def parse_load(self, load, mem_length, loc=None):
        """Return dict with Load object and load type"""

        if type(load) == PointLoad:
            if not loc:
                raise Exception('PointLoads need the loc parameter.')

            load_type = 'point'
            load_dict = {
                'load': load,
                'mem_start': loc,
            }
        elif type(load) == UniformLoad:
            if not loc:
                mem_start = 0
                mem_end = mem_length
            else:
                try:
                    mem_start = loc[0]
                    mem_end = loc[1]
                except:
                    raise Exception('Error occurred while parsing loc')

            load_type = 'uniform'
            load_dict = {
                'load': load,
                'mem_start': mem_start,
                'mem_end': mem_end,
            }

        return load_dict, load_type

    def get_total_uniform_load(self, load_dict):
        """Filter loads for uniform loads and return sum"""
        uniform_loads = []

        for load_data in load_dict['uniform']:
            uniform_loads.append(load_data['load'])

        if uniform_loads:
            sum, unit = sum_loads(*uniform_loads)
            return sum, unit

        else:
            return 0, None

    def get_point_load_list(self, load_dict):

        return load_dict['point']