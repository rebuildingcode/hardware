from abc import ABC

from ...point import Point


VALID_FORCE_UNITS = ['lb', 'kip']
VALID_LENGTH_UNITS = ['in', 'ft']


class Load(ABC):
    """Parent class for PointLoads and Uniform Loads

    Parameters
    ----------
    magnitude : float
        Intensity of force quantified by kips or kN
    direction : str
        X, Y, or Z
    label : str
        For use as keys in dicts
    description : str
        Property to provide additional context

    TODO:
    - [ ] Support for loads that are not in the principal X, Y, and Z axes
    """

    def __init__(self, magnitude, direction=None, label=None,
                 description=None, force_unit='kip'):
        if direction not in ['X', 'Y', 'Z']:
            raise Exception('Direction must be either X, Y, or Z')
        self.magnitude = magnitude
        self.direction = direction
        self.label = label
        self.description = description
        self.force_unit = force_unit
        self.validate()

    def __repr__(self):
        return f"Load({self.magnitude} {self.force_unit}, '{self.direction}')"

    def __str__(self):
        if self.label:
            return (f'{self.label}: {self.magnitude} {self.force_unit}s in '
                    f'the {self.direction} direction')
        else:
            return (f'{self.magnitude} {self.force_unit}s in the '
                    f'{self.direction} direction')

    def validate(self):
        if self.force_unit not in VALID_FORCE_UNITS:
            raise Exception(f'force_unit must be one of {VALID_FORCE_UNITS}')


class PointLoad(Load):
    """A force applied at a single point in one direction

    Parameters
    ----------
    distance : float
        offset distance from member's start_point

    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class UniformLoad(Load):
    """A load that is distributed evenly along a line

    By default, UniformLoads should be assumed to be applied to the entire
    length of a member.

    Parameters
    ----------
    magnitude : float
        Intensity of uniform load
    length : float
        Length of member where uniform load is applied

    """
    def __init__(self, magnitude, direction, length_unit='ft', **kwargs):
        self.length_unit = length_unit
        super().__init__(magnitude, direction, **kwargs)

        self.validate()

    def validate(self):
        super().validate()
        if self.length_unit not in VALID_LENGTH_UNITS:
            raise Exception(f'length_unit must be one of {VALID_LENGTH_UNITS}')
