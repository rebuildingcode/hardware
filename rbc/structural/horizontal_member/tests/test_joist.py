import pytest

from rbc.point import Point
from ..joist import Joist


def test_joist():
    b = Joist(length=10, uniform_load=2)

    assert b.max_moment == 25
    assert b.max_shear == 10