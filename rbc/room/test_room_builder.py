import pytest

from .room_builder import RoomBuilder

def test_room_builder():
    rb = RoomBuilder()
    rb.set_dimensions(10, 12)
    rb.set_name('Master Bedroom')
    rb.set_room_type('bedroom')

    master_bedroom = rb.room()

    assert master_bedroom.area == 120
    assert master_bedroom.area == 120