from ...point import Point


INIT_ERROR_MSG = ('HorizontalMembers can only be instantiated with either a '
                  'length value or with points')


class HorizontalMember:
    def __init__(self, length=None, points=None):
        if length and points:
            raise Exception(INIT_ERROR_MSG)
        elif not length and not points:
            raise Exception(INIT_ERROR_MSG)
        elif not length:
            self.points = points
            self.length = points[0].distance(points[1])
        else:
            self.length = length
            self.points = [
                Point(0, 0, 0),
                Point(self.length, 0, 0)
            ]

    @property
    def start_point(self):
        return self.points[0]

    @property
    def end_point(self):
        return self.points[1]
