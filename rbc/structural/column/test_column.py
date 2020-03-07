import pytest
from unittest import mock

from .column import Column
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
def one_z_column(one_z_points):
    yield Column(points=one_z_points)


# =================
# TESTS
# =================

def test_generic_column(one_z_column):
    c = one_z_column

    assert c.height == 1
    assert str(c) == 'Column([(0.0, 0.0, 0.0), (0.0, 0.0, 1.0)])'


def test_load_column(one_z_column):
    c = one_z_column

    kg = Load(1)
    c.apply_load(kg)

    assert c.load_data == [{'load': kg, 'location': 100}]
    assert c.base_reaction == -1


def test_column_with_loads(one_z_points):
    l1 = {'load': Load(-1), 'location': 50}
    l2 = {'load': Load(2), 'location': 100}

    c = Column(points=one_z_points, loads=[l1, l2])

    assert c.base_reaction == -1
    assert c.fbd_data == {0: -1, 50: -1, 100: 2}
    assert c.internal_loads == {0: -1, 50: -2, 100: 0}

    assert c.internal_load_at(25) == -1
    assert c.internal_load_at(75) == -2


def test_plot(one_z_column):
    """plt.show() should be called"""
    c = one_z_column

    l1 = Load(-1)
    c.apply_load(l1)

    with mock.patch('matplotlib.pyplot.show') as mock_show:
        c.plot(include_loads=True)
        mock_show.assert_called()
