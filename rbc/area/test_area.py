import pytest

from .area import Area
from ..point.point import Point


@pytest.fixture()
def point_1():
    yield Point(0, 1, 0)


@pytest.fixture()
def point_2():
    yield Point(1, 1, 0)


@pytest.fixture()
def point_3():
    yield Point(1, 0, 0)


@pytest.fixture()
def point_4():
    yield Point(0, 0, 0)


def test_area_from_points(point_1, point_2, point_3, point_4):
    a = Area([point_1, point_2, point_3, point_4])

    assert a.area() == 1


def test_area_from_dimensions():
    a = Area(dimensions=(3, 4))
    assert a.area() == 12