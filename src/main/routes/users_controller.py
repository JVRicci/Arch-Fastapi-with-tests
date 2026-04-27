from fastapi import APIRouter
from fastapi.responses import JsonResponse

users_controller = APIRouter(tags=["Users"])


@users_controller.post("/users")
async def create_user():
    # Logic to create a user goes here
    return JsonResponse({"message": "User created successfully"})
