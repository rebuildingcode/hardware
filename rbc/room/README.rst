Room
====

``Room`` objects are common elements in buildings and houses. ``FloorPlan``
objects will be containers for ``Room`` objects. ``Room`` is a subclass of
Shapely's ``Polygon``. This allows ``Room`` to inherit useful attributes and
methods such as ``.area``, ``.contains()``, ``.touches()``, etc.


Parameters/Attributes
---------------------

points
  List of ``Point`` objects

room_type
  Type of room (e.g. bedroom, bathroom, kitchen, living room, etc.)

min_area
  This value will be used to determine the minimum random value when
  generating rooms


Constants
---------

MIN_AREA = 70
  Set based on the Residential Building Code

MIN_WIDTH = 7
  Set based on the Residential Building Code

MAX_WIDTH = 15
  This constant is likely to change.


Examples
--------

Creating a 10x10 room
~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> pt1 = Point(0, 0)
    >>> pt2 = Point(0, 10)
    >>> pt3 = Point(10, 10)
    >>> pt4 = Point(10, 0)
    >>> square_room = Room(points=[pt1, pt2, pt3, pt4], room_type="shed")
    >>> square_room.area
    100
    >>> square_room.room_type


Real-World Constraints
----------------------

The Residential Building Code has the following provisions:

* Minimum area: no less than 70 square feet
* Minimum dimension: no less than 7 feet in any horizontal dimension