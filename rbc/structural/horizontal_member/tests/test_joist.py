import pytest

from rbc.point import Point
from ..joist import Joist
from ...load import PointLoad, UniformLoad


def test_joist():
    j = Joist(length=10)
    j.create_and_add_uniform_load(-2)

    assert j.length == 10
    assert j.uniform_load == -2
    assert j.max_moment == 25
    assert j.max_shear == 10

    # Joist should be accept UniformLoads
    l = UniformLoad(magnitude=-2, direction='Z')
    j.add_load(l)

    assert j.uniform_load == -4
    assert j.max_moment == 50
    assert j.max_shear == 20


def test_conn_type():
    j = Joist(length=10, conn=('roller', 'pinned'))

    assert j.start_conn_type == 'roller'
    assert j.end_conn_type == 'pinned'
    assert j.conn == ('roller', 'pinned')


def test_invalid_conn_types():
    with pytest.raises(Exception):
        Joist(length=10, conn=('pinned', 'glued'))


def test_moment_shear_with_invalid_conn():
    j = Joist(length=10, conn=('pinned', 'pinned'))

    # max_moment and max_shear property methods checks that self.conn includes
    #  both 'pinned' and 'roller'
    with pytest.raises(Exception):
        j.max_moment
    with pytest.raises(Exception):
        j.max_shear


def test_joist_with_uniform_load_and_loc():
    j = Joist(length=10, conn=('roller', 'pinned'))
    l = UniformLoad(magnitude=-2, direction='Z')

    j.add_load(l, loc=(0, 5))

    assert j.uniform_load == -2


def test_joist_with_uniform_load_and_invalid_loc():
    j = Joist(length=10, conn=('roller', 'pinned'))
    l = UniformLoad(magnitude=-2, direction='Z')

    # loc for uniform loads needs to be a tuple (start, end)
    with pytest.raises(Exception):
        j.add_load(l, loc=(5))


def test_joist_with_point_loads():
    j = Joist(length=10)
    l = PointLoad(magnitude=-5, direction='Z')

    j.add_load(l, loc=5)

    assert j.point_loads == [{'load': l, 'mem_start': 5}]


def test_joist_with_invalid_point_load():
    j = Joist(length=10)
    l = PointLoad(magnitude=-5, direction='Z')

    with pytest.raises(Exception):
        j.add_load(l)
