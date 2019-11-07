import pytest

from .polygon import Polygon
from ..point.point import Point


@pytest.fixture()
def one_by_one():
    p1 = Point(0, 1, 0)
    p2 = Point(1, 1, 0)
    p3 = Point(1, 0, 0)
    p4 = Point(0, 0, 0)
    yield [p1, p2, p3, p4]


def test_area_from_points(one_by_one):
    a = Polygon(one_by_one)

    assert a.area == 1


def test_area_from_dimensions():
    a = Polygon(dimensions=(3, 4))
    assert a.area == 12
