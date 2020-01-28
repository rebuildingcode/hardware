from .wall import Wall


__all__ = ['Wall']


STANDARD_INTERIOR_WALL = Wall()
STANDARD_EXTERIOR_WALL = Wall(
    width=6,
    layer_B='5/16" Fiber Cement',
    layer_A='15/32" Structural Plywood',
    insulation='Fiberglass R-30',
    framing='2x6')

