from pydantic import BaseModel, Field
from src.utils.email_regex import email_regex


class UserRegisterValidator(BaseModel):
    username: str = Field(..., min_length=3)
    age: int = Field(..., gt=0)
    email: str = Field(..., pattern=email_regex)
    uf: str = Field(
        ...,
        min_length=2,
        max_length=2,
    )
