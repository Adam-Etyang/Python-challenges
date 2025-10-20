"""
The scenario is that you want to represent a Circle. It has a center point and a radius.
represent it using NamedTuple
"""

from typing import NamedTuple


class Center(NamedTuple):
    x: float
    y: float


class Circle(NamedTuple):
    center: Center
    radius: float = 1.0


origin = Center(0, 0)
circle = Circle(center=origin, radius=5.5)

print(f"{circle.center},\n {circle.radius}")
