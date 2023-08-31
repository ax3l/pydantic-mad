from .base import Thick

from typing import Literal


class Drift(Thick):
    """A drift element"""

    element: Literal["drift"] = "drift"
    """The element type"""
