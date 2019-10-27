Polygon
=======

``Polygon``s are shapes 


Parameters
----------

points
  list of ``Point``s used to define the ``Polygon``

dimensions 
  tuple of dimensions (x, y) used to define the ``Polygon``


Attributes
----------

area
  the total area of the polygon


Examples
--------

Finding the area of a polygon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. codeblock:: python

    >>> poly1 = Polygon([(0, 0), (1, 0), (0, 1), (1, 1)])
    >>> poly1.area
    1

    >>> poly2 = Polygon((2, 2))
    >>> poly2.area
    4
