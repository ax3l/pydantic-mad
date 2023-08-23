from pydantic import BaseModel

from .Element import Element


class Thin(Element):
    ds: float = 0.0
