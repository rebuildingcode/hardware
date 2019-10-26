from ..point.point import Point

class Polygon():
    """Four points required to create an Polygon

    Parameters
    ----------
    points : iterable of Points
    dimensions : tuple of floats

    Attributes
    ----------
    area : float
        area of polygon

    Examples
    --------
    >>> poly1 = Polygon([(0, 0), (1, 0), (0, 1), (1, 1)])
    >>> poly1.area
    1

    >>> poly2 = Polygon((2, 2))
    >>> poly2.area
    4

    """
    def __init__(self, points=[], dimensions=None):

        if dimensions:
            points = self.create_from_dim(dimensions)
        self.points = self.validate(points)
        self.area = self._get_area()
        
    def __repr__(self):
        return f"Polygon({[v for _, v in self.points.items()]})"

    def _get_area(self):
        """Calculate and return the area"""
        len_x = self.points['2'].x - self.points['1'].x
        len_y = self.points['1'].y - self.points['4'].y
        return len_x * len_y

    def create_from_dim(self, dimensions):
        """Generate points from (x, y) tuple
        
        Parameters
        ----------
        dimensions : tuple of floats
            dimensions of rectangle given in format, (x, y)

        Returns
        -------
        list of Points that correlate to given dimensions

        """
        z = 0  # default zero
        x, y = dimensions
        lower_left = Point(0, 0, z)
        lower_right = Point(x, 0, z)
        upper_left = Point(0, y, z)
        upper_right = Point(x, y, z)
        return [lower_left, lower_right, upper_left, upper_right]

    def validate(self, points):
        """Validate that set of points represents a rectangular polygon

        Parameters
        ----------
        points : iterable of Points
        
        Returns
        ------- 
        dict of Points in order starting from top left ``Point``, going
        clockwise
        
        """
        assert len(points) == 4
        x_set = set([point.x for point in points])
        y_set = set([point.y for point in points])
        z_set = set([point.z for point in points])

        assert len(x_set) == len(y_set) == 2
        assert len(z_set) == 1  # only support polygons in one z-plane

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
