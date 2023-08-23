from .base import Thick

from annotated_types import Gt
from typing import Annotated, Literal


class SBend(Thick):
    element: Literal["sbend"] = "sbend"
    rc: Annotated[float, Gt(0)]
