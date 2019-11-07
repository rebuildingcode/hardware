import pytest

from .point import Point


def test_distance_for_2d_space():
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    assert p1.distance(p2) == 5


def test_distance_for_3d_space():
    p1 = Point(0, 0)
    p2 = Point(3, 4, 12)
    p3 = Point(0, 0, 10)

    assert p1.distance(p2) == 13
    assert p3.distance(p1) == 10

    # test with tuple (x, y, z)
    assert p2.distance((0, 0, 12)) == 5

    # test with tuple (x, y)
    assert p2.distance((3, 4)) == 12


def test_relative_to_creates_point_at_correct_location():
    p1 = Point(0, 10, 0)
    p2 = Point.relative_to(p1, (10, 0, 10))
    p3 = Point.relative_to(p1, (10, 0))

    assert (p2.x, p2.y, p2.z) == (10, 10, 10)
    assert list(p3.coords)[0] == (10, 10, 0)


def test_temp_point_returns_error():
    p1 = (0, 10, 5)
    with pytest.raises(ValueError):
        p2 = Point.relative_to(p1, (5,))