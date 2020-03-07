from .load import Load, PointLoad


def test_generic_load():
    l = Load(magnitude=5, direction='Y', label='car', description='weight of car')

    assert l.magnitude == 5
    assert l.direction == 'Y'
    assert l.label == 'car'
    assert l.description == 'weight of car'
    assert l.__repr__() == "Load(5, 'Y')"
    assert l.__str__() == 'car: 5 in the Y direction'


def test_load_without_label():
    l = Load(magnitude=5, direction='Y', description='weight of car')

    assert l.__str__() == '5 in the Y direction'


def test_point_load():
    p = PointLoad(magnitude=5, direction='Y', description='weight of sofa')

    assert p.magnitude == 5