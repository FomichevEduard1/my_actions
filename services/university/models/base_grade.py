from typing import ClassVar

from pydantic import BaseModel, ConfigDict


class BaseGrade(BaseModel):
    model_config = ConfigDict(extra="forbid")

    MIN_GRADE: ClassVar[int] = 1
    MAX_GRADE: ClassVar[int] = 5

    teacher_id: int
    student_id: int
    grade: int
