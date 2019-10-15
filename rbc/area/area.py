from ..point.point import Point

class Area():
    def __init__(self, points=[], dimensions=None):
        """Four points required to create an Area

        Args:
            points (Iterable of Points)
        """
        if dimensions:
            points = self.create_from_dim(dimensions)
        self.points = self.validate(points)
        
    def area(self):
        """Calculate and return the area"""
        len_x = self.points['2'].x - self.points['1'].x
        len_y = self.points['1'].y - self.points['4'].y
        return len_x * len_y

    def create_from_dim(self, dimensions):
        """Generate points from (x, y) tuple"""
        z = 0  # default zero
        x, y = dimensions
        lower_left = Point(0, 0, z)
        lower_right = Point(x, 0, z)
        upper_left = Point(0, y, z)
        upper_right = Point(x, y, z)
        return [lower_left, lower_right, upper_left, upper_right]

    def validate(self, points):
        """Validate that set of points represents a rectangular area

        Args:
            points (Iterable of Points)
        Returns: dict of points
        """
        assert len(points) == 4
        x_set = set([point.x for point in points])
        y_set = set([point.y for point in points])
        z_set = set([point.z for point in points])

        assert len(x_set) == len(y_set) == 2
        assert len(z_set) == 1  # only support areas in one z-plane

        top_left = [point for point in points 
                    if point.x == min(x_set) and point.y == max(y_set)][0]
        top_right = [point for point in points 
                     if point.x == max(x_set) and point.y == max(y_set)][0]
        bottom_right = [point for point in points 
                        if point.x == max(x_set) and point.y == min(y_set)][0]
        bottom_left = [point for point in points 
                        if point.x == min(x_set) and point.y == min(y_set)][0]

        return {
            '1': top_left,
            '2': top_right,
            '3': bottom_right,
            '4': bottom_left,
        }