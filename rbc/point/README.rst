Point
=====

Point objects are coordinates in 3-dimensional space. They can be moved in 3D
space and distances can be measured between different points. They are used
to define ``Polygon`` objects, and soon will support other types of objects as
well.


Parameters/Attributes
---------------------

x
  Coordinate associated with east/west direction

y
  Coordinate associated with north/south direction

z
  Coordinate associated with elevation


Examples
--------

Moving ``Point`` objects
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

  >>> p1 = Point(0, 0)
  >>> p1.move(2, 4)
  >>> p1
  Point(2, 4, 0)


Measuring distances
~~~~~~~~~~~~~~~~~~~

.. code:: python

  >>> p1 = Point(0, 0)
  >>> p2 = Point(3, 4)
  >>> p2.distance_from(p1)
  5
