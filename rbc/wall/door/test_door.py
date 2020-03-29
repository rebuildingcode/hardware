import pytest
from .door import Door, DoorInstalled
from ...point import Point


def test_door():
    """Test default Door values"""
    d = Door()

    assert d.thickness == 1.375
    assert d.width == 32


@pytest.mark.parametrize("wall_direction, expected_end_coords", [
    ('X', [(72.0, 40.0)]),
    ('-X', [(8.0, 40.0)]),
    ('Y', [(40.0, 72.0)]),
    ('-Y', [(40.0, 8.0)]),
])
def test_door_installed(wall_direction, expected_end_coords):
    """End coordinates is calculated based on the wall direction"""
    p = Point(40, 40, 0)
    d = DoorInstalled(hinge_point=p, wall_direction=wall_direction)

    assert d.closed_xy.length == 32.0
    assert list(d.latch_point.coords) == expected_end_coords


def test_install_existing_door():
    """DoorInstalled should accept an existing door as a parameter"""
    p = Point(40, 40, 0)
    existing_door = Door(width=40, height=84)

    installed_door = DoorInstalled(hinge_point=p, wall_direction='X',
                                   door=existing_door)

    assert installed_door.width == 40
    assert installed_door.height == 84
