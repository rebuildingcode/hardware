import pytest

from .section import Section
from ...point import Point

# =================
# FIXTURES
# =================

@pytest.fixture
def ten_by_ten_points():
    p1 = Point(0, 0, 0)
    p2 = Point(0, 10, 0)
    p3 = Point(10, 10, 0)
    p4 = Point(10, 0, 0)

    yield [p1, p2, p3, p4]


@pytest.fixture
def ten_by_ten_section(ten_by_ten_points):
    yield Section(points=ten_by_ten_points)


# =================
# TESTS
# =================

def test_generic_section(ten_by_ten_section):
    s = ten_by_ten_section

    assert str(s) == 'Section: AREA=100.0, BOUNDS=(-5.0, -5.0, 5.0, 5.0)'


def test_new_section_with_dimensions():
    s = Section(rect_dim=(10, 10))

    assert s.exterior_coords == [
        (-5.0, -5.0), (-5.0, 5.0), (5.0, 5.0), (5.0, -5.0)
    ]


def test_section_with_invalid_params():
    # Section requires either points or rect_dim
    with pytest.raises(Exception):
        Section()

    # rect_dim requires iterable with two values
    with pytest.raises(Exception):
        Section(rect_dim=(10,))

    # radius needs to be a float or int
    with pytest.raises(Exception):
        Section(radius='r')

def test_circle_section():
    s = Section(radius=2)

    assert '{:.3f}'.format(s.area) == '12.546'