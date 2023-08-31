from .base import Thin

from annotated_types import Gt
from typing import Literal


class Marker(Thin):
    """A marker of a position in a line"""

    element: Literal["marker"] = "marker"
    """The element type"""

    name: str
    """"A unique name for the element when placed in the line"""
