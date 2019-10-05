from .node import Node


def test_distance_from():
    """Should return the correct value for distance"""

    a = Node(0, 0, 0)
    b = Node(1, 2, 3)

    # exact answer is 3.7416573867739413
    assert a.distance_from(b) > 3.74
    assert a.distance_from(b) < 3.75
    
