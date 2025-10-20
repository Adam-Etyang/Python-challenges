"""
Create a simple, imutable way to represent a 2D point using collections.namedtuple
"""

from collections import namedtuple

# creating the namedtuple
Point = namedtuple("Point", ["x", "y"])

# including type hints
Point.__annotations__ = {"x": int, "y": int}

# instances of point
p1 = Point(10, 20)
p2 = Point(x=10, y=20)

# accessing fields from the instances of points
print(p1.x)
print(p2.y)

# comparing fields
if p1 == p2:
    print(True)
else:
    print(False)
