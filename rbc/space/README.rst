Space
=====

``Space`` objects are defined by a list of ``Point`` objects.


Parameters
----------

points: list
  list of ``Point`` objects used to define the ``Space``

name: string
  Human-readable name of Space

contents: Polygons or subclasses of Polygons
  List of objects that should be located within the Space


Attributes
----------

plan: dict
  dict of Polygons contained in Space (key is name and value is Polygon)


area
  the total area of the Space (inherited from Shapely's Polygon)


Examples
--------

Creating a Space
~~~~~~~~~~~~~~~~

.. code:: python

  >>> bd1 = Point(0, 0)
  >>> bd2 = Point(0, 10)
  >>> bd3 = Point(10, 10)
  >>> bd4 = Point(10, 0)
  >>> bedroom = Space(points=[bd1, bd2, bd3, bd4], name='bedroom')
  >>> bedroom.area
  100


Placing ``bedroom`` inside of another Space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

  >>> adu_pt1 = Point(0, 0)
  >>> adu_pt2 = Point(0, 15)
  >>> adu_pt3 = Point(20, 15)
  >>> adu_pt4 = Point(20, 0)
  >>> adu = Space(points=[adu_pt1, adu_pt2, adu_pt3, adu_pt4], name='adu',
                  contents=[bedroom])
  >>> adu.plan
  {'bedroom': <rbc.room.room.Room at 0x116880588>}

  >>> bedroom.within(adu)
  True

  >>> adu.contains(bedroom)
  True
