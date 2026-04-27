from pydantic import BaseModel, Field


class UserRegisterValidator(BaseModel):
    username: str = Field(..., min_length=3)
    age: int = Field(..., gt=0)
    uf: str = Field(
        ...,
        min_length=2,
        max_length=2,
    )
