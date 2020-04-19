import pytest

from .load import PointLoad, UniformLoad
from .utils import sum_loads


# =================
# FIXTURES
# =================

@pytest.fixture
def two_kip_per_ft_uniform_load():
    u = UniformLoad(magnitude=-2, direction='Z', force_unit='kip')
    yield u

@pytest.fixture
def three_kip_per_ft_uniform_load():
    u = UniformLoad(magnitude=-3, direction='Z', force_unit='kip')
    yield u

@pytest.fixture
def five_kip_point_load():
    p = PointLoad(magnitude=-5, direction='Z', force_unit='kip')
    yield p


# =================
# TESTS
# =================

def test_loads_must_be_same_type(two_kip_per_ft_uniform_load,
                                 three_kip_per_ft_uniform_load,
                                 five_kip_point_load):
    s = sum_loads(two_kip_per_ft_uniform_load, three_kip_per_ft_uniform_load)
    assert s == (-5, 'kip')

    with pytest.raises(Exception):
        sum_loads(two_kip_per_ft_uniform_load, five_kip_point_load)


def test_loads_must_be_in_same_direction(two_kip_per_ft_uniform_load,
                                         three_kip_per_ft_uniform_load):
    three_kip_per_ft_uniform_load.direction = 'X'

    with pytest.raises(Exception):
        sum_loads(two_kip_per_ft_uniform_load, three_kip_per_ft_uniform_load)


def test_loads_must_have_the_same_units(two_kip_per_ft_uniform_load,
                                        three_kip_per_ft_uniform_load):
    three_kip_per_ft_uniform_load.force_unit = 'lb'

    with pytest.raises(Exception):
        sum_loads(two_kip_per_ft_uniform_load, three_kip_per_ft_uniform_load)
