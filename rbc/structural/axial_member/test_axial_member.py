import pytest
from unittest import mock

from .axial_member import AxialMember
from ...point import Point
from ..load import Load


# =================
# FIXTURES
# =================

@pytest.fixture
def one_z_points():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 0, 1)

    yield [p1, p2]


@pytest.fixture
def one_z_member(one_z_points):
    yield AxialMember(points=one_z_points)


# =================
# TESTS
# =================

def test_generic_axial_member(one_z_member):
    am = one_z_member

    assert str(am) == 'AxialMember([(0.0, 0.0, 0.0), (0.0, 0.0, 1.0)])'
    assert am.length == 1.0


def test_axial_member_with_not_two_points():
    p1 = Point(0, 0, 1)
    with pytest.raises(Exception):
        am = AxialMember(points=[p1])


def test_axial_member_with_points_without_z():
    p1 = Point(0, 0)
    p2 = Point(0, 1)
    with pytest.raises(Exception):
        am = AxialMember(points=[p1, p2])


def test_axial_member_with_loads(one_z_points):
    _l1 = Load(-1)
    _l2 = Load(2)
    l1 = {'load': _l1, 'location': 100}
    l2 = {'load': _l2, 'location': 100}

    am = AxialMember(points=one_z_points, loads=[l1, l2])

    assert am.load_data == [
        {'load': _l1, 'location': 100},
        {'load': _l2, 'location': 100},
    ]


def test_plot(one_z_member):
    """plt.show() should be called"""
    am = one_z_member

    with mock.patch('matplotlib.pyplot.show') as mock_show:
        am.plot()
        mock_show.assert_called()
