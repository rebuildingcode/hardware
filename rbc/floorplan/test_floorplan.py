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
def thirteen_by_ten_points():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 10, 0)
    p3 = Point(13, 10, 0)
    p4 = Point(13, 0, 0)

    yield [p1, p2, p3, p4]


@pytest.fixture
def thirteen_by_ten_fp(thirteen_by_ten_points):
    yield FloorPlan(points=thirteen_by_ten_points, name='13x10 Floor Plan')


@pytest.fixture
def eight_by_five_room():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 8, 0)
    p3 = Point(5, 8, 0)
    p4 = Point(5, 0, 0)

    yield Room(points=[p1, p2, p3, p4], name='8x5 room', room_type='bedroom')


@pytest.fixture
def eight_by_eight_room():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 8, 0)
    p3 = Point(8, 8, 0)
    p4 = Point(8, 0, 0)

    yield Room(points=[p1, p2, p3, p4], name='8x8 room', room_type='bedroom')


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

def test_generic_floorplan(thirteen_by_ten_fp):
    """thirteen_by_ten_space should have an area value of 100"""
    assert thirteen_by_ten_fp.area == 130
    assert str(thirteen_by_ten_fp) == 'FloorPlan: 13x10 Floor Plan, Rooms: []'
    assert thirteen_by_ten_fp.__repr__() == 'FloorPlan: 13x10 Floor Plan, Rooms: []'


def test_floorplan_with_room(thirteen_by_ten_points, eight_by_five_room):
    fp = FloorPlan(points=thirteen_by_ten_points, rooms=[eight_by_five_room])
    assert '8x5 room' in fp.rooms

    assert fp.room_count() == {'bedroom': 1}
    assert fp.plan_summary() == {'bedroom': 40}


def test_floorplan_with_two_rooms(thirteen_by_ten_points, eight_by_eight_room, eight_by_five_room):
    fp = FloorPlan(points=thirteen_by_ten_points)

    fp.add_room(eight_by_eight_room)
    fp.add_room(eight_by_five_room, x_offset=8)

    assert fp.room_count() == {'bedroom': 2}
    assert fp.plan_summary() == {'bedroom': 104}


def test_fp_with_invalid_room_placement(thirteen_by_ten_points, eight_by_eight_room):
    """Placing a room where part of the room is located outside of the
    FloorPlan should raise an Exception"""
    fp = FloorPlan(points=thirteen_by_ten_points)
    with pytest.raises(Exception):
        fp.add_room(eight_by_eight_room, y_offset=5)


def test_fp_with_space_raises_exc(thirteen_by_ten_points, five_by_five_space):
    """FloorPlan will not accept Spaces and is expected to raise an exception
    """
    with pytest.raises(Exception):
        FloorPlan(points=thirteen_by_ten_points, rooms=[five_by_five_space])


# =================
# TESTCASES
# =================

# NOTE: pytest.raises() used above follows the same pattern as previous tests
# and does not require the use of TestCases. TestCase was originally used in
# order to assert that an Exception was raised with assertRaises. Will opt for
# the pytest implementation until TestCase becomes necessary.

# @pytest.mark.usefixtures('ten_by_ten_points', 'five_by_five_space')
# class TestFloorPlan(TestCase):
#     def test_floorplan_with_space(self):
#         self.assertRaises(Exception, FloorPlan, points=ten_by_ten_points,
#                           rooms=[five_by_five_space])
