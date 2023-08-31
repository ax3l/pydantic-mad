from annotated_types import Gt
from pydantic import BaseModel, Field
from typing import Annotated, List, Union

from .elements.base import Element
from .elements import Drift, SBend, Marker


class Line(BaseModel):
    """A line of elements and/or other lines"""

    line: List[Union[Drift, SBend, Marker, "Line"]] = Field(..., discriminator="element")
    """A list of elements and/or other lines"""

    # Hints for pure Python usage
    class Config:
        validate_assignment = True

# Hints for pure Python usage
Line.update_forward_refs()

# TODO / Ideas
# - Validate the Element.name is, if set, unique in a Line (including nested lines).
