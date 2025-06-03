from typing import Optional

from pydantic import BaseModel


class GradeStatResponse(BaseModel):
    count: int
    min: Optional[int]
    max: Optional[int]
    avg: Optional[float]
