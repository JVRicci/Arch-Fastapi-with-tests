from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.validators.user_register_validator import UserRegisterValidator

users_controller = APIRouter(tags=["Users"])


@users_controller.post("/users")
async def create_user(body: UserRegisterValidator):
    dict_body = dict(body)

    return JSONResponse(
        status_code=201,
        content={
            "message": "User created successfully",
            "user": dict_body,
        },
    )
