import pytest
from unittest import mock

from ..room import Room
from .constructors import random_rectangle


def test_random_rectangle():
    max_x = 10
    max_y = 10
    rect_points = random_rectangle(max_x, max_y)
    for point in rect_points:
        assert point.x <= max_x
        assert point.y <= max_y
