from math import sqrt


class Node():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self._x = None
        self._y = None
        self._z = None


    def distance_from(self, other_node):
        dist = sqrt(
            (other_node.x - self.x) ** 2 
            + (other_node.y - self.y) ** 2
            + (other_node.z - self.z) ** 2
        )

        return dist