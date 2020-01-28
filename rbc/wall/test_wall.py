from .wall import Wall


def test_wall():
    """Default width of wall should be 6.5"""
    w = Wall()

    assert w.width == 4