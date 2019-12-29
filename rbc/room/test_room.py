import pytest
from unittest import mock

from .room import Room
from ..point import Point


def test_10_by_10_room():
    pt1 = Point(0, 0)
    pt2 = Point(0, 10)
    pt3 = Point(10, 10)
    pt4 = Point(10, 0)

    square_room = Room(points=[pt1, pt2, pt3, pt4], room_type="shed")

    assert square_room.area == 100
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
