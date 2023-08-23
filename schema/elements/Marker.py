from .base import Thin

from annotated_types import Gt
from typing import Literal


class Marker(Thin):
    element: Literal["marker"] = "marker"
    name: str
