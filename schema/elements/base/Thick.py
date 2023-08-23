from annotated_types import Gt
from pydantic import BaseModel
from typing import Annotated

from .Element import Element

class Thick(Element):
    ds: Annotated[float, Gt(0)]
    nslice: int = 1
