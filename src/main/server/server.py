from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.users_controller import users_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(users_controller)
