import logging

from ..axial_member import AxialMember
from ...load import PointLoad

log = logging.getLogger()


class Column(AxialMember):

    def __repr__(self):
        return f'Column({self.coordinates})'

    def __str__(self):
        return self.__repr__()

    @property
    def height(self):
        return self.length

    # def apply_load(self, load, location):
    #     pass

    @property
    def base_reaction(self):
        """

        Sum of forces and reactions must be equal to zero
            R_base + L1 + L2 + L3 + ... = 0

        Solve for R_base
            R_base = -(L1 + L2 + L3 + ...)

        """
        applied_loads = [l['load'] for l in self.load_data]
        total_load_applied = sum([l.magnitude for l in applied_loads])
        return -total_load_applied
