import pytest
from unittest import mock

from .room import Room
from ..point import Point


# =================
# FIXTURES
# =================

@pytest.fixture
def ten_by_ten_points():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 120, 0)
    p3 = Point(120, 120, 0)
    p4 = Point(120, 0, 0)

    yield [p1, p2, p3, p4]


# =================
# TESTS
# =================

def test_10_by_10_room(ten_by_ten_points):
    square_room = Room(points=ten_by_ten_points, room_type="shed")

    assert square_room.area == 14400
    assert square_room.room_type == "shed"


def test_random_room_without_bounds():
    random_room = Room.random()
    assert random_room.area > 0


def test_random_room_with_bounds():
    bounds = (2, 2, 10, 10)
    random_room = Room.random(bounds=bounds)
    rr_bounds = random_room.bounds
    assert rr_bounds[0] >= bounds[0]
    assert rr_bounds[1] >= bounds[1]
    assert rr_bounds[2] <= bounds[2]
    assert rr_bounds[3] <= bounds[3]
    assert random_room.area <= 64


def test_room_with_door(ten_by_ten_points):
    square_room = Room(points=ten_by_ten_points, room_type="shed")
    square_room.add_door(offset=60)

    assert square_room.door.latch_point.x == 92
