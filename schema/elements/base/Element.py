from pydantic import BaseModel
from typing import Optional


class Element(BaseModel):
    name: Optional[str] = None

    class Config:
        validate_assignment = True
