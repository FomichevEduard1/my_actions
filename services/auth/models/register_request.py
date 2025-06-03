from pydantic import BaseModel, EmailStr
from pydantic.v1 import ConfigDict


class RegisterRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    username: str
    password: str
    password_repeat: str
    email: EmailStr
