from .opening import Opening


def test_opening():
    o = Opening(width=36, height=80)

    assert o.height == 80
    assert o.width == 36
    assert o.area == 36 * 80