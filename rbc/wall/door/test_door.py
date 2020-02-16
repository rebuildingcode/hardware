from .door import Door


def test_door():
    """Test default Door values"""
    d = Door()

    assert d.thickness == 1.375
    assert d.width == 32