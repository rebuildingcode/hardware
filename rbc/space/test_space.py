import pytest
from unittest import mock

from .space import Space
from ..point.point import Point
from shapely.geometry import Polygon


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
def five_by_four_points():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 4, 0)
    p3 = Point(5, 4, 0)
    p4 = Point(5, 0, 0)

    yield [p1, p2, p3, p4]

@pytest.fixture
def ten_by_ten_space(ten_by_ten_points):
    yield Space(points=ten_by_ten_points, name='10x10 Space')


@pytest.fixture
def five_by_four_poly(five_by_four_points):
    poly = Polygon(shell = [(pt.x, pt.y) for pt in five_by_four_points])

    yield poly


@pytest.fixture
def five_by_four_space(five_by_four_points):
    poly = Space(points=five_by_four_points, name='5x4 Space')

    yield poly


# =================
# HELPER FUNCTIONS
# =================

def nameable_space(name, x, y):
    p1 = Point(0, 0, 0)
    p2 = Point(0, y, 0)
    p3 = Point(x, y, 0)
    p4 = Point(x, 0, 0)
    points = [p1, p2, p3, p4]

    return Space(points=points, name=name)


# =================
# TESTS
# =================

def test_space_area(ten_by_ten_space):
    """ten_by_ten_space should have an area value of 100"""
    assert ten_by_ten_space.area == 100


def test_place_contents_polygon(ten_by_ten_points, five_by_four_poly):
    """Space object should be able to contain shapely Polygon objects"""
    s = Space(points=ten_by_ten_points, contents=[five_by_four_poly])

    assert s.plan['AREA: 20.0'].within(s)


def test_place_contents_space(ten_by_ten_points, five_by_four_space):
    """Space object should be able to contain shapely Polygon objects"""
    s = Space(points=ten_by_ten_points, contents=[five_by_four_space])

    assert s.plan['5x4 Space'].within(s)


def test_place_contents_will_not_fit_second_content(ten_by_ten_points):
    """Space object should be able to contain shapely Polygon objects"""
    three_square = nameable_space('three square', 3, 3)
    eight_square = nameable_space('eight square', 8, 8)

    # eight_square is not expected to fit after three_square is placed
    s = Space(points=ten_by_ten_points, contents=[
        three_square, eight_square
    ])

    assert len(s.plan) == 1
    assert list(s.plan.keys()) == ['three square']


def test_place_contents_will_fit_second_content(ten_by_ten_points):
    """Space object should be able to contain shapely Polygon objects"""
    three_square = nameable_space('three square', 3, 3)
    five_square = nameable_space('five square', 5, 5)

    # eight_square is not expected to fit after three_square is placed
    s = Space(points=ten_by_ten_points, contents=[
        three_square, five_square
    ])

    assert len(s.plan) == 2
    assert list(s.plan.keys()) == ['three square', 'five square']


def test_plot_space(ten_by_ten_points, five_by_four_space):
    """plt.show() should be called"""
    s = Space(points=ten_by_ten_points, contents=[five_by_four_space])

    with mock.patch('matplotlib.pyplot.show') as mock_show:
        s.plot()
        # plot_rooms([random_room])
        mock_show.assert_called()
