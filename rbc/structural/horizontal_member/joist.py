from .horizontal_member import HorizontalMember
from .mixins import UniformlyLoadedMixin


class Joist(UniformlyLoadedMixin, HorizontalMember):
    """Uniformly loaded horizontal member

    Parameters
    ----------
    uniform_load : float
        Distributed load applied along the length of the member

    Limitations
    -----------
    Joist is assumed to be supported by a pin and roller for simpler analysis

    """

    def __init__(self, uniform_load=0, **kwargs):
        super().__init__(**kwargs)

        self.uniform_load = uniform_load
