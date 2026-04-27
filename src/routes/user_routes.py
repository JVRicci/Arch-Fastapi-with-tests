from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.schema.user_schema import UserRegisterValidator
from src.controllers import user_controller

user_routes = APIRouter(prefix="/users", tags=["users"])


@user_routes.post("/")
async def create_user(body: UserRegisterValidator):

    return JSONResponse(
        status_code=201,
        content={
            "message": "User created successfully",
            # "user": dict_body,
        },
    )
