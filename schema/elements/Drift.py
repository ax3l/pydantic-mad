from .base import Thick

from typing import Literal


class Drift(Thick):
    element: Literal["drift"] = "drift"
