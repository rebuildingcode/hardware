import pytest

from .load import Load, PointLoad, UniformLoad


def test_generic_load():
    l = Load(magnitude=5, direction='Y', label='car', description='weight of car')

    assert l.magnitude == 5
    assert l.direction == 'Y'
    assert l.label == 'car'
    assert l.description == 'weight of car'
    assert l.__repr__() == "Load(5 kip, 'Y')"
    assert l.__str__() == 'car: 5 kips in the Y direction'


def test_load_without_label():
    l = Load(magnitude=5, direction='Y', description='weight of car')

    assert l.__str__() == '5 kips in the Y direction'


def test_load_without_direction():
    with pytest.raises(Exception):
        l = Load(magnitude=5)


def test_point_load():
    p = PointLoad(magnitude=5, direction='Y', description='weight of sofa')

    assert p.magnitude == 5


def test_uniform_load():
    u = UniformLoad(magnitude=-2, force_unit='kip', length_unit='ft',
                    direction='Z')

    assert type(u) == UniformLoad


def test_load_with_invalid_force_unit():
    with pytest.raises(Exception):
        l = Load(magnitude=-5, force_unit='oz', direction='Z')


def test_load_with_invalid_length_unit():
    with pytest.raises(Exception):
        l = UniformLoad(magnitude=-2, force_unit='lb', length_unit='mi',
                        direction='Z')
