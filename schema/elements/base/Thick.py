from annotated_types import Gt
from pydantic import BaseModel
from typing import Annotated

from .Element import Element

class Thick(Element):
    """A mix-in model for elements with finite segment length"""

    ds: Annotated[float, Gt(0)]
    """Segment length in m"""

    nslice: int = 1
    """Number of slices through the segment (might be numerics and not phyics, thus might be removed)"""
