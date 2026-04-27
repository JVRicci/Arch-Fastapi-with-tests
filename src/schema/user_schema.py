from pydantic import BaseModel, EmailStr, Field


class UserRegisterValidator(BaseModel):
    username: str = Field(..., min_length=3, description="User's username")
    age: int = Field(..., gt=0, description="User's age, must be greater than 0")
    email: EmailStr = Field(..., description="User's email address")
    uf: str = Field(
        ...,
        min_length=2,
        max_length=2,
        description="User's state abbreviation (e.g., 'SP' for São Paulo)",
    )
