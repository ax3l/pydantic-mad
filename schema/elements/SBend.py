from .base import Thick

from annotated_types import Gt
from pydantic import Field
from typing import Annotated, Literal


class SBend(Thick):
    """An ideal sector bend."""

    element: Literal["sbend"] = "sbend"
    """The element type"""

    rc: Annotated[float, Gt(0)]
    """Radius of curvature in m"""
