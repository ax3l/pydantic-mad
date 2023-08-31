from pydantic import BaseModel
from typing import Literal

from .Element import Element


class Thin(Element):
    """A mix-in model for elements with finite segment length"""

    element: Literal["ds"] = 0.0
    """Segment length in m (thin elements are always zero)"""
