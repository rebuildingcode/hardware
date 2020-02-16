from .door import Door


STANDARD_INTERIOR_DOOR = Door()
STANDARD_EXTERIOR_DOOR = Door(width=36, jamb_width=6.5625)
ADA_INTERIOR_DOOR = Door(width=36)
ADA_EXTERIOR_DOOR = Door(width=36, jamb_width=6.5625)
