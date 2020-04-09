import pytest

from ...point import Point
from .horizontal_member import HorizontalMember


# =================
# FIXTURES
# =================

@pytest.fixture
def zero_to_ten_points():
    p1 = Point(0, 0, 0)
    p2 = Point(10, 0, 0)

    yield [p1, p2]


# =================
# TESTS
# =================

def test_horizontal_member(zero_to_ten_points):
    hm1 = HorizontalMember(length=10)

    assert hm1.length == 10
    assert hm1.start_point.x == 0
    assert hm1.start_point.y == 0
    assert hm1.end_point.x == 10
    assert hm1.end_point.y == 0

    hm2 = HorizontalMember(points=zero_to_ten_points)

    assert hm1.length == 10
    assert hm1.start_point.x == 0
    assert hm1.start_point.y == 0
    assert hm1.end_point.x == 10
    assert hm1.end_point.y == 0


def test_raises_exception(zero_to_ten_points):
    with pytest.raises(Exception):
        hm = HorizontalMember()

    with pytest.raises(Exception):
        hm = HorizontalMember(points=zero_to_ten_points, length=20)
