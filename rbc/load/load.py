from abc import ABC


class Load(ABC):
    def __init__(self, magnitude, direction=None, label=None,
                 description=None):
        self.magnitude = magnitude
        self.direction = direction
        self.label = label
        self.description = description


    def __repr__(self):
        return f"Load({self.magnitude}, '{self.direction}')"

    def __str__(self):
        if self.label:
            return (f'{self.label}: {self.magnitude} in the {self.direction} '
                    'direction')
        else:
            return f'{self.magnitude} in the {self.direction} direction'



class PointLoad(Load):
    def __init__(self, distance=None, **kwargs):
        super().__init__(**kwargs)

        # NOTE not likely to keep this attribute as the host should be
        # responsible for knowing where the load is applied.
        self.distance = distance
