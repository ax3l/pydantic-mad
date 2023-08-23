from annotated_types import Gt
from pydantic import BaseModel, Field
from typing import Annotated, List, Union

from .elements.base import Element
from .elements import Drift, SBend, Marker


class Line(BaseModel):
    line: List[Union[Drift, SBend, Marker, 'Line']] = Field(..., discriminator='element')

Line.update_forward_refs()
