import pytest
from unittest import TestCase

from ..point import Point
from ..space import Space
from ..room import Room
from .floorplan import FloorPlan


# =================
# FIXTURES
# =================

@pytest.fixture
def ten_by_ten_points():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 10, 0)
    p3 = Point(10, 10, 0)
    p4 = Point(10, 0, 0)

    yield [p1, p2, p3, p4]


@pytest.fixture
def ten_by_ten_fp(ten_by_ten_points):
    yield FloorPlan(points=ten_by_ten_points, name='10x10 Floor Plan')


@pytest.fixture
def eight_by_five_room():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 8, 0)
    p3 = Point(5, 8, 0)
    p4 = Point(5, 0, 0)

    yield Room(points=[p1, p2, p3, p4], name='8x5 room')


@pytest.fixture
def five_by_five_space():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 5, 0)
    p3 = Point(5, 5, 0)
    p4 = Point(5, 0, 0)

    yield Space(points=[p1, p2, p3, p4], name='5x5 space')


# =================
# TESTS
# =================

def test_generic_floorplan(ten_by_ten_fp):
    """ten_by_ten_space should have an area value of 100"""
    assert ten_by_ten_fp.area == 100
    assert str(ten_by_ten_fp) == 'FloorPlan: 10x10 Floor Plan, Rooms: None'
    assert ten_by_ten_fp.__repr__() == 'FloorPlan: 10x10 Floor Plan, Rooms: None'


def test_floorplan_with_room(ten_by_ten_points, eight_by_five_room):
    fp = FloorPlan(points=ten_by_ten_points, rooms=[eight_by_five_room])

    assert '8x5 room' in fp.plan.keys()


# =================
# TESTCASES
# =================

@pytest.mark.usefixtures('ten_by_ten_points', 'five_by_five_space')
class TestFloorPlan(TestCase):
    def test_floorplan_with_space(self):
        self.assertRaises(Exception, FloorPlan, points=ten_by_ten_points,
                          rooms=[five_by_five_space])