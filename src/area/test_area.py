import pytest

from .area import Area
from ..node.node import Node


@pytest.fixture()
def node_1():
    yield Node(0, 1, 0)


@pytest.fixture()
def node_2():
    yield Node(1, 1, 0)

@pytest.fixture()
def node_3():
    yield Node(1, 0, 0)


@pytest.fixture()
def node_4():
    yield Node(0, 0, 0)


def test_area(node_1, node_2, node_3, node_4):
    A = Area([node_1, node_2, node_3, node_4])

    assert A.area() == 1

