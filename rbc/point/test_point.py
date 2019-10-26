import pytest

from .point import Point


def test_repr():
    p1 = Point(1, 2, 3)
    assert p1.__repr__() == 'Point(1, 2, 3)'


def test_distance_from_returns_correct_value():
    p1 = Point(0, 0, 0)
    p2 = Point(3, 4, 12)

    assert p1.distance_from(p2) == 13

    # test with tuple (x, y, z)
    assert p2.distance_from((0, 0, 12)) == 5
    
    # test with tuple (x, y)
    assert p2.distance_from((3, 4)) == 12


def test_relative_to_creates_point_at_correct_location():
    p1 = Point(0, 10, 0)
    p2 = Point.relative_to(p1, (10, 0, 10))

    assert (p2.x, p2.y, p2.z) == (10, 10, 10)


def test_move_point_returns_correct_value():
    p1 = Point(0, 10, 5)
    p1.move(5, -5)

    assert (p1.x, p1.y, p1.z) == (5, 5, 5)


def test_temp_point_returns_error():
    p1 = Point(0, 10, 5)
    with pytest.raises(ValueError):
        p1.move(5)
