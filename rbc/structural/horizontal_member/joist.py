import logging
from collections import defaultdict

from ..load import UniformLoad
from ..load.load_manager import LoadManager

from .horizontal_member import HorizontalMember
from .mixins import UniformlyLoadedMixin

log = logging.getLogger(__name__)

VALID_CONN_TYPES = ['fixed', 'pinned', 'roller', 'free']


class Joist(UniformlyLoadedMixin, HorizontalMember):
    """Uniformly loaded horizontal member that will only support loads in the
    Z-direction

    Parameters
    ----------
    uniform_load : float
        Distributed load applied along the length of the member

    Limitations
    -----------
    Joist is assumed to be supported by a pin and roller

    """
    def __init__(self, conn=('pinned', 'roller'), **kwargs):
        super().__init__(**kwargs)

        self.loads = defaultdict(list)
        self.lm = LoadManager()

        self.conn = conn
        self.start_conn_type = conn[0]
        self.end_conn_type = conn[1]

        self.validate()

    def validate(self):
        if (self.start_conn_type not in VALID_CONN_TYPES or
            self.end_conn_type not in VALID_CONN_TYPES):
            raise Exception(
                f'Invalid connection type: {self.start_conn_type} and '
                f'{self.end_conn_type}. Connections must be one of '
                f'{VALID_CONN_TYPES}')

    @property
    def uniform_load(self):
        """Filter loads for uniform loads and return sum"""
        total_uniform_load, unit = self.lm.get_total_uniform_load(self.loads)
        log.info('%s %s', total_uniform_load, unit)
        return total_uniform_load

    @property
    def point_loads(self):
        """Filter loads and return list of point loads"""
        return self.lm.get_point_load_list(self.loads)

    def add_load(self, load, loc=None):
        """
        Input can be PointLoad, UniformLoad, or MomentLoad
        """
        parsed_load, load_type = self.lm.parse_load(load, self.length, loc)
        self.loads[load_type].append(parsed_load)

    def create_and_add_uniform_load(self, magnitude):
        """"""
        new_load = UniformLoad(magnitude=magnitude, direction='Z')
        self.add_load(new_load)

    def internal_forces_up_to(self, d):  # pragma: no cover
        """Return internal forces up to a given distance from start"""
        pass
