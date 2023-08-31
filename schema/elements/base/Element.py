from pydantic import BaseModel
from typing import Optional


class Element(BaseModel):
    """A mix-in model for elements, defining common properties"""

    name: Optional[str] = None
    """A unique name for the element when placed in the line"""

    # Hints for pure Python usage
    class Config:
        validate_assignment = True
